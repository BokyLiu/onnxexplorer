# ONNXExplorer

**code under construction, full functionality will be ready soon**

*ONNX 浏览器** is an easy way to explore your onnx model. You can simply do these function in a onnx model very quickly:

- `onnxexplorer model.onnx -ls`:  list all nodes inside onnx model;
- `onnxexplorer model.onnx `: this will gives u a quick onnx model summary;
- `onnxexplorer model.onnx -s '123424'`: search and print out a single node index by name;

Here are some experiments on `resnet50.onnx` model:

```
ONNX model sum on: model.onnx


-------------------------------------------
ir version: 3
opset_import: 9 
producer_name: onnx-caffe2
doc_string: 
-------------------------------------------

start list nodes all:
input: "gpu_0/data_0"
input: "gpu_0/conv1_w_0"
output: "gpu_0/conv1_1"
name: ""
op_type: "Conv"
attribute {
  name: "pads"
  ints: 3
  ints: 3
  ints: 3
  ints: 3
  type: INTS
}
attribute {
  name: "kernel_shape"
  ints: 7
  ints: 7
  type: INTS
}
attribute {
  name: "strides"
  ints: 2
  ints: 2
  type: INTS
}

.....
input: "gpu_0/pred_1"
output: "gpu_0/softmax_1"
name: ""
op_type: "Softmax"

listed all 176 nodes in detail.

Done!
```



## Install

to install *onnxexplorer*, you can do:

```
sudo pip3 install onnxexplorer
```



## Copyright

All right reserved by Fagang Jin. Codes released under Apache License.