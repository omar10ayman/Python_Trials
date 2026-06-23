import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\DELL\Desktop\Employee Sample Data 1.csv",
    encoding="latin1"
)
df["Annual Salary"]=(
    df["Annual Salary"].
    replace(r"[\$,]","",regex=True).
    astype(float)
    )
df.at[0,'Annual Salary']=None
df.at[1,'Job Title']=None
df.at[2,'Job Title']="Ai"
df=df[['Full Name','Job Title','Annual Salary']].head(10)
print(df)
print(df.index)
print(df.columns)
print(df.values)
print(df.shape)
print(df.size)
print(df.dtypes)
print(df.empty)
print(df.isna())
print(df.notna())
print(df.describe())
print(df.ndim)
print(df.info())
print(df.head(2))
print(df.tail(2))
print(df.isnull().sum())
# remove nan values
drop=df.dropna()
print(drop)
dropِAll=df.dropna(how='all')
print(dropِAll)
dropِSpecfic=df.dropna(subset=['Job Title','Annual Salary'])
print(dropِSpecfic)
# fill nan values
# df=df.fillna(value=0)
# print(df)
df=df.fillna({
    'Annual Salary' : 484,
    'Job Title' : 'Ai'
})
print(df)

df=df.sort_values(by='Annual Salary')
print(df)
# Copy 
df_copy =df.copy()
print(df_copy)
# rename colums
# inplace=True => changed in orgin dataframe
df.rename(columns={'Annual Salary':'Salary'}, inplace=True)
print(df)
# Editing
df['Salary'] =df['Salary']*10
print(df)
# grouping => has same features put in same group
# df=df[['Full Name','Job Title','Salary']]
df_group =df.groupby('Job Title')['Salary'].sum()
print(df_group)
df_group1 =df.groupby('Job Title').count()
print(df_group1)
# adding columns
print(len(df))
df['status']=[0,1]*(len(df)//2)
print(df)
# aggragtion => if you need make some operators like mean , sum ,std
# df_agg = df.groupby('Job Title').agg({
#     'Salary' :['mean']
# })
# print(df_agg)
print(df)
# melt => melt 2 colunms to convert one column
df_melt = df.melt(
    
    id_vars='Full Name',
    value_vars=['Job Title','Salary'],
    var_name='melted',
    value_name='collected',
    ignore_index=True

)
print(df_melt)
# pivot invearse melt
df_pivot = df_melt.pivot(index='Full Name',columns='melted',values='collected')
print(df_pivot)
# stack => convert colums to rows
df_stack = df.set_index('Full Name').stack()
print(df_stack)
# unstack => convert to unstack
df_unStack=df_stack.unstack()
print(df_unStack)
# concat => must be same columns names
new = pd.DataFrame({
    'a' :[1,2,3],
    'b' :[5,6,7],
})
new1 = pd.DataFrame({
    'a' :[7,8,9],
    'b' :[10,11,12],
})
all=pd.concat([new,new1],ignore_index=True)
print(all)
print("="*20)
# mearge => merge two dframes but by condition
new = pd.DataFrame({
    'a' :[1,2,3],
    'b' :[5,6,7],
})
new1 = pd.DataFrame({
    'a' :[1,2],
    'z' :[10,11],
})
meraged = pd.merge(new,new1,on='a',how='right')
meraged = pd.merge(new,new1,on='a',how='left')
meraged = pd.merge(new,new1,on='a',how='inner')
meraged = pd.merge(new,new1,on='a',how='outer')
print(meraged)

# join => join by index ,must not be same columns names
new = pd.DataFrame({
    'a' :[1,2,3],
    'b' :[5,6,7],
},index=[0,1,2])
new1 = pd.DataFrame({
    'c' :[7,8,9],
    'd' :[10,11,12],
},index=[0,1,2])
joined=new.join(new1)
print(joined)
# Data
import pandas as pd

dates = [
    '2025-06-01',
    '2025-06-02',
    '2025-06-15',
    '2025-07-10',
    '2025-07-25',
    '2025-07-30',
    '2025-08-01',
    '2025-08-15'
]

sales = [10, 5, 7, 8, 2, 5, 1, 3]
data = pd.DataFrame({'str_date': dates,'sales':sales})

data['date'] = pd.to_datetime(data['str_date'])


data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day'] = data['date'].dt.day
data['day_name'] = data['date'].dt.day_name()
data['weekday'] = data['date'].dt.weekday
print(data)
# current sales
sales_grouped=data.groupby('month')['sales'].sum()
# last sales
sales_last=data.groupby('month')['sales'].sum().shift(1).fillna(value=0)
print(sales_grouped)
print(sales_last)
# filtered
print(df[df['Salary']>10000])
filtered= df.query('Salary > 10000')
print(filtered)
# reindex 
# df =df.reindex([1,2,3])
# visualzation
print(df)
plt.bar(df['Job Title'],df['Salary'])
plt.xticks(rotation=45)
plt.xlabel('Job Title')
plt.ylabel('Salary')
plt.show()


























