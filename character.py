from collections import Counter
import re
prices = df['AMOUNT_RAISED'].tolist()
​
text = ' '.join(str(price) for price in prices)
​
# First of all I need to find all characters which exist in my database
currency_symbols = re.findall(r'[^\d\.\s]+', text)
​
# Now I need to count all of them
currency_counts = dict(Counter(currency_symbols))
​
# Print it
for currency, count in currency_counts.items():
    print(f'{currency}: {count}')