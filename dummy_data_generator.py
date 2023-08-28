import pandas as pd
import numpy as np
import random
import os
os.chdir(r"C:\Users\tyler\shippingRIE")

order_ids_needed = 10

#first we need to build out some dummy orders
order_ids = np.arange(0,order_ids_needed,1)
line_numbers = np.arange(1,100,1)
partids = ['a','b','c','d','e','f','g']

#Random Date Generator
end_date = pd.Timestamp.today()  # Current date
date_offsets = np.random.randint(0,360,order_ids_needed).tolist()
due_dates = []
for date in date_offsets:
    due_dates.append(end_date - pd.DateOffset(days=date) )

df = pd.DataFrame({'order_id':order_ids,
                   'due_date':due_dates,
                   'lines' : np.random.randint(1,10,order_ids_needed)})


line_objects = []


for index, row in df.iterrows():
    so_id = row['order_id']
    due_date = row['due_date']
    line_count = row['lines']
    for line in range(1, line_count + 1):
        so_line_detail = {
            'order_id': f'SO-0000{so_id}',
            'due_date': due_date,
            'line_no': line,
            'part_id': np.random.choice(partids),
            'qty': np.random.randint(1, 15, 1)[0],  # Get the actual integer value
            'identifier': f'SO-0000{so_id}/{line}'
        }
        line_objects.append(so_line_detail)


test = pd.DataFrame(line_objects)
test.to_csv('excelSources/open_orders.csv')

#Build the fake inventory data
inventory = {}
for part in partids:
    count = random.randint(1,10)
    for item in range(0,count):
        serial = f'abcde{part}{count}{item}'
        inventory[serial] = (part, count, item, 1, serial)

pd.DataFrame(inventory
             , index =['part_id','total_count','item','qty','serial']).T.to_csv('excelSources/inventory_listing.csv'
            ,index=False)


            



