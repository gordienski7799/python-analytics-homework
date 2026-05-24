import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 500, 500]}
df = pd.DataFrame(data)
print("Продажі по містах:")
print("Середнє значення:", df["sales"].mean())
print(df)