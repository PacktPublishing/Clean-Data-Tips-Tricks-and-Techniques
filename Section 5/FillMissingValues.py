import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(2, 2),
                  index=['1', '3'],
                  columns=['key_1', 'val_1']
                  )
df = df.reindex(['1', '2'])
print(df)
print("NaN replaced with '0':")
print(df.fillna(0))
