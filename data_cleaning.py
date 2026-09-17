import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Automobile.csv')
# col of the data and info about it
print(df.columns)
print("info about numerical col of data :\n",df.describe())
print("info about the data:\n",df.info())
# missing values=6 from col horsepower
print(df.isnull().sum())
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())
# duplicate =none
print(df.duplicated().sum())
# rename the name col to manufacturer
df['manufacturer']=df['name'].str.split().str[0].str.lower()
# Correcting car model names
fix_manufactor={
'chevroelt': 'chevrolet',
    'chevy': 'chevrolet',
    'maxda': 'mazda',
    'toyouta': 'toyota',
    'vokswagen': 'volkswagen',
    'vw': 'volkswagen',
    'mercedes': 'mercedes-benz',
    'capri': 'ford',
    'hi': 'plymouth',
}
df['manufacturer']=df['manufacturer'].replace(fix_manufactor)
# model_year: Add a column for the full, readable model year.
df['model_year_full'] = 1900 + df['model_year']
# origin: Standardizing character formatting
df['origin'] = df['origin'].str.capitalize()
# Extract the remainder of the name as the model (the name excluding the initial company name).
df['model'] = df.apply(
    lambda r: r['name'][len(r['name'].split()[0]):].strip(), axis=1
)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
cols = ['mpg', 'horsepower', 'weight']
for ax, col in zip(axes, cols):
    ax.boxplot(df[col], orientation='vertical')
    ax.set_title(col)
plt.tight_layout()
plt.savefig("boxplots.png", dpi=130)
print("تم الحفظ: boxplots.png")
