import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

# Iterating through a DataFrame using iterrows()
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['name']}, Local Price: {row['local_price']}, Dollar Price: {row['dollar_price']}")

# Iterating through a DataFrame using apply()
def get_country_name(row):
    return f"Name: {row['name']}, Local Price: {row['local_price']}, Dollar Price: {row['dollar_price']}"
    
result = df.apply(get_country_name, axis=1)
print(result)