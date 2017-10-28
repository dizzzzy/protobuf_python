from concurrent import futures
import time
import json
import grpc

import products_pb2
import products_pb2_grpc
import dbReader


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# setup database connection

def get_product(product_db, product_id):
  """Returns Feature at given location or None."""
  print('hello')
  # return 'hello'
  for product in product_db:
    if product.product_num == product_id:
      return product
  return None


class Server(products_pb2_grpc.RfqServicer):

  def __init__(self):
    self.db = dbReader.read_products_database()

  def rfq(self, request, context):
    #get product list
    #find product with wtv was given (request)
    temp = request.product_num
    print(temp)
    temp2 = get_product(self.db, request.product_num)
    print('temp2')
    print(temp2)
    reply = products_pb2.QuoteReply(unit_price=temp2.unit_price, price_validation_period=temp2.price_validation_period)
    return reply

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  products_pb2_grpc.add_RfqServicer_to_server(Server(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
