import pymysql
def createConnection():
    return pymysql.connect(host="localhost",database="sakila",user="root",password="Root@123",port=3306)
conn=createConnection()
cursor=conn.cursor()
query="create table symbiosis(id int primary key auto_increment, name varchar(30),email varchar(30),city varchar(30))"
cursor.execute(query)
conn.commit()
conn.close()
def CreateTable():
    conn=createConnection()
    cursor=conn.cursor()
    query="insert into symbiosis values(1,'a','vhhf')"
    cursor.execute(query)
    query="insert into symbiosis values(2,'b','aef')"
    cursor.execute(query)
    conn.commit()
def insertdata(name,email,city):
    conn=createConnection()
    cursor=conn.cursor()
    args=(name,email,city)
    query="insert into symbiosis (name,email,city)values(%s,%s,%s)"
    cursor.execute(query,args)
    conn.commit()
    conn.close()
def removedata(id):
    conn=createConnection()
    cursor=conn.cursor()
    query="delete from symbiosis where id=(%s)"
    cursor.execute(query,id)
    conn.commit()
    conn.close()
def reset():
    conn=createConnection()
    cursor=conn.cursor()
    query="alter table symbiosis auto_increment =1"
    cursor.execute(query)
    conn.commit()
def UpdateT(id,name,email,city):
    conn=createConnection()
    cursor=conn.cursor()
    args=(name,email,city,id)
    query="update symbiosis set name=%s,email=%s,city=%s where id=%s "
    cursor.execute(query,args)
    conn.commit()
    conn.close()
UpdateT(5,"aofeh","aoehf","faoiehf")
def Get():
    conn=createConnection()
    cursor=conn.cursor()
    query="select * from symbiosis "

    cursor.execute(query)
    a=cursor.fetchall()
    conn.commit()
    conn.close()
    print(a)
Get()
def ShowById(sid,aid):
    conn=createConnection()
    cursor=conn.cursor()
    args=(sid,aid)
    query="select * from actor where actor_id between %s and %s"
    cursor.execute(query,args)
    a=cursor.fetchall()
    conn.commit()
    conn.close()
    return a
ShowById(100,120)
