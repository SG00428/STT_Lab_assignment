import os
import json
import pandas as pd
from collections import Counter

repositories = ["pyinfra", "yellowbrick", "scapy"]  # Replace with actual repo names

repo_results = {}

for repo in repositories:
    repo_dir = os.path.join(os.getcwd(), repo, "commits")  # JSON files stored in 'commits' folder
    if not os.path.exists(repo_dir):
        print(f"Skipping {repo}, commits folder not found.")
        continue

    print(f"Processing {repo}...")

    results = []
    for filename in os.listdir(repo_dir):
        if filename.endswith(".json"):
            commit_hash = filename.replace("bandit_output_", "").replace(".json", "")
            file_path = os.path.join(repo_dir, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                results.append({
                    "commit": commit_hash,
                    "high_confidence": sum(1 for issue in data["results"] if issue["issue_confidence"] == "HIGH"),
                    "medium_confidence": sum(1 for issue in data["results"] if issue["issue_confidence"] == "MEDIUM"),
                    "low_confidence": sum(1 for issue in data["results"] if issue["issue_confidence"] == "LOW"),
                    "high_severity": sum(1 for issue in data["results"] if issue["issue_severity"] == "HIGH"),
                    "medium_severity": sum(1 for issue in data["results"] if issue["issue_severity"] == "MEDIUM"),
                    "low_severity": sum(1 for issue in data["results"] if issue["issue_severity"] == "LOW"),
                    "cwes": [issue["test_id"] for issue in data["results"]]  # Collect CWEs
                })

    df = pd.DataFrame(results)
    df.to_csv(f"{repo}_bandit_analysis.csv", index=False)
    repo_results[repo] = df

    print(f"Analysis completed for {repo}. Results saved as {repo}_bandit_analysis.csv.")

print("All repositories analyzed!")
