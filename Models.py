import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,MetaData,Table,Insert,Column,Integer,String,Select,text
import os
from sqlalchemy.sql.expression import update,insert,delete

# conn= sqlite3.connect('sample.db')
# try:
#     query="""CREATE TABLE product_And_transactions(product_name STRING,quantity INTEGER,purchases INTEGER,sales INTEGER)"""
#     cur=conn.cursor()
#     cur.execute(query)
# except sqlite3.OperationalError as err:
#     print("Already table exist")
# cur=conn.cursor()
# print(cur.fetchall())




# engine=create_engine('sqlite:///sample.db',echo=True)
# meta=MetaData()

# work_table=Table("product_And_transactions",meta,
#                 Column("id",Integer,primary_key=True),
#                 Column("product_name",String),
#                 Column("quantity",Integer),
#                 Column("purchases",Integer),
#                 Column("sales",Integer)
#                 )
class MainDB_class:

    def __init__(self,work_table,engine,product_name=None,quantity=None,purchases=None,sales=None):
        self.work_table=work_table
        self.engine=engine
        self.product_name=product_name
        self.quantity=quantity
        self.purchases=purchases
        self.sales=sales

    def retrive_data(self):
        query=text("SELECT * FROM product_And_transactions")
        eng_conn=self.engine.connect()
        fetchObj=eng_conn.execute(query)
        return fetchObj.fetchall()

    def insert_data(self):
        inser= self.work_table.insert().values(product_name=self.product_name,quantity=self.quantity,purchases=self.purchases,sales=self.sales)
        eng_conn=self.engine.connect()
        eng_conn.execute(inser)
        eng_conn.commit()

    def update_data(self,new_product_name,new_quantity,new_purchases,new_sales):
        if new_product_name:
            inser= update(self.work_table).where(self.work_table.c.product_name==self.product_name).values(product_name=new_product_name)
            eng_conn=self.engine.connect()
            eng_conn.execute(inser)
            eng_conn.commit()
        if new_quantity:
            inser= update(self.work_table).where(self.work_table.c.quantity==self.quantity).values(quantity=new_quantity)
            eng_conn=self.engine.connect()
            eng_conn.execute(inser)
            eng_conn.commit()
        if new_purchases:
            inser= update(self.work_table).where(self.work_table.c.purchases==self.purchases).values(purchases=new_purchases)
            eng_conn=self.engine.connect()
            eng_conn.execute(inser)
            eng_conn.commit()
        if new_sales:
            inser= update(self.work_table).where(self.work_table.c.sales==self.sales).values(sales=new_sales)
            eng_conn=self.engine.connect()
            eng_conn.execute(inser)
            eng_conn.commit()
        

    def delete_data(self):
        if self.product_name:
            delet_val= self.work_table.delete().where(self.work_table.c.product_name==self.product_name)
            eng_conn=self.engine.connect()
            eng_conn.execute(delet_val)
            eng_conn.commit()
        if self.quantity:
            delet_val= self.work_table.delete().where(self.work_table.c.quantity==self.quantity)
            eng_conn=self.engine.connect()
            eng_conn.execute(delet_val)
            eng_conn.commit()
        if self.purchases:
            delet_val= self.work_table.delete().where(self.work_table.c.purchases==self.purchases)
            eng_conn=self.engine.connect()
            eng_conn.execute(delet_val)
            eng_conn.commit()
        if self.sales:
            delet_val= self.work_table.delete().where(self.work_table.c.sales==self.sales)
            eng_conn=self.engine.connect()
            eng_conn.execute(delet_val)
            eng_conn.commit()



# if __name__=="__main__":
#     product_name="Bulb"
#     quantity=5
#     purchases=100
#     sales=200

#while calling update_data method just pass the values which you wants update and where.

    # obj=MainDB_class(work_table,engine,product_name,quantity,purchases,sales)
    # print("my data is ",obj.insert_data())


