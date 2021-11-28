import sqlite3

con = sqlite3.connect('C:\git\pyCodeBasement\SQL\\SHOPPING.db')
cur = con.cursor()
cur.execute("select * from shopping")
for row in enumerate(cur, 1):
    print(row)
def add_item(cur, table, id, name, amount, maavar):
    cur.execute(f'INSERT INTO {table} VALUES ({id}, "{name}",{amount}, {maavar})')
#cur.execute("INSERT INTO shopping VALUES (8, 'humus', 12, 7)")
add_item(cur, "shopping", 8, 'humus', 12, 7)
cur.execute("UPDATE shopping SET amount=14 WHERE id = {'humus'}")
cur.execute("DELETE FROM shopping WHERE name = 'humus'")
for row in enumerate(cur, 1):
    print(row)
con.commit()
con.close()