import json

import products_pb2


def read_products_database():
  """Reads the route guide database.

  Returns:
    The full contents of the route guide database as a sequence of
      route_guide_pb2.Features.
  """
  product_list = []
  with open("products.json") as product_db_file:
    for item in json.load(product_db_file):
      print(item)
      product = products_pb2.Product(
      product_num=item["_id"],
      product_category=item["product category"],
      quantity=item["quantity"],
      price_validation_period=item["price_valid"],
      unit_price=item['unit_price'])
      product_list.append(product)
  return product_list

def get_json_database():
  json_product_list = []
  with open("products.json") as product_db_file:
    json_product_list = json.load(product_db_file)
  return json_product_list




# message Product {
#   int32 product_num = 1;
#   string product_category = 2;
#   int32 quantity = 3;
#   string price_validation_period = 4;
# }