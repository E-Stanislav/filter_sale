import pandas as pd
df = pd.read_csv('pp-complete.csv', header=None)

col = ['Transaction unique identifier' , 'Price','Date of Transfer','Postcode','Property Type','Old/New',
       'Duration','PAON','SAON','Street','Locality', 'Town/City','District','County','PPD Category Type','Record Status - monthly file only']

df.columns = col
new_df = df['Postcode'].value_counts().reset_index()
one_postcode = new_df[new_df['Postcode'] == 1]['index'].to_list()
df[df['Postcode'].isin(one_postcode)].to_csv('one sale.csv', index = False)