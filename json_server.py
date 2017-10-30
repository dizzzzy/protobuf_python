# build a running REST API using
# python
# Flask web framework
# Flask Restful extension
# SQLite3
# SQLAlchemy

# prepare the data
# http://www.sqlitetutorial.net/sqlite-sample-database/ download chinook.db
# $ virtualenv venv
# $ source venv/bin/activate
# $ pip install flask flask-jsonpify flask-sqlalchemy flask-restful
# $ pip freeze

# connect to the database
# sqlite3 chinook.db

# run this server.py code

# http://127.0.0.1:5002/employees
# http://127.0.0.1:5002/tracks
# http://127.0.0.1:5002/employees/8


from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify
import dbReader
app = Flask(__name__)
api = Api(app)


class Rfq(Resource):
    def get(self, rfq_id, acc_id, product_num, product_category, quantity):
        product_list = dbReader.get_json_database()
        print(product_num)
        for product in product_list:
            if product['_id'] == int(product_num):
                print('found it')
                return jsonify(product)
        return jsonify(None)
        # print(product_list)
        # return jsonify(product_list)


api.add_resource(Rfq, '/rfq/<rfq_id>&<acc_id>&<product_num>&<product_category>&<quantity>')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')

    # {
    #     "_id": 1,
    #     "product category": "construction",
    #     "quantity": 43,
    #     "price_valid": "27/09/2018",
    #     "unit_price": 54.55
    # }, {
