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
            if product['_id'] == int(product_num) and product['product category'] == product_category:
                if product['quantity'] > int(quantity):
                    return jsonify({'price': product['unit_price'], 'price validation period': product['price_valid']})
                else:
                    return jsonify({'message': 'Cannot supply that quantity!'})
        return jsonify({'message': 'Cannot find product!'})
        # print(product_list)
        # return jsonify(product_list)


api.add_resource(Rfq, '/rfq/<rfq_id>&<acc_id>&<product_num>&<product_category>&<quantity>')

if __name__ == '__main__':
    app.run(port='5002')

