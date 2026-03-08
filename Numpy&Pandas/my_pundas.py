import numpy as np
import pandas as pd

# dict1={
#     "name":['irfan','sahab','anis','imam'],
#     "marks":[92,90,85,70],
#     "city":['chittagong','Bashnkhali','Patiya','Patiya']
# }
# df=pd.DataFrame(dict1)
# print(df)
# #df.to_csv('iiuc.csv')

# print("only 2 data________________________________ \n", df.head(2))

# print("last 2 data________________________________ \n", df.tail(2))
# print(df.describe())
# #----SERIES---
# newdf=pd.DataFrame(np.random.rand(10,5))
# ages=pd.Series([25,30,35,40],name='Ages')
# print(ages)
# print(newdf)
# #print(newdf.T)
# newdf2=newdf
# newdf2[0][0]=9783
# print(newdf2)
# #remove column
# print(newdf.drop(0,axis=1))



titanic_data = {
    'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    'Pclass': [3, 1, 3, 1, 3, 3, 1, 3, 2, 3, 1, 3],
    'Name': ['Braund, Mr. Owen Harris', 'Cumings, Mrs. John Bradley',
             'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques Heath',
             'Allen, Mr. William Henry', 'Moran, Mr. James',
             'McCarthy, Mr. Timothy J', 'Palsson, Master. Gosta Leonard',
             'Johnson, Mrs. Oscar W', 'Nasser, Mrs. Nicholas',
             'Sandstrom, Miss. Marguerite Rut', 'Bonnell, Miss. Elizabeth'],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male',
            'male', 'male', 'female', 'female', 'female', 'female'],
    'Age': [22.0, 38.0, 26.0, 35.0, 35.0, None, 54.0, 2.0, 27.0, 14.0, 4.0, 58.0],
    'Fare': [7.25, 71.28, 7.92, 53.1, 8.05, 8.46, 51.86, 21.08, 11.13, 30.07, 16.7, 26.55]
}
df=pd.DataFrame(titanic_data)
# print(df.info())
# print(df.shape)
# name=df['Name']#retuen series(1D)Array
# print(name)
# print(type(name))
# subset=df[['Name','Age','Sex']]#retuen dataframe(2D)Array
# print(type(subset))
# print(subset.head(3))

#______ILOC AND LOC_______
# print("iloc example(position based):")
# print("retuen first position(row):")
# print(df.iloc[0])
# print("retuen first 0 to 2 position(row):")
# print(df.iloc[0:3])
# print("retuen 2,4,6 specific position(row):")
# print(df.iloc[[2,4,6]])


# print("retuen first position(row):")
# print(df.loc[0])
# print("retuen first 0 to 3 position(row):")
# print(df.loc[0:3])
# print("return specific row and column which i want:")
# print(df.loc[0:2,['Name','Age']])
# print("return fixed row and column which i want:")
#print(df.loc[[1,2],['Age','Sex']])

#______Filtering Data with Conditions_____
# age_withrange=df['Age']>30
# print("Age>30")
# print(age_withrange)
# print(type(age_withrange))
#adults=df[df['Age']>30]#DataFrame
#print(adults)
#print(type(adults))
#print(adults[['Name','Age']])


# print(" Female passengers:")
# females = df[df['Sex'] == 'female']
# print(females[['Name','Age','Sex']])

#______Combining conditions with & (AND)_____
# print("Female Passenger older than 25")
# young_female=df[(df['Sex'] == 'female') & (df['Age']>25)]
# print(young_female)

#______Combining conditions with | (or)_____
# print("People in first class and survived")
# first_or_survived=df[(df['Pclass']==1) | (df['Survived']==1)]
# print(first_or_survived)

#_____unique() and value_counts()____
# print("Unique value in sex column:")
# print(df['Sex'].unique())
# print("count how many Unique value in sex column column:")
# print(df['Sex'].value_counts())
# print("Unique value in pclass column:")
# print(df['Pclass'].unique())
# print("count how many Unique value in sex column column:")
# print(df['Pclass'].value_counts())

#_____Sorting____
# sortby_age=df.sort_values(by='Age')
# print(sortby_age[['Name','Age']].head())
# print("sorted by age oldest to young:")
# sortedby_age_des=df.sort_values(by='Age',ascending=False)
# print(sortedby_age_des[['Name','Age']].head())
# print("sorted by class(ascending) and Fare(descending):")
# multi_sort=df.sort_values(by=['Pclass','Age'],ascending=[True,False])
# print(multi_sort.head(5))


#________Section 9: Handling Missing Data (NaN)______
# print("missing value in each column:")
# missing_data=df.isnull().sum()
# print(missing_data)
# print("rows with missing age values:")
# missing_age_rows=df[df['Age'].isnull()]
# print(missing_age_rows[['Name','Age']])
#____Remove missing data
# print("\nOriginal shape:", df.shape)
# remove_missing_row=df.dropna()
# print("After removing missing row:\n",remove_missing_row)

#____filling missing data(NAN)
#df_filled_zero=df.copy()
# df_filled_zero['Age'].fillna(0,inplace=True)
# print("Filled with zero: ",df_filled_zero['Age'].tolist())
# age_mean=df_filled_zero['Age'].mean()
# df_filled_zero['Age'].fillna(age_mean,inplace=True)
# print(f"Filled with mean({age_mean:.1f}):",df_filled_zero['Age'].tolist())

#________Dropping and Renaming Columns___
#new_dataF=df.copy()
# df_dropped=new_dataF.drop(['PassengerId', 'Sex',],axis=1)
# # print(df_dropped)
# print(list(df_dropped.columns))

# print("\n Renaming columns:")
# df_renamed = new_dataF.rename(columns={
#     'Pclass': 'PassengerClass',
#     'Sex': 'Gender',
#     'Age': 'AgeInYears',
#     'Fare': 'TicketPrice'
# })
# print(list(df_renamed.columns))
# grouped=new_dataF.groupby('Sex')
# print("Group created\n",list(grouped.groups.keys()))

#__Section 15: Combining DataFrames with concat and merge________

# Let's create some example DataFrames for demonstration
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
})

df2 = pd.DataFrame({
    'Name': ['David', 'Eve', 'Frank'],
    'Age': [28, 32, 29],
    'City': ['Boston', 'Seattle', 'Miami']
})
# print("DataFrame 1:\n",df1)
# print("DataFrame 2:\n",df2)
#concatation
# combined=pd.concat([df1,df2],ignore_index=True)
# print(combined)

# Merging - Joining DataFrames on common columns
# Create DataFrames with a common column to join on
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28]
})

orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerID': [1, 2, 2, 3, 5],  # Note: CustomerID 5 doesn't exist in customers data!
    'Product': ['Laptop', 'Phone', 'Tablet', 'Camera', 'Watch'],
    'Amount': [1000, 800, 300, 600, 200]
})
# inner_marged=pd.merge(customers,orders,on='CustomerID',how='inner')
# print(inner_marged)

# left_marged=pd.merge(customers,orders,on='CustomerID',how='left')
# print(left_marged)

# right_marged=pd.merge(customers,orders,on='CustomerID',how='right')
# print(right_marged)
# outer_marged=pd.merge(customers,orders,on='CustomerID',how='outer')
# print(outer_marged)




import pandas as pd
import numpy as np

df3 = pd.DataFrame({
    'A': [21, np.nan, 22, 4, np.nan],
    'B': [31, 32, 33, 34, 35],
    'C': [np.nan, np.nan, np.nan, np.nan, np.nan],
    'D': [46, 47, np.nan, 48, 49]
})

print(df3)
print(df3.isnull().sum())
print(df3.fillna(method='ffill'))
print(df3.fillna(method='bfill'))
print(df3.fillna(0))