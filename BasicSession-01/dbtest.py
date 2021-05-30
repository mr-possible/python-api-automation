from utils.dbUtil import DbUtil
from dbqueries import getQueries

conn = DbUtil().giveMeConnection()
assert conn, 'Connection is not established !! Check your dbUtil.py for any error or malicious code.'

query = getQueries.getCustomerInfo
cursor = conn.cursor()
cursor.execute(query)
print(cursor.fetchall())
