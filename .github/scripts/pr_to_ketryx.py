"""Open or refresh a Ketryx Change Request that represents this pull request.

The CR carries the PR title, description, changed files and diff, so the
"PR to DFMEA" agent in Ketryx can assess DFMEA coverage from the CR alone.
Re-running on new commits updates the same CR (sourceId = github/<repo>/pr-<n>).
"""
import json
import os
import subprocess
import sys
import urllib.request

MAX_DIFF_CHARS = 30000

url = os.environ.get("KETRYX_URL", "https://demo.ketryx.com").rstrip("/")
project = os.environ["KETRYX_PROJECT"]
key = os.environ["KETRYX_API_KEY"]
repo = os.environ["GITHUB_REPOSITORY"]
event = json.load(open(os.environ["GITHUB_EVENT_PATH"]))
pr = event["pull_request"]
base, head = pr["base"]["sha"], pr["head"]["sha"]


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


files = git("diff", "--name-status", f"{base}...{head}").strip()
diff = git("diff", f"{base}...{head}")
if len(diff) > MAX_DIFF_CHARS:
    diff = diff[:MAX_DIFF_CHARS] + "\n... (diff truncated)"

description = "\n".join([
    f"Pull request #{pr['number']}: {pr['title']}",
    f"Link: {pr['html_url']}",
    f"Author: {pr['user']['login']}  Branch: {pr['head']['ref']} -> {pr['base']['ref']}  Head commit: {head[:7]}",
    "",
    "PR description:",
    pr.get("body") or "(none)",
    "",
    "Changed files:",
    files,
    "",
    "Diff:",
    diff,
])

payload = {"itemData": {
    "sourceId": f"github/{repo}/pr-{pr['number']}",
    "type": "Change Request",
    "title": f"PR #{pr['number']}: {pr['title']}",
    "statusName": "Open",
    "fields": [
        {"label": "Description", "type": "string", "value": description},
        {"label": "Reason for change", "type": "string", "value": pr.get("body") or pr["title"]},
    ],
}}

req = urllib.request.Request(
    f"{url}/api/v1/projects/{project}/items",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    method="POST",
)
result = json.load(urllib.request.urlopen(req))["item"]
if not result.get("success"):
    print("Ketryx rejected the change request:", json.dumps(result.get("warnings")), file=sys.stderr)
    sys.exit(1)

item_url = f"{url}/projects/{project}/items/{result['id']}"
print(f"Change request {result['id']} -> {item_url}")
for w in result.get("warnings") or []:
    print("warning:", json.dumps(w))
with open(os.environ["GITHUB_OUTPUT"], "a") as out:
    out.write(f"item_id={result['id']}\nitem_url={item_url}\n")
