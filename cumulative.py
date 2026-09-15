import sqlite3
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

conn = sqlite3.connect('db/lesson.db')

query = """
SELECT o.order_id, o.date, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
"""
df = pd.read_sql_query(query, conn)

def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

df['cumulative'] = df['total_price'].cumsum()


# Line plot
df.plot(x= "order_id", y="cumulative", kind="line", title= "Cumulative Revenue VS. Order ID")
plt.show()