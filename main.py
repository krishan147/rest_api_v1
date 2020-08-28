import pandas as pd
import requests
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import codecs
from codecs import open
import sqlite3
import json

app = Flask(__name__)
api = Api(app)

json_path = 'raw_data.json'
with open(json_path) as f:
  json_data = json.load(f)

class Products(Resource):

    # def get(self, sku, name, qty, price):
    def get(self, function, sku):

        if function == "sku_search":
            for data in json_data:
                if data['sku'] == int(sku):
                    return data
        if function == "availability":
            temp_list = []

            for data in json_data:
                if data["qty"] > 0:
                    temp_list.append(data)
            return temp_list

        if function == "sold_out":
            pass

        # return {"sku": sku, "name": name, "qty": qty, "price": price}


    def put(self, sku, name, qty, price):

        add = {"sku": sku, "name": name, "qty": qty, "price": price}
        return "added: "

    def delete(self):
        pass

    def post(self):
        pass

# api.add_resource(Products, "/products/<int:sku>/<string:name>/<int:qty>/<int:price>")
# api.add_resource(Products, "/products/<string:function>/<int:sku>")
# api.add_resource(Products, "/availability/")

if __name__ == "__main__":
    app.run(debug=True)