# %%

import pandas as pd

df = pd.read_csv('diamonds.csv', sep=';')
df1 = pd.read_csv('new-diamonds.csv', sep=';')

df.head()
# %%
Price = -5269 + 8413 * 1 + 158.1 * 1 + 454 * 1
Price
# %%
Price1 = -5269 + 8413 * 2 + 158.1 * 1 + 454 * 1
Price1
# %%
Dif = Price1 - Price 
Dif
# %%
MyDiamond = -5269 + 8413 * 1.5 + 158.1 * 3 + 454 * 5
MyDiamond
# %%
df1.head()
# %%
df1['price'] = -5269 + 8413 * df1['carat'] + 158.1 * df1['cut_ord'] + 454 * df1['clarity_ord']
df1.head(20)

# %%
frames = [df, df1]
result = pd.concat(frames)

result
# %%
import seaborn
# %%
seaborn.scatterplot(x="cut",
                    y="price",
                    data=result)
# %%
import seaborn as sns
import matplotlib.pyplot as plt

# Criando um gráfico de dispersão
plt.figure(figsize=(10, 6)) 

sns.scatterplot(x=df['carat'], y=df['price'], label='Diamonds Original', color='blue')

sns.scatterplot(x=df1['carat'], y=df1['price'], label='Diamonds New Predictiv', color='red')


# Labels e títulos 
plt.xlabel('Carat')
plt.ylabel('Price')
plt.title('Scatter Plot Datasets')

# legenda
plt.legend()

# Mostrar o gráfico 
plt.show()
# %%
import seaborn as sns
import matplotlib.pyplot as plt

# Criando um gráfico de linhas 
plt.figure(figsize=(10, 6))  


sns.lineplot(x=df['carat'], y=df['price'], label='Diamonds Original', color='blue')

sns.lineplot(x=df1['carat'], y=df1['price'], label='Diamonds New Predictiv', color='orange')

# Labels e títulos 
plt.xlabel('Carat')
plt.ylabel('Price')
plt.title('Datasets Plot')

# legenda
plt.legend()

# Mostrar o gráfico 
plt.show()
# %%
sumValuesPred = sum(df1['price'])
# %%
sumValuesPred
# %%
sum_30_percent_discount = sumValuesPred * 0.70
# %%
sum_30_percent_discount
# %%
