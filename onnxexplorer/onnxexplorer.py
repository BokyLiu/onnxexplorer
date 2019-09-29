"""

This script provides
various exploration on onnx model
such as those operations:

- summary:
    this command will summarize model info mation such as:
    1. model opset version;
    2. if check pass;
    3. whether can be simplifiered or not;
    4. inputs node and outputs node;
    5. all nodes number;
    6. Initializers tensornumber and their index;

- search:
    1. search all nodes by OpType;
    2. search node by node name (ID);

- list:
    1. print out all nodes id
    2. list -hl will print all nodes and it's attribute

"""
import os
import sys
import argparse
import onnxruntime as ort
# import onnx
# from onnx.onnx_ml_pb2 import ModelProto
from proto.onnx_ml_pb2 import ModelProto, TensorProto, NodeProto
from typing import Optional, cast, Text, IO
from google import protobuf
from colorama import init, Fore, Style, Back
init()


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



def search_nodes_by_type(model_proto, type_name):
    """
    search all nodes that with Type
    :param model_proto:
    :param type_name:
    :return:
    """
    pass


def list_nodes(model_proto):
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



def list_nodes_hl(model_proto):
    print(Style.BRIGHT + 'start list nodes all:' + Style.RESET_ALL)
    if isinstance(model, ModelProto):
        graph = model.graph
        i = 0
        for node in graph.node:
            print(node)
            i += 1
        print(Style.BRIGHT + 'listed all {} nodes in detail.\n'.format(i) + Style.RESET_ALL)


def search_node_by_id(model_proto, node_id):
    """
    print out specific node by ID
    :param model_proto:
    :param node_id:
    :return:
    """
    pass


def summary(model_proto, model_p):
    if isinstance(model, ModelProto):
        print(Fore.WHITE + Style.BRIGHT + 'ONNX model sum on: ' +  Style.RESET_ALL + os.path.basename(model_p))
        print('\n')
        print('-------------------------------------------')
        print('ir version: {}'.format(model.ir_version))
        for opi in model.opset_import:
            print('opset_import: {} {}'.format(opi.version, opi.domain))
        print('producer_name: {}'.format(model.producer_name))
        print('doc_string: {}'.format(model.doc_string))
        print('-------------------------------------------\n')


if __name__ == '__main__':
    model_p = sys.argv[1]
    model = load_onnx_model(model_p, ModelProto())
    summary(model, model_p)
    list_nodes(model)
    print(Fore.GREEN + "Done!")
