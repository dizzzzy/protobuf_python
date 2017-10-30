from __future__ import print_function

import grpc

import products_pb2
import products_pb2_grpc

def run():
  ##Protobuff
  channel = grpc.insecure_channel('localhost:50051')
  stub = products_pb2_grpc.RfqStub(channel)
  print("Client sent a request for quote with an id of 1")
  temp = products_pb2.QuoteRequest(product_num=1) #, product_category='education', quantity=4
  response = stub.rfq(temp)
  print("Quote received: \n" + "  price:" + str(response.unit_price) + "\n  price validation period:" + str(response.price_validation_period))



if __name__ == '__main__':
  run()
