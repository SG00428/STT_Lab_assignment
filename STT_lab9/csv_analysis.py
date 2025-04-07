import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Sneha Gautam\Downloads\junit4\output\TypeMetrics.csv"
df = pd.read_csv(file_path)

high_lcom_threshold = 500  # adjustable
df_high_lcom = df[(df["LCOM1"] > high_lcom_threshold) | (df["LCOM5"] > 0.9) | (df["YALCOM"] > 0.9)]

print("Classes with High LCOM:")
print(df_high_lcom[["Type Name", "LCOM1", "LCOM5", "YALCOM"]])

columns = ["Type Name", "LCOM1", "LCOM2", "LCOM3", "LCOM4", "LCOM5", "YALCOM"]
df_selected = df[columns]

# LCOM values in a table format
print(df_selected.to_string(index=False))

# bar chart 
plt.figure(figsize=(12, 6))
df_selected.set_index("Type Name").plot(kind="bar", stacked=True, figsize=(12, 6), colormap="viridis")
plt.title("Comparison of LCOM Metrics for Classes")
plt.xlabel("Classes")
plt.ylabel("LCOM Values")
plt.xticks(rotation=90)
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
