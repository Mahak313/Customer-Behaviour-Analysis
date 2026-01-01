import pyodbc

conn = pyodbc.connect(
'Driver={ODBC Driver 18 for SQL Server};'
'Server=LAPTOP-NOF12KKI\SQLEXPRESS;'
'Database=customer_behavior;'
'Trusted_Connection=yes;'
'Encrypt=no;'
)
cursor = conn.cursor()
print("Connection successful!")

