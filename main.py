
import pandas as pd


df = pd.read_csv('Store_Complaints.csv')

#clean data 
clean_data = df.dropna(axis=0)

#find value count in new data which is cleaned
clean_data.Department.value_counts()

#create new dataframe which name is 'df_2' and its contain 'Department','Complain Type' and 'Product Details' columns
df_2 = df[['Department','Complaint Type','Product Details']]

# This dataframe shows that which number of product get complaint and also to who
df_3 = df[['Product Details','Staff Name']].value_counts()

# This dataframe show which customer name have more complaints in store
df_4 = df['Customer Name'].value_counts()

# This dataframe shows  everything about 'Sophia Davis' from Customer
df_5 = df[df['Customer Name'] == 'Sophia Davis']

# The last dataframe about Sophia Davias too  but her most complaint Product, Complaint type and Staff name
most = df_5[['Product Details','Complaint Type','Staff Name']].value_counts()






print(most)
