import sqlite3
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

conn = sqlite3.connect('db/lesson.db')

query = """
SELECT last_name, SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o 
ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id
"""

results = pd.read_sql_query(query, conn)

# Main app content
st.title("Employee Results")

# Bar Graph
bar_chart = px.bar(results, x='last_name', y= 'revenue', barmode='group')
st.plotly_chart(bar_chart)

