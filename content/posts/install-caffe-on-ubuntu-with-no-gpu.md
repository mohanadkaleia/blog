Title: Install Caffe on Ubuntu with no GPU
Date: 2017-03-24 04:30
Author: mohanad
Category: Academic, Application, GNULinux, howto
Tags: caffe, CPU, no-GPU, pycaffe
Slug: install-caffe-on-ubuntu-with-no-gpu
Status: published

[If you are reading this post then for sure you know what is Caffe and most probably you want to install it on your machine so I don’t want to speak about what is Caffe and how to use it, this post is just to explain how to install it without having a hard time]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [—]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-mdash}[ hopefully. Okay, the installation of Caffe was not straight forward to me, I ran into several problems, first my system was not clean, I had a lot of broken packages that drove me crazy, until I decided eventually to install Caffe on a clean Ubuntu system in a virtual machine without GPU]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [—]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-mdash}[ not the best option but for testing and get hands dirty it is okay. I need to mention that my operating system is Ubuntu 16.04.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

<div>

[1. Install Opencv]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#install-opencv usually-unique-id="633371284244845"}
=================================================================================================================================================================================

</div>

<div>

[Caffe depends on the image processing library opencv, so before installing Caffe we need to install opencv, the installation of it is kind of straight forward and it does not take a lot of time just follow the following official instruction and come back when you done:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

[<http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html>]{.attrlink .url .author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .url}

</div>

<div>

</div>

<div>

<div>

[2. Install Prerequisites]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#install-prerequisites usually-unique-id="266282231223534"}
========================================================================================================================================================================================

</div>

<div>

[Caffe depends on the following packages, you need to install them before installing Caffe, you should not get errors while installing these packages,]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}[I got a lot of broken dependencies while installing them until I moved to fresh installed Ubuntu system): ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

</div>

<div>

``` {.prettyprint}
sudo apt-get install -y --no-install-recommends libboost-all-dev

sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev libgflags-dev libgoogle-glog-dev liblmdb-dev protobuf-compiler

sudo apt-get install libopenblas-dev

sudo apt-get install libatlas-base-dev
```

</div>

<div>

<div>

[3. Clone Caffe]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#clone-caffe usually-unique-id="372750367213554"}
==============================================================================================================================================================================

</div>

<div>

[Cool, now we need to download and install Caffe, unfortinatly we need to pull it from its repository and compile it from its source code, lets first pull it into a directory, from the terminal change the directory to the one you need to install Caffe in and run the following:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

``` {.prettyprint}
git clone https://github.com/BVLC/caffe
cd caffe
cp Makefile.config.example Makefile.config
```

<div>

<div>

[4. Install python packages]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#install-python-packages usually-unique-id="170057383149123"}
==========================================================================================================================================================================================

</div>

``` {.prettyprint}
sudo apt-get install python-pip python-dev build-essential

sudo pip install scikit-image protobuf
cd python
for req in $(cat requirements.txt); do sudo pip install $req; done
```

<div>

<div>

[5. Change the configuration]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#change-the-configuration usually-unique-id="094120785564284"}
===========================================================================================================================================================================================

</div>

<div>

[Since we are working on a CPU-only environment, we have to tell Caffe that we don’t have GPU, we can do that from Makefile.config file, also we need to tell Caffe which opencv we are working on]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}[on the time of writing this post I installed opencv 3.2 which is the latest), let's set our configuration then:  ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

``` {.prettyprint}
cd ..
sudo gedit Makefile.config
```

<div>

[Now a text file of the configuration is opened, uncomment the]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [“]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-ldquo}[CPU\_ONLY ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[:]{.autolink .author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[= 1” and uncomment OPENCV\_VERSION as follow:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

``` {.prettyprint}
# CPU-only switch (uncomment to build without GPU support).
CPU_ONLY := 1
...
# Uncomment if you're using OpenCV 3
OPENCV_VERSION := 3
```

<div>

[Also we need to include hdf5 library in the INCLUDE\_DIRS variable to avoid future problems, so modify INCLUDE\_DIRS variable as follow]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}[believe me just do that to make your life easier ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[):]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

</div>

</div>

</div>

``` {.prettyprint}
# add some directory to the include director variable
--- INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
+++ INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/
```

<div>

<div>

[6. Modify the Makefile]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#modify-the-makefile usually-unique-id="779849528280479"}
======================================================================================================================================================================================

</div>

<div>

[Now we need to modify the Makefile as well, open it as follow:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

``` {.prettyprint}
sudo gedit Makefile
```

</div>

<div>

[Modify the library to add hdf5 headers path]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

``` {.prettyprint}
--- LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5
+++ LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial
```

</div>

<div>

<div>

[7. Solve problems even before they happen]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#solve-problems-even-before-they-happen usually-unique-id="703727469307917"}
=========================================================================================================================================================================================================

</div>

<div>

[If you jump immediately to compile Caffe you would get compilation errors about hdf5 library because the installed hdf5 has an extension of the version number, so we need to create a link to that library that does not have an extension, to do so create a link as follow:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

``` {.prettyprint}
sudo ln -s /usr/lib/x86_64-linux-gnu/libhdf5_serial.so.10.1.0 /usr/lib/x86_64-linux-gnu/libhdf5.so
sudo ln -s /usr/lib/x86_64-linux-gnu/libhdf5_serial_hl.so.10.0.2 /usr/lib/x86_64-linux-gnu/libhdf5_hl.so
```

<div>

</div>

<div>

[Note that in my case the version number libhdf5\_serial.so is 10.1.0 and 10.0.2 for the libhdf5\_serial\_hl, just pay attention that you have same version, otherwise just change it to the version you have]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

</div>

<div>

<div>

[8. Compile the Caffe]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#compile-the-caffe usually-unique-id="646450042404744"}
====================================================================================================================================================================================

</div>

<div>

[Okay, finally we can compile Caffe package we need make and test the compilation as follow:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

``` {.prettyprint}
make all
make test
make runtest
```

[If everything went fine hopefully the compilation process you should get similar results:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

![](https://paper.dropbox.com/ep/redirect/image?url=https%3A%2F%2Fd2mxuefqeaa7sj.cloudfront.net%2Fs_8A2A77A358E3169DD92D4304A9B14ED189F4CD5A9C9406CE34E5618566268596_1490317333764_Screenshot%2Bfrom%2B2017-03-21%2B14-27-14.png&hmac=w4gdIE3nip957cC9I2z9Obx29vg1S4UFjHELawahkYo%3D&width=1490)

<div>

[9. Compile Caffe-Python Interface]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#compile-caffe-python-interface usually-unique-id="533031381001008"}
=================================================================================================================================================================================================

</div>

<div>

[Since Caffe support Python so we will install pycaffe]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}[a python interface with Caffe), as follow:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

``` {.prettyprint}
make pycaffe
echo export PYTHONPATH=/path/to/caffe/python:$PYTHONPATH >> ~/.bashrc
source ~/.bashrc
```

<div>

<div>

[10. Try python caffe module]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z style="color: #007a8c;"} {#try-python-caffe-module usually-unique-id="793391583102605"}
===========================================================================================================================================================================================

</div>

<div>

[Now as a final step, just make sure that your pycaffe is working by importing caffe module into python, you can test that using python console as follow:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

``` {.prettyprint}
python
>>>import caffe
```

<div>

<div>

[Does it work with you? then congratulations!, if not, please leave a comment so I can help you with that.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

</div>

<div>

[Note I used multiple references and websites that helped me to do the installation, here is the complete list that can help you as well:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

1.  <http://caffe.berkeleyvision.org/>
2.  <http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html>
3.  <https://chunml.github.io/ChunML.github.io/project/Installing-Caffe-CPU-Only/>
4.  <https://sandeeppalakkal.wordpress.com/2016/07/09/installation-of-caffe-on-cpu-only-without-gpu/>

 

</div>

</div>

</div>

</div>
