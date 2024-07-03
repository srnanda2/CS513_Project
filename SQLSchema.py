# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:29:43 2024

@author: Soumya Nanda
"""

import pandas as pd

# Load the CSV files
dish_df = pd.read_csv('/path/to/Dish.csv')
menu_df = pd.read_csv('/path/to/Menu.csv')
menu_item_df = pd.read_csv('/path/to/MenuItem.csv')
menu_page_df = pd.read_csv('/path/to/MenuPage.csv')

def generate_create_table_statement(table_name, df):
    columns = []
    for column_name, dtype in df.dtypes.iteritems():
        if 'int' in str(dtype):
            col_type = 'INT'
        elif 'float' in str(dtype):
            col_type = 'DECIMAL(10, 2)'
        elif 'datetime' in str(dtype):
            col_type = 'TIMESTAMP'
        else:
            col_type = 'VARCHAR(255)'
        columns.append(f"{column_name} {col_type}")
    columns_str = ",\n    ".join(columns)
    return f"CREATE TABLE {table_name} (\n    {columns_str}\n);"

# Generate SQL statements
dish_sql = generate_create_table_statement('Dish', dish_df)
menu_sql = generate_create_table_statement('Menu', menu_df)
menu_item_sql = generate_create_table_statement('MenuItem', menu_item_df)
menu_page_sql = generate_create_table_statement('MenuPage', menu_page_df)

# Print the SQL statements
print(dish_sql)
print(menu_sql)
print(menu_item_sql)
print(menu_page_sql)
