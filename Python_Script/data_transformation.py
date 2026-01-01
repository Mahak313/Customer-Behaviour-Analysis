import pandas as pd

# Option 1: raw string(r)-error avoid krta hai
df = pd.read_csv(r'C:\Users\Mahak shrivastav\Downloads\customer_shopping_behavior.csv')


# First 5 rows dekhen
df.head()
print(df.head())

df.info()   #tells about column ,data type ,non-null count
df.describe()       #gives statistical summary of numerical columns
print(df.describe(include='all'))

df.isnull().sum()   #missing values check karne ke liye
print(df.isnull().sum())


#removing missing values(filling missing values with median of that category)
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
df.isnull().sum()
print(df.isnull().sum())


#making code more effiecient and readable data 
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

#printing all column exist in dataset
print(df.columns)  #➡ Check karne ke liye ke column sahi rename hue ya nahi.

#Create a column age_group
labels=['young Adult','Adult','Middle-aged','Senior ']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
df[['age','age_group']].head(10)
print(df[['age','age_group']].head(10))   #➡ Age aur age_group ke first 10 rows dikhata hai.

# createcolumn purchase_frequency_days
frequency_mapping ={
    'Fortnightly':14,
    'weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14, 
    'Annually':365,
    'Every 3 Months':90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days','frequency_of_purchases']].head(10)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))


#Check ki kya discount aur promo code ek hi baat hai?
df[['discount_applied','promo_code_used']].head(10)
print(df[['discount_applied','promo_code_used']].head(10))

# Columns equal hai ya nahi
(df['discount_applied']==df['promo_code_used']).all()
print((df['discount_applied']==df['promo_code_used']).all()) #➡ True aayega agar dono column same hai to warna False aayega.

df=df.drop('promo_code_used',axis=1)  #➡ promo_code_used column drop kar diya kyunki dono column same the.
df.columns
print(df.columns)

