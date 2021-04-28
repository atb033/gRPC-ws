# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from generated import msg_pb2 as msg__pb2


class DataBrokerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DataBroker = channel.unary_stream(
                '/DataBroker/DataBroker',
                request_serializer=msg__pb2.Empty.SerializeToString,
                response_deserializer=msg__pb2.Features.FromString,
                )


class DataBrokerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DataBroker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataBrokerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DataBroker': grpc.unary_stream_rpc_method_handler(
                    servicer.DataBroker,
                    request_deserializer=msg__pb2.Empty.FromString,
                    response_serializer=msg__pb2.Features.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataBroker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataBroker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DataBroker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/DataBroker/DataBroker',
            msg__pb2.Empty.SerializeToString,
            msg__pb2.Features.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
