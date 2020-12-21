Title: Caffe Tutorial: build, train and predict
Date: 2017-03-30 05:24
Author: mohanad
Category: Academic, Application
Tags: caffe, deep learning, LeNet, MNIST, Neural Networks
Slug: caffe-tutorial-build-train-and-predict
Status: published

Caffe is one of the most popular tools for deep learning, with it you can easily build, train and use deep neural networks and it is considered as the fastest framework as the time of writing this post. The reason why I’m writing this post is because I could not find one article that can answer all of my questions, I had to go back and forth between caffe’s official website, and other blogs in order to get the full picture of how to use Caffe. In this post I’m gonna cover the following points, of how to create a neural network, how can I train it and then use the trained model to predict new samples, I will cover the different approach and highlights the differences between them. Also, I’m gonna cover how to get and use a pre-trained model from Model Zoo. 

In this post, we will implement [LeNet](http://yann.lecun.com/exdb/lenet/) on MNIST dataset, where the LeNet is known for its ability to classify handwritten digits. So let's get started!

I will suppose that you already have Caffe installed on your device or you have an access to remote machine with Caffe installed on it. If you did not install it you can refer to another post that I wrote on [how to install Caffe on a CPU only machine](http://mohanadkaleia.com/install-caffe-on-ubuntu-with-no-gpu/)

The first step toward implementing the model is to get the dataset, [MNIST](https://en.wikipedia.org/wiki/MNIST_database), fortunately, is available online, also the installation script is available with Caffe installation, so we can use it right away.

cd $CAFFE\_ROOT   
./data/mnist/get\_mnist.sh   
./examples/mnist/create\_mnist.sh

note: $CAFFE\_ROOT is the installation path of caffe, in my case it is /home/mohanad/caffe. 

Cool!, we got the training set, now we can move forward to build and train our model. As mentioned before we are going to use LeNet, which nothing but Convolutional Neural Network compromised of **Conv layer → Pooling layer → Conv layer → pool layer → Fully connected network → ReLU function → Fully connected network → Softmax classifier function** 

Build the model
===============

We got the data, and we know the structure of the model we want to build, we are ready to build our model. To build the model Caffe provides an easy way to define the structure of the network layer by layer, using Protocol buffer format, which is a serialization method created by Gogle that represents structured data, in order to generate code or object out of this structure. By defining a protocol text of the network Caffe then can read this structure to train a model. In this section we will see how we can build such a model, 

Before we proceed, lets just see how we can build a layer using Prototxt format, in general each layer defined in the protobuff format has two main sections, the first one is the layer definition, where we define layer name, type, inputs and outputs, the other section is the layer option, where each layer type has different set of options. We can take now the network we are going to implement as a practical example. 

**note: don’t copy and paste from the following protobuffs I will provide the whole network structure at the end of this post, the following layers just to illustrate how to use protobuff in caffe for this example.**

Data layer
----------

Now to read the data we’ve just imported we need a data layer, that read the data source, the following prototxt represent the input layer:

```
:::python
layer {
  name: "mnist"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TRAIN
  }
  transform\_param {
    scale: 0.00390625
  }
  data\_param {
    source: "examples/mnist/mnist\_train\_lmdb"
    batch\_size: 64
    backend: LMDB
  }
}
```

As we can see from the layer definition above, we called the layer as “mnist”, and the type is “data”, here we have two outputs we called the first one as data and the second one as the label, where we will use it later to calculate the loss. 

Still, we did not finish yet, we need to define the options of this layer, since it is data layer then we need to define the source of the data and the type of the data. here the type is [LMDB](https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database), 

The data layer can read different format of data, as a database like LMDB or LEVELDB, from memory or from a file on a disk in HDF5 or image format.

The batch size of the data will be 64 and a scale transformation will be applied on the data. We can note here that a preprocessing operation can be applied on the data, (e.x. scaling, normalization, mean, .., etc). 

Note that this layer only works in the train phase, since the data source is training dataset we only need it when the optimizer is training the model, we can write another data layer that is specified for testing phase and we can assign the test set with it.

Convolutional layer
-------------------

The first layer in the LeNet after the data layer is the convolution layer, the structure of it is represented as follow:
```
:::python
layer {
  name: "conv1"
  type: "Convolution"
  param { lr\_mult: 1 }
  param { lr\_mult: 2 }
  convolution\_param {
    num\_output: 20
    kernel\_size: 5
    stride: 1
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
  bottom: "data"
  top: "conv1"
}
```

In this section, I will discuss only the parametric options since they are different than the previous layer. The convolution\_param define the convolution output size, the kernel size, the stride, also we can define how the weights will be initialized, there are many algorithms can be used to initialize the weights, the one used here is Xavier. Also, we can define how the bias will be initialized. 

The parameter of lr\_mult is the learning rate adjustment, the value of the learning rate is stored in the solver configuration, but this parameter would allow the solver to adjust the learning rate during the training phase, for example when the value of the lr\_mult is equal to 1, then the solver will multiply the learning rate with 1, which means leave it as it is. We notice here we have two lr\_mult parameters, the first one is for weights and the other one for the bias.

Pooling layer 
--------------

In LeNet architecture, a down sampling layer comes right after the convolutional layer, as we can call it Pooling layer, the following protobuf txt represents the pooling layer: 
```
:::python
layer {
  name: "pool1"
  type: "Pooling"
  pooling\_param {
    kernel\_size: 2
    stride: 2
    pool: MAX
  }
  bottom: "conv1"
  top: "pool1"
}
```

In the pooling\_param we define the parameters related to the pooling layer, note that we specified the type of this layer as “Pooling”, as we know in a pooling layer we need to define the kernel size along with the stride, the most common size is 2 with stride of 2, then we need to choose the pooling function, also you can choose one from many available functions (e.g. average, max, .., etc) the most common function to be used is the max function. 

Fully Connected layer
---------------------

The last layer type we need to add into LeNet network is a fully connected layer, where the structure of this layer is represented in the following protobuff txt:

```
:::python
layer {
  name: "ip1"
  type: "InnerProduct"
  param { lr\_mult: 1 }
  param { lr\_mult: 2 }
  inner\_product\_param {
    num\_output: 500
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
  bottom: "pool2"
  top: "ip1"
}
```

Note the type here called as “InnerProduct”, we need to specify the output size of this layer in the inner\_product\_param, the weight and bias initialization is just similar to the ones we did with the convolutional layer, nothing new here so far.![smiling face with open mouth](https://d1fldwwydewvss.cloudfront.net/static/img/ace/emoji/1f603.png "smiling face with open mouth") 

ReLU layer
----------

The activation function we are going to use in this network is RelU, defining such a functions is just straight forward in the protobuff format, like the following: 

```
:::python
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
```

Loss layer
----------

In LeNet and just after creating the fully connected layer we need to define the classifier we are going to use, in our example, we will use softmax classifier, that accepts two inputs, the out of the last FC layer which is the predicted label and the actual labels from the dataset. 

Assemble all layers together in one protobuff file
--------------------------------------------------

GREAT!, now we know how to define all needed layers, the only thing we need to do is to assemble them in one file, to make it easier for you try to write down the layers one by one, like what we need for this architecture. 

Data layer → conv layer → pooling layer → Fully connected layer → ReLU → Fully Connected layer → Loss. Now let's write down all of these layers in a file and make sure the format of the file is “**.prototxt**”:

```
:::python
name: "LeNet"
layer {
  name: "mnist"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TRAIN
  }
  transform\_param {
    scale: 0.00390625
  }
  data\_param {
    source: "examples/mnist/mnist\_train\_lmdb"
    batch\_size: 64
    backend: LMDB
  }
}
layer {
  name: "mnist"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TEST
  }
  transform\_param {
    scale: 0.00390625
  }
  data\_param {
    source: "examples/mnist/mnist\_test\_lmdb"
    batch\_size: 100
    backend: LMDB
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr\_mult: 1
  }
  param {
    lr\_mult: 2
  }
  convolution\_param {
    num\_output: 20
    kernel\_size: 5
    stride: 1
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling\_param {
    pool: MAX
    kernel\_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr\_mult: 1
  }
  param {
    lr\_mult: 2
  }
  convolution\_param {
    num\_output: 50
    kernel\_size: 5
    stride: 1
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling\_param {
    pool: MAX
    kernel\_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr\_mult: 1
  }
  param {
    lr\_mult: 2
  }
  inner\_product\_param {
    num\_output: 500
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr\_mult: 1
  }
  param {
    lr\_mult: 2
  }
  inner\_product\_param {
    num\_output: 10
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
}
layer {
  name: "accuracy"
  type: "Accuracy"
  bottom: "ip2"
  bottom: "label"
  top: "accuracy"
  include {
    phase: TEST
  }
}
layer {
  name: "loss"
  type: "SoftmaxWithLoss"
  bottom: "ip2"
  bottom: "label"
  top: "loss"
}
```

 To draw the previous image, I used a [netscope](http://ethereon.github.io/netscope/quickstart.html) which is a nice tool to draw the neural network architecture from a protobuff. If you find writing the architecture using protobuff format, you are right, it is not straightforward for a beginner, so I can suggest you use a graphical tool that can generate the prototxt for you, try this [http://yanglei.me/gen\_proto/](http://yanglei.me/gen_proto/), not bad huh!

![](https://paper.dropbox.com/ep/redirect/image?url=https%3A%2F%2Fd2mxuefqeaa7sj.cloudfront.net%2Fs_21BC1A9FF46697A08B39A188DB849C9960E7291A1228DF91BE13B61A2A56F2B1_1490758944219_Screenshot%2Bfrom%2B2017-03-28%2B22-42-05.png&hmac=ehT1XoRozAUlxvsasuSjnSb161mGVRR9BrqyqkvNROw%3D)

Train the network
=================

To train the network Caffe offers solver for model optimization that applies forward and backward that updates the weights in order to improve the loss. Caffe provides the following solvers:

*   Stochastic Gradient Descent (type: "SGD"),
*   AdaDelta (type: "AdaDelta"),
*   Adaptive Gradient (type: "AdaGrad"),
*   Adam (type: "Adam"),
*   Nesterov’s Accelerated Gradient (type: "Nesterov") and
*   RMSprop (type: "RMSProp")

For more information about the caffe’s solver please refer to the following page: [http://caffe.berkeleyvision.org/tutorial/solver.html](http://caffe.berkeleyvision.org/tutorial/solver.html)

Now we tell how the solver should train the network by defining a prototxt file, you can create new .prototxt file and name it as lenet\_solver.prototxt, then write the following in it:

```
:::python
\# The train/test net protocol buffer definition
net: "examples/mnist/lenet\_network.prototxt"
# test\_iter specifies how many forward passes the test should carry out.
# In the case of MNIST, we have test batch size 100 and 100 test iterations,
# covering the full 10,000 testing images.
test\_iter: 100
# Carry out testing every 500 training iterations.
test\_interval: 500
# The base learning rate, momentum and the weight decay of the network.
base\_lr: 0.01
momentum: 0.9
weight\_decay: 0.0005
# The learning rate policy
lr\_policy: "inv"
gamma: 0.0001
power: 0.75
# Display every 100 iterations
display: 100
# The maximum number of iterations
max\_iter: 10000
# snapshot intermediate results
snapshot: 5000
snapshot\_prefix: "examples/mnist/lenet"
# solver mode: CPU or GPU
solver\_mode: CPU
type: "Adam"
```

In the prototxt above we can see some parameters, some of them are trivial and some are not, let me explain them here to make it as clear as possible to you:

**base\_lr:** This parameter indicates the base (beginning) learning rate of the network. The value is a real number (floating point).

**lr\_policy:** This parameter indicates how the learning rate should change over time. This value is a quoted string. (Please refer to this page to get the formula of each option [https://github.com/BVLC/caffe/blob/master/src/caffe/proto/caffe.proto#L157-L172](https://github.com/BVLC/caffe/blob/master/src/caffe/proto/caffe.proto#L157-L172)

**gamma**

This parameter indicates how much the learning rate should change every time we reach the next "step." The value is a real number and can be thought of as multiplying the current learning rate by said number to gain a new learning rate.

**max\_iter**

This parameter indicates when the network should stop training. The value is an integer indicate which iteration should be the last.

**momentum**

This parameter indicates how much of the previous weight will be retained in the new calculation. This value is a real fraction.

**weight\_decay**

This parameter indicates the factor of (regularization) penalization of large weights. This value is a often a real fraction.

**solver\_mode**

This parameter indicates which mode will be used in solving the network.

Options include:

1.  CPU
2.  GPU

**snapshot**

This parameter indicates how often caffe should output a model and solverstate. This value is a positive integer.

**snapshot\_prefix:**

This parameter indicates how a snapshot output's model and solverstate's name should be prefixed. This value is a double quoted string.

**net:**

This parameter indicates the location of the network to be trained (path to prototxt). This value is a double quoted string.

**test\_iter**

This parameter indicates how many test iterations should occur per **test\_interval**. This value is a positive integer.

**test\_interval**

This parameter indicates how often the test phase of the network will be executed.

**display**

This parameter indicates how often caffe should output results to the screen. This value is a positive integer and specifies an iteration count.

**type**

This parameter indicates the back propagation algorithm used to train the network. This value is a quoted string.

To see the full list of options you can visit this page: [https://github.com/BVLC/caffe/wiki/Solver-Prototxt](https://github.com/BVLC/caffe/wiki/Solver-Prototxt)

Almost done, almost done, writing such a long post is also not easy so be patient ![smiling face with open mouth](https://d1fldwwydewvss.cloudfront.net/static/img/ace/emoji/1f603.png "smiling face with open mouth") 

Now we wrote all configuration that the solver needs to know how to optimize the network, we can call it now on our network using the following command from the terminal: 

`caffe train -solver lenet_solver.prototxt` 

Note that we did not specify the network file because it is already specified in the solver prototxt file. 

The solver generates two types of file:

*   lenet\_multistep\_10000.caffemodel: weights of the architecture to be used in testing
*   lenet\_multistep\_10000.solverstate: used if training dies (for example, power outage) to resume training from current iteration

Here is a screenshot during the training process from my laptop, it is good to know that I did the training on a non-GPU machine although it is not recommended but for testing or learning purposes it is still very good good option: 

![](https://paper.dropbox.com/ep/redirect/image?url=https%3A%2F%2Fd2mxuefqeaa7sj.cloudfront.net%2Fs_21BC1A9FF46697A08B39A188DB849C9960E7291A1228DF91BE13B61A2A56F2B1_1490671154884_Screenshot%2Bfrom%2B2017-03-27%2B22-17-20.png&hmac=%2B03OyfHbAF72wePUJqpxGhd4I75ApH97PVyxz6t3xFo%3D)

![](https://paper.dropbox.com/ep/redirect/image?url=https%3A%2F%2Fd2mxuefqeaa7sj.cloudfront.net%2Fs_21BC1A9FF46697A08B39A188DB849C9960E7291A1228DF91BE13B61A2A56F2B1_1490759287932_Screenshot%2Bfrom%2B2017-03-25%2B18-43-40.png&hmac=YYmmx0ECBt4q8STaryWyiin8wD3ekwZ8tWMyE5dMIrU%3D&width=1490)

Notice how we got a feedback from the solver each 100 iterations as we specified in the solver prototxt file. 

It would be good to plot the accuracy over iteration, to do that you only need to run the following command after your model is trained:

`python ~/caffe/tools/extra/parse_log.py my_model.log .gnuplot -persist gnuplot_commands`

where mu\_mode.log is generated after finish training your model.

Predict and classify new samples
================================

Now after the solver finish training we will have a trained model that can be used to predict the class of new samples, and here is one of the questions I got when I was studying Caffe, how to use the model? can I use it directly from the command line as we did in the training phase, or I need to write C++ code for that, 

The best answer I was able to get is to use Python interface to predict the class of any new sample. In this section I will show how to use Caffe-python interface to predict new samples, in the caffe root path create new python file, you can name it as predict.py and write the following in it:

```
:::python
import numpy as np
import matplotlib.pyplot as plt
import sys
import caffe
import cv2


# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL\_FILE = 'examples/mnist/deploy.prototxt'
PRETRAINED = 'examples/mnist/lenet\_iter\_1000.caffemodel'

# load the model
caffe.set\_mode\_cpu()

net = caffe.Classifier(MODEL\_FILE, PRETRAINED, caffe.TEST, raw\_scale=255)

print "successfully loaded classifier"

IMAGE\_FILE = 'examples/mnist/9\_28x28.png'
img = cv2.imread(IMAGE\_FILE,0)
if img.shape != \[28,28\]:
        img2 = cv2.resize(img,(28,28))
        img = img2.reshape(28,28,-1);
else:
        img = img.reshape(28,28,-1);

img = 1.0 - img/255.0

# predict takes any number of images,
# and formats them for the Caffe net automatically
res = net.forward(data = np.asarray(\[img.transpose(2,0,1)\]))
pred = res.values()\[0\]
print pred.argmax()
```

# This code has been copied and modified from the following link:
# https://github.com/9crk/caffe-mnist-test/blob/master/mnist\_test.py

Notice in the code above we used **deploy.prototxt** for the network architecture, which is different than the one we used in training phase. The reason, we slightly modified the architecture by removing the data layer that was taking the training set as a resource, we don’t need it anymore, also we don’t need the accuracy nor the loss functions since they depend on the training labels. So now let's modify the prototxt file:

1.  Copy the network prototxt file and name it as **deploy.prototxt**, 
2.  remove “data” layers, 
3.  remove “accuracy” and “loss” layers from the end of the file
4.  Create input layer in the first of the file, 

```
:::python
layer {
    name: "data"
    type: "Input"
    top: "data"
    input\_param { shape: { dim: 1 dim: 1 dim: 28 dim: 28 } }
}
```

5.  We still need a classifier in the end of our network, so create the following layer at the end of the file:

```
:::python
layer {
  name: "loss"
  type: "Softmax"
  bottom: "ip2"
  top: "loss"
}
```

The whole structure is represented as follow:

```
:::python
name: "LeNet"
layer {
    name: "data"
    type: "Input"
    top: "data"
    input\_param { shape: { dim: 1 dim: 1 dim: 28 dim: 28 } }
}

layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr\_mult: 1
  }
  param {
    lr\_mult: 2
  }
  convolution\_param {
    num\_output: 20
    kernel\_size: 5
    stride: 1
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling\_param {
    pool: MAX
    kernel\_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr\_mult: 1
  }
  param {
    lr\_mult: 2
  }
  convolution\_param {
    num\_output: 50
    kernel\_size: 5
    stride: 1
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling\_param {
    pool: MAX
    kernel\_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr\_mult: 1
  }
  param {
    lr\_mult: 2
  }
  inner\_product\_param {
    num\_output: 500
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr\_mult: 1
  }
  param {
    lr\_mult: 2
  }
  inner\_product\_param {
    num\_output: 10
    weight\_filler {
      type: "xavier"
    }
    bias\_filler {
      type: "constant"
    }
  }
}

layer {
  name: "loss"
  type: "Softmax"
  bottom: "ip2"
  top: "loss"
}
```

Now all you need to do is to run the python code you already wrote, make sure to have a sample image to test with on the defined path in the code, how to run it?

python predict.py

If everything went fine you should get the prediction result: ![](https://paper.dropbox.com/ep/redirect/image?url=https%3A%2F%2Fd2mxuefqeaa7sj.cloudfront.net%2Fs_21BC1A9FF46697A08B39A188DB849C9960E7291A1228DF91BE13B61A2A56F2B1_1490758253115_Screenshot%2Bfrom%2B2017-03-28%2B22-30-39.png&hmac=pug0LVbrx8T3%2FO%2FO%2BD8HhwoAY9wSbCZ62KW45I8l4yg%3D) I tested with this image, if you are lazy to get new one ![smiling face with open mouth](https://d1fldwwydewvss.cloudfront.net/static/img/ace/emoji/1f603.png "smiling face with open mouth")  ![](https://paper.dropbox.com/ep/redirect/image?url=https%3A%2F%2Fd2mxuefqeaa7sj.cloudfront.net%2Fs_21BC1A9FF46697A08B39A188DB849C9960E7291A1228DF91BE13B61A2A56F2B1_1490732252179_10_28x28.png&hmac=Xmw8e3YEtEnO90KdUmIAoLcfgwezBdprXETP8KNH9PE%3D)

\======================================================

This is the end of this tutorial, so tired of writing this long post, I really wish that someone would get benefit out of it, please if you have any question don’t hesitate to leave a comment or send an email to me, happy to help anyone

I would not be able to make this post without these great resources:

\[1\] [https://shadowthink.com/blog/tech/2016/08/28/Caffe-MNIST-tutorial](https://shadowthink.com/blog/tech/2016/08/28/Caffe-MNIST-tutorial)

\[2\] [http://caffe.berkeleyvision.org/gathered/examples/mnist.html](http://caffe.berkeleyvision.org/gathered/examples/mnist.html)

\[3\] [http://shengshuyang.github.io/A-step-by-step-guide-to-Caffe.html](http://shengshuyang.github.io/A-step-by-step-guide-to-Caffe.html)

\[4\] [https://software.intel.com/en-us/articles/training-and-deploying-deep-learning-networks-with-caffe-optimized-for-intel-architecture#Training](https://software.intel.com/en-us/articles/training-and-deploying-deep-learning-networks-with-caffe-optimized-for-intel-architecture#Training)

\[5\] [https://github.com/BVLC/caffe/wiki/Solver-Prototxt](https://github.com/BVLC/caffe/wiki/Solver-Prototxt)

\[6\] [http://adilmoujahid.com/posts/2016/06/introduction-deep-learning-python-caffe/](http://adilmoujahid.com/posts/2016/06/introduction-deep-learning-python-caffe/)

\[7\] [http://stackoverflow.com/questions/33765029/caffe-how-to-predict-from-a-pretrained-net](http://stackoverflow.com/questions/33765029/caffe-how-to-predict-from-a-pretrained-net)

\[8\] [https://github.com/9crk/caffe-mnist-test](https://github.com/9crk/caffe-mnist-test)

\[9\] [https://github.com/BVLC/caffe/wiki/Using-a-Trained-Network:-Deploy](https://github.com/BVLC/caffe/wiki/Using-a-Trained-Network:-Deploy)

\[10\] [http://mohanadkaleia.com/install-caffe-on-ubuntu-with-no-gpu/](http://mohanadkaleia.com/install-caffe-on-ubuntu-with-no-gpu/)

\[11\] [http://nbviewer.jupyter.org/github/BVLC/caffe/blob/master/examples/01-learning-lenet.ipynb](http://nbviewer.jupyter.org/github/BVLC/caffe/blob/master/examples/01-learning-lenet.ipynb)

\[12\][https://docs.google.com/presentation/d/1UeKXVgRvvxg9OUdh\_UiC5G71UMscNPlvArsWER41PsU/edit#slide=id.gc2fcdcce7\_216\_278](https://docs.google.com/presentation/d/1UeKXVgRvvxg9OUdh_UiC5G71UMscNPlvArsWER41PsU/edit#slide=id.gc2fcdcce7_216_278)