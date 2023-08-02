
import pandas as pd


df = pd.read_csv('Store_Complaints.csv')


clean_data = df.dropna(axis=0)

clean_data.Department.value_counts()


df_2 = df[['Department','Complaint Type','Product Details']]

df_3 = df[['Product Details','Staff Name']].value_counts()

df_4 = df['Customer Name'].value_counts()


df_5 = df[df['Customer Name'] == 'Sophia Davis']

most = df_5[['Product Details','Complaint Type','Staff Name']].value_counts()






print(most)