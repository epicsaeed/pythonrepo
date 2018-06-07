


#used to add products into the database
def addItem(p,n,s,c,instock):
    c.execute("INSERT INTO stuffToPlot VALUES(p,n,s,c,instock)")
    conn.commit()
    c.close()
    conn.close()

def removeItem(p):
    c.execute('DELETE FROM data WHERE  value = (?)',p)
    conn.commit()

def editItem(oldInStock,newInStock):
    c.execute('UPDATE data SET value =(?) WHERE value =(?)',(newInStock,newInStock))
    conn.commit()

def ReadDatabase():
    c.execute('SELECT * FROM data')
    for row in c.fetchall():
        print(row)