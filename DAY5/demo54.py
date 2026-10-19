import sqlite3
conn = sqlite3.connect('products.db')
sth = conn.cursor()
sth.execute("create table product(id INT,pname TEXT,pcost NUMBER)")
sth.execute("insert into product(id,pname,pcost) values(101,'pA',1000)")
sth.execute("insert into product(id,pname,pcost) values(102,'pB',2000)")
sth.execute("insert into product(id,pname,pcost) values(103,'pC',3000)")
va = 104
vb = 'pD'
vc = 4000
sth.execute("insert into product(id,pname,pcost) values(?,?,?)",(va,vb,vc))
conn.commit()
conn.close()