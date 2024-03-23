import pandas as pd
​
# We need to find the multiplier which convert EURO to USD 
# In order to reach this we need to google it to find the current multiplier to convert EURO to USD
​
multiplier = 1.11
​

def process_amount_raised(value):
    try:
        if isinstance(value, str):
            value = value.replace("€", "").replace(",", "")
            value = float(value) * multiplier
            value = int(value)
        return value
    except ValueError:
        return value
​
df["AMOUNT_RAISED"] = df["AMOUNT_RAISED"].apply(process_amount_raised)

​
# PRINT 
print(df)