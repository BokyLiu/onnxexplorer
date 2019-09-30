# ONNXExplorer

**code under construction, full functionality will be ready soon**

**ONNX 浏览器** is an easy way to explore your onnx model. You can simply do these function in a onnx model very quickly:

```
usage: onnxexp <command> [<args>]

The most commonly used onnxexp commands are:
   ls          ls all model nodes
   search      search and print out certain commands
   summary     print out model summary

i.e.:
onnxexp model.onnx search -t 'Slice'
onnxexp model.onnx search -n '342654'
onnxexp model.onnx ls -hl
onnxexp model.onnx ls
```



Here are some experiments on `resnet50.onnx` model:

```
$ onnxexp ../onnx_deploy/models/retinaface_mbv2_sim.onnx search -t 'Conv' 
Exploring on onnx model: ../onnx_deploy/models/retinaface_mbv2_sim.onnx
search node by ID: Conv
input: "input.1"
input: "531"
input: "533"
output: "301"
op_type: "Conv"
attribute {
  name: "dilations"
  ints: 1
  ints: 1
  type: INTS
}
attribute {
  name: "group"
  i: 1
  type: INT
}
attribute {
  name: "kernel_shape"
  ints: 3
  ints: 3
  type: INTS
}
attribute {
  name: "pads"
  ints: 1
  ints: 1
  ints: 1
  ints: 1
  type: INTS
}
attribute {
  name: "strides"
  ints: 2
  ints: 2
  type: INTS
}

```

function to be add:

- [ ] List all op type used in this model;
- [ ] Estimate on this model, whether it can optimize or can convert to TensorRT engine;



## Update

- **2019.09.30**: First released this package;



## Install

to install *onnxexplorer*, you can do:

```
sudo pip3 install onnxexplorer
```

Or if pip not available:

```
sudo python3 setup.py install
```



## Copyright

All right reserved by Fagang Jin. Codes released under Apache License.