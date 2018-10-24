import pandas as pd

df = pd.DataFrame({'one': [10, 20, 30, 40, 50, 2000],
                   'two': [1000, 0, 30, 40, 50, 60]})
print("-----Original------\n", df)
print("-----Replaced------\n", df.replace({1000: 10, 2000: 60}))
