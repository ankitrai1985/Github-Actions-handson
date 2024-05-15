import requests

def delete_workflow_run(repo_owner, repo_name, run_id, access_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}"
    headers = {"Authorization": f"token {access_token}"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully deleted workflow run {run_id}")
    else:
        print(f"Failed to delete workflow run {run_id}: {response.status_code}")

def list_workflow_runs(repo_owner, repo_name, access_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs"
    headers = {"Authorization": f"token {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["workflow_runs"]
    else:
        print(f"Failed to list workflow runs: {response.status_code}")
        return []

def main():
    repo_owner = "ankitrai1985"
    repo_name = "Github-Actions-handson"
    access_token = "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"

    # List all workflow runs
    workflow_runs = list_workflow_runs(repo_owner, repo_name, access_token)

    # Delete workflow runs based on some criteria (e.g., older than a certain date)
    # for run in workflow_runs:
    #     delete_workflow_run(repo_owner, repo_name, run["id"], access_token)

if __name__ == "__main__":
    main()
