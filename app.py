from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import Models
import sqlite3
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,MetaData,Table,Insert,Column,Integer,String
import os
from Models import MainDB_class




################## Database creation and Intigration ################
conn= sqlite3.connect('sample.db')
try:
    query="""CREATE TABLE product_And_transactions(product_name STRING,quantity INTEGER,purchases INTEGER,sales INTEGER)"""
    cur=conn.cursor()
    cur.execute(query)
except sqlite3.OperationalError as err:
    print("Already table exist")
cur=conn.cursor()

engine=create_engine('sqlite:///sample.db',echo=True)
meta=MetaData()

work_table=Table("product_And_transactions",meta,
                Column("id",Integer,primary_key=True),
                Column("product_name",String),
                Column("quantity",Integer),
                Column("purchases",Integer),
                Column("sales",Integer)
                )

##########################Flask application #####################

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:////C:\\Users\\DATR2138\\client_environment\\Inventory_management_system\\sample.db"
db=SQLAlchemy(app)




product_name="Bulb"
quantity=5
purchases=50
sales=100


#### just pass new values when updating ####
new_product_name="ball"
new_quantity=3
new_purchases=30
new_sales=90



@app.route("/operations",methods=['GET','POST','PUT','DELETE'])
def operation_vals():
    if request.method=="GET":
        obj=MainDB_class(work_table,engine,product_name,quantity,purchases,sales)
        all_data=obj.retrive_data()
        return all_data

    elif request.method=="POST":
        obj=MainDB_class(work_table,engine,product_name,quantity,purchases,sales)
        obj.insert_data()
        return "The value inserted succussfully to database"

    elif request.method=="PUT":       
        obj=MainDB_class(work_table,engine,new_product_name,new_quantity,new_purchases,new_sales)
        obj.update_data()
        return "The value updated succussfully to database"
    
    elif request.method=="DELETE":
        obj=MainDB_class(work_table,engine,product_name,quantity,purchases,sales)
        obj.delete_data()
        return "The value updated succussfully to database"
    else:
        return "operation_vals function ran"

if __name__=="__main__":
    app.run(debug=True)