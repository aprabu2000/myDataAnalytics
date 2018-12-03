import pandas as pd
df = pd.DataFrame(1,2,3,4,5)
df.to_excel('output.xlsx', header=False, index=False)
