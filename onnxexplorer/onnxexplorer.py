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
import onnx
# import onnx
# from onnx.onnx_ml_pb2 import ModelProto
from .proto.onnx_ml_pb2 import ModelProto, TensorProto, NodeProto
from typing import Optional, cast, Text, IO
from google import protobuf
from colorama import init, Fore, Style, Back
from .core import *
init()


class ONNXExplorer(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='ONNX Explorer',
            usage='''onnxexp <command> [<args>]

The most commonly used onnxexp commands are:
   ls          ls all model nodes
   search      search and print out certain commands
   summary     print out model summary

i.e.:
onnxexp model.onnx search -t 'Slice'
onnxexp model.onnx search -n '342654'
onnxexp model.onnx ls -hl
onnxexp model.onnx ls
''')
        parser.add_argument('model', help='model path')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:3])
        self.model_path = args.model
        if args.model != None and os.path.exists(args.model):
            print(Style.BRIGHT + 'Exploring on onnx model: ' +
                  Style.RESET_ALL + Fore.GREEN + self.model_path + Style.RESET_ALL)
            # self.model_proto = load_onnx_model(self.model_path, ModelProto())
            self.model_proto = onnx.load(self.model_path)
            if not hasattr(self, args.command):
                # summary
                print('unrecognized command.')
                exit(1)
            # use dispatch pattern to invoke method with same name
            getattr(self, args.command)()
        else:
            parser.print_help()
            print('{} does not exist or you should provide model path at first arg.'.format(
                args.model))

    def ls(self):
        parser = argparse.ArgumentParser(
            description='ls at any level about the model.')
        # prefixing the argument with -- means it's optional
        parser.add_argument('-hl', action='store_true')
        args = parser.parse_args(sys.argv[3:])
        print('Running onnxexp ls, hl=%s' % args.hl)
        if args.hl:
            list_nodes_hl(self.model_proto)
        else:
            list_nodes(self.model_proto)

    def search(self):
        parser = argparse.ArgumentParser(
            description='Download objects and refs from another repository')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('--name', '-n', help='name of to search node')
        parser.add_argument('--type', '-t', help='type of to search node')
        args = parser.parse_args(sys.argv[3:])
        if args.name != None:
            search_node_by_id(self.model_proto, args.name)
        elif args.type != None:
            search_nodes_by_type(self.model_proto, args.type)
        else:
            print('search should provide type name or id to search.')

    def summary(self):
        summary(self.model_proto, self.model_path)


def main():
    ONNXExplorer()


if __name__ == '__main__':
    main()