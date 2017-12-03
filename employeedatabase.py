import collections
import sqlite3
import json

#connect to database
conn = sqlite3.connect("employees.db")

# Create table
# conn.execute('''CREATE TABLE employees
#             (eid text, ename text, hiredate text)''')

# Insert a row of data
conn.execute("INSERT INTO employees VALUES ('Fred','Bloggs','2017-01-01')")
conn.execute("INSERT INTO employees VALUES ('Jo','Talbot','2017-02-02')")
conn.execute("INSERT INTO employees VALUES ('Barry','Johns','2017-03-03')")
conn.execute("INSERT INTO employees VALUES ('Kevin','Smith','2017-04-04')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


#connect to database
conn = sqlite3.connect("employees.db")

#Fetch rows
sql = "SELECT * from employees"
cursor = conn.cursor()
cursor.execute(sql)
data = cursor.fetchall()

#Converting data into json
user_list = []
for row in data :
    print('row: ', row)
    d = collections.OrderedDict()
    d['eid'] = row[0] #name
    d['ename'] = row[1] #lname
    d['hiredate'] = row[2] #email
    user_list.append(d)
stuff = json.dumps(user_list)
print(stuff)