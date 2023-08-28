import pathlib as path
import os

import pandas as pd
import numpy as np

class Picklist():
    pass

class OpenOrderFile():
    required_columns = ['part_id','due_date','product_code','order_qty','shipped_qty','customer_po_ref']
    def __init__(self,open_order_data):
        self.df = open_order_data
        test = self._validate_import()
        if test == True:
            self = self._clean_data()
    def _clean_data(self):
        df = self.df
        df = df.assign(
            part_id = df.part_id.astype(str),
            due_date = pd.to_datetime(df.due_date),
            order_qty = df.order_qty.astype(int),
            shipped_qty = df.shipped_qty.astype(int),
            open_qty = df.order_qty  - df.shipped_qty, #This may be a break point
            product_code  = df.product_code.astype(pd.Categorical),  
            order_type = df['customer_po_ref'].apply(lambda x: self._categorize_cust_po_ref(x)).attype(pd.Categorical)
        )
        self.df = df
        return self
    def _validate_import(self):
        columns = self.df.columns
        for column in self.required_columns:
            if column not in columns:
                print(f"Error {column} is required in DataFrame")
                return False
        return True
    
    def _categorize_cust_po_ref(po_ref:str):
        keys = {'PROSTAFF':'PRO','VIP':'VIP','MARKETING':'MARK','SAMPLE':"SAMPLE",'EMP':'EMP',
                'EMPLOYEE':'EMP'}
        if po_ref.upper() in keys.keys:
            return keys[po_ref]
        return None
        
            



class SerializedInventory():
    pass
