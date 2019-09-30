"""

Core of onnxexplorer

"""
import onnxruntime as ort
# import onnx
# from onnx.onnx_ml_pb2 import ModelProto
from .proto.onnx_ml_pb2 import ModelProto, TensorProto, NodeProto
from typing import Optional, cast, Text, IO
from google import protobuf
from colorama import init, Fore, Style, Back
import os
import sys


def load_onnx_model(f, proto):
    s = None
    if hasattr(f, 'read') and callable(cast(IO[bytes], f).read):
        s = cast(IO[bytes], f).read()
    else:
        with open(cast(Text, f), 'rb') as readable:
            s = readable.read()
    decoded = cast(Optional[int], proto.ParseFromString(s))
    if decoded is not None and decoded != len(s):
        raise protobuf.message.DecodeError(
            "Protobuf decoding consumed too few bytes: {} out of {}".format(
                decoded, len(s)))
    return proto



def search_nodes_by_type(model, type_name):
    """
    search all nodes that with Type
    :param model_proto:
    :param type_name:
    :return:
    """
    print(Style.BRIGHT + 'search node by op type: ' + Style.RESET_ALL + Fore.GREEN + type_name + Style.RESET_ALL)
    if isinstance(model, ModelProto):
        graph = model.graph
        i = 0
        for node in graph.node:
            if type_name in node.op_type:
                i += 1
                print(node)
        print(Style.BRIGHT + 'listed all {} {} nodes in detail.\n'.format(i, type_name) + Style.RESET_ALL)


def list_nodes(model):
    """
    print out all nodes
    :param model_proto:
    :return:
    """
    print(Style.BRIGHT + 'start list nodes names:' + Style.RESET_ALL)
    if isinstance(model, ModelProto):
        graph = model.graph
        i = 0
        for node in graph.node:
            i += 1
            print('{}. {}'.format(i, node.name))
        print(Style.BRIGHT + 'listed all {} nodes names.\n'.format(i) + Style.RESET_ALL)



def list_nodes_hl(model):
    print(Style.BRIGHT + 'start list nodes all:' + Style.RESET_ALL)
    if isinstance(model, ModelProto):
        graph = model.graph
        i = 0
        for node in graph.node:
            if node.attribute.raw_data != None:
                node.attribute.raw_data = 'too long ignore it...'
                print(node)
                i += 1
        print(Style.BRIGHT + 'listed all {} nodes in detail.\n'.format(i) + Style.RESET_ALL)


def search_node_by_id(model, node_id):
    """
    print out specific node by ID
    :param model_proto:
    :param node_id:
    :return:
    """
    print(Style.BRIGHT + 'search node by ID: ' + Style.RESET_ALL + Fore.GREEN + node_id + Style.RESET_ALL)
    if isinstance(model, ModelProto):
        graph = model.graph
        i = 0
        for node in graph.node:
            if node_id in node.name:
                i += 1
                print(node)
        print(Style.BRIGHT + 'listed all {} nodes in detail.\n'.format(i) + Style.RESET_ALL)


def summary(model_proto, model_p):
    if isinstance(model_proto, ModelProto):
        print(Fore.WHITE + Style.BRIGHT + 'ONNX model sum on: ' +  Style.RESET_ALL + os.path.basename(model_p))
        print('\n')
        print('-------------------------------------------')
        print('ir version: {}'.format(model_proto.ir_version))
        for opi in model_proto.opset_import:
            print('opset_import: {} {}'.format(opi.version, opi.domain))
        print('producer_name: {}'.format(model_proto.producer_name))
        print('doc_string: {}'.format(model_proto.doc_string))
        print('-------------------------------------------\n')