import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_id = input("Please enter the product id: ")

opinions = pd.read_json(f"opinions/{product_id}.json")

opinions_count = len(opinions)
pros_count = opinions["pros"].map(bool).sum()
print(pros_count)