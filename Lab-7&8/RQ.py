import matplotlib.pyplot as plt
import pandas as pd

repo = "yellowbrick"  # change this for other repositories
df = pd.read_csv(f"{repo}_bandit_analysis.csv")

########## RQ1 ############

plt.figure(figsize=(12, 5))
plt.plot(df["commit"], df["high_severity"], marker="o", linestyle="-", color="red", label="High Severity Issues")
plt.xlabel("Commits")
plt.ylabel("High Severity Issues")
plt.xticks(rotation=90)
plt.title(f"High Severity Issues Over Time ({repo})")
plt.legend()
plt.grid()
plt.show()


########## RQ2 ############

plt.figure(figsize=(12, 5))
plt.plot(df["commit"], df["high_severity"], label="High", color="red", marker="o")
plt.plot(df["commit"], df["medium_severity"], label="Medium", color="orange", marker="o")
plt.plot(df["commit"], df["low_severity"], label="Low", color="blue", marker="o")

plt.xlabel("Commits")
plt.ylabel("Number of Issues")
plt.title(f"Severity Trends Over Time ({repo})")
plt.legend()
plt.xticks(rotation=90)
plt.grid()
plt.show()


########## RQ3 ############


from collections import Counter

all_cwes = []
for cwe_list in df["cwes"]:
    all_cwes.extend(eval(cwe_list)) 

cwe_counts = Counter(all_cwes)
top_cwes = cwe_counts.most_common(10)

# Plot CWE frequency
plt.figure(figsize=(10, 5))
plt.barh([cwe[0] for cwe in top_cwes], [cwe[1] for cwe in top_cwes], color="purple")
plt.xlabel("Occurrences")
plt.ylabel("CWE ID")
plt.title(f"Most Frequent CWEs in {repo}")
plt.gca().invert_yaxis()  # Highest count at top
plt.show()


