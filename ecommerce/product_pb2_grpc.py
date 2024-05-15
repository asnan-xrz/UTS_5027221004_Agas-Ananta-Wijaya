# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import product_pb2 as product__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in product_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProduct = channel.unary_unary(
                '/ecommerce.ProductService/CreateProduct',
                request_serializer=product__pb2.Product.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                _registered_method=True)
        self.GetProduct = channel.unary_unary(
                '/ecommerce.ProductService/GetProduct',
                request_serializer=product__pb2.ProductId.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                _registered_method=True)
        self.UpdateProduct = channel.unary_unary(
                '/ecommerce.ProductService/UpdateProduct',
                request_serializer=product__pb2.Product.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                _registered_method=True)
        self.DeleteProduct = channel.unary_unary(
                '/ecommerce.ProductService/DeleteProduct',
                request_serializer=product__pb2.ProductId.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                _registered_method=True)
        self.ListProducts = channel.unary_unary(
                '/ecommerce.ProductService/ListProducts',
                request_serializer=product__pb2.Empty.SerializeToString,
                response_deserializer=product__pb2.ProductList.FromString,
                _registered_method=True)


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=product__pb2.Product.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=product__pb2.ProductId.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'UpdateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProduct,
                    request_deserializer=product__pb2.Product.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'DeleteProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProduct,
                    request_deserializer=product__pb2.ProductId.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'ListProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProducts,
                    request_deserializer=product__pb2.Empty.FromString,
                    response_serializer=product__pb2.ProductList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecommerce.ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ecommerce.ProductService/CreateProduct',
            product__pb2.Product.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ecommerce.ProductService/GetProduct',
            product__pb2.ProductId.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ecommerce.ProductService/UpdateProduct',
            product__pb2.Product.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ecommerce.ProductService/DeleteProduct',
            product__pb2.ProductId.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ecommerce.ProductService/ListProducts',
            product__pb2.Empty.SerializeToString,
            product__pb2.ProductList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)