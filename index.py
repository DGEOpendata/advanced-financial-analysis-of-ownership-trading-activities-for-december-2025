python
import pandas as pd

# Load the dataset
file_path = 'Ownership_Trading_Summary_DEC.xlsx'
df = pd.read_excel(file_path)

# Example analysis: Calculate total trades for each category
category_trades = df.groupby('Category').agg({'Number_of_Trades': 'sum'})
print("Total trades for each category:")
print(category_trades)

# Example analysis: Calculate net buy-sell value for each category
df['Net_Buy_Sell'] = df['Buy_Value_AED'] - df['Sell_Value_AED']
category_net_values = df.groupby('Category').agg({'Net_Buy_Sell': 'sum'})
print("Net buy-sell values for each category:")
print(category_net_values)

# Example analysis: Compare trading volumes between GCC and other categories
gcc_volume = df[df['Category'] == 'GCC']['Trading_Volume'].sum()
other_volume = df[df['Category'] != 'GCC']['Trading_Volume'].sum()
print("GCC Trading Volume:", gcc_volume)
print("Other Categories Trading Volume:", other_volume)
