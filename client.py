from __future__ import print_function

import grpc

import products_pb2
import products_pb2_grpc
import requests

def run():
  ##Protobuff
  channel = grpc.insecure_channel('localhost:50051')
  stub = products_pb2_grpc.RfqStub(channel)
  print("Client sent a request for quote with an id of 1")
  temp = products_pb2.QuoteRequest(product_num=1) #, product_category='education', quantity=4
  response = stub.rfq(temp)
  print("Quote received: \n" + "  price:" + str(response.unit_price) + "\n  price validation period:" + str(response.price_validation_period))

  ##JSON
  post_data = {'product_num': '1'}
  # POST some form-encoded data:
  print('json')
  post_response = requests.post(url='localhost:50051/rfq', data=post_data)


if __name__ == '__main__':
  run()

  # int32  product_num = 1;
  # string  product_category = 2;
  # int32  quantity = 3;
  # string  price_validation_period = 4;