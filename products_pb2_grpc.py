# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import products_pb2 as products__pb2


class RfqStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.rfq = channel.unary_unary(
        '/products.Rfq/rfq',
        request_serializer=products__pb2.QuoteRequest.SerializeToString,
        response_deserializer=products__pb2.QuoteReply.FromString,
        )


class RfqServicer(object):
  """The greeting service definition.
  """

  def rfq(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RfqServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'rfq': grpc.unary_unary_rpc_method_handler(
          servicer.rfq,
          request_deserializer=products__pb2.QuoteRequest.FromString,
          response_serializer=products__pb2.QuoteReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'products.Rfq', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
