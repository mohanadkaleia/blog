Title: Install Caffe on Ubuntu with no GPU
Date: 2017-03-24 04:30
Author: mohanad
Category: Academic, Application, GNULinux, howto
Tags: caffe, CPU, no-GPU, pycaffe
Slug: install-caffe-on-ubuntu-with-no-gpu
Status: published

If you are reading this post then for sure you know what is Caffe and most probably you want to install it on your machine so I don’t want to speak about what is Caffe and how to use it, this post is just to explain how to install it without having a hard time [—]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-mdash} hopefully. Okay, the installation of Caffe was not straight forward to me, I ran into several problems, first my system was not clean, I had a lot of broken packages that drove me crazy, until I decided eventually to install Caffe on a clean Ubuntu system in a virtual machine without GPU [—]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-mdash} not the best option but for testing and get hands dirty it is okay. I need to mention that my operating system is Ubuntu 16.04.


1. Install Opencv
=================================================================================================================================================================================



Caffe depends on the image processing library opencv, so before installing Caffe we need to install opencv, the installation of it is kind of straight forward and it does not take a lot of time just follow the following official instruction and come back when you done:



[<http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html>]{.attrlink .url .author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .url}






2. Install Prerequisites
========================================================================================================================================================================================



Caffe depends on the following packages, you need to install them before installing Caffe, you should not get errors while installing these packages, [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}I got a lot of broken dependencies while installing them until I moved to fresh installed Ubuntu system): 




``` {.prettyprint}
sudo apt-get install -y --no-install-recommends libboost-all-dev

sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev libgflags-dev libgoogle-glog-dev liblmdb-dev protobuf-compiler

sudo apt-get install libopenblas-dev

sudo apt-get install libatlas-base-dev
```




3. Clone Caffe
==============================================================================================================================================================================



Cool, now we need to download and install Caffe, unfortinatly we need to pull it from its repository and compile it from its source code, lets first pull it into a directory, from the terminal change the directory to the one you need to install Caffe in and run the following:


``` {.prettyprint}
git clone https://github.com/BVLC/caffe
cd caffe
cp Makefile.config.example Makefile.config
```



4. Install python packages
==========================================================================================================================================================================================


``` {.prettyprint}
sudo apt-get install python-pip python-dev build-essential

sudo pip install scikit-image protobuf
cd python
for req in $(cat requirements.txt); do sudo pip install $req; done
```



5. Change the configuration
===========================================================================================================================================================================================



Since we are working on a CPU-only environment, we have to tell Caffe that we don’t have GPU, we can do that from Makefile.config file, also we need to tell Caffe which opencv we are working on [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}on the time of writing this post I installed opencv 3.2 which is the latest), let's set our configuration then:  


``` {.prettyprint}
cd ..
sudo gedit Makefile.config
```


Now a text file of the configuration is opened, uncomment the [“]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-ldquo}CPU\_ONLY [:]{.autolink .author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}= 1” and uncomment OPENCV\_VERSION as follow:


``` {.prettyprint}
# CPU-only switch (uncomment to build without GPU support).
CPU_ONLY := 1
...
# Uncomment if you're using OpenCV 3
OPENCV_VERSION := 3
```


Also we need to include hdf5 library in the INCLUDE\_DIRS variable to avoid future problems, so modify INCLUDE\_DIRS variable as follow [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}believe me just do that to make your life easier ):





``` {.prettyprint}
# add some directory to the include director variable
--- INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
+++ INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/
```



6. Modify the Makefile
======================================================================================================================================================================================



Now we need to modify the Makefile as well, open it as follow:



``` {.prettyprint}
sudo gedit Makefile
```



Modify the library to add hdf5 headers path


``` {.prettyprint}
--- LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5
+++ LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial
```




7. Solve problems even before they happen
=========================================================================================================================================================================================================



If you jump immediately to compile Caffe you would get compilation errors about hdf5 library because the installed hdf5 has an extension of the version number, so we need to create a link to that library that does not have an extension, to do so create a link as follow:


``` {.prettyprint}
sudo ln -s /usr/lib/x86_64-linux-gnu/libhdf5_serial.so.10.1.0 /usr/lib/x86_64-linux-gnu/libhdf5.so
sudo ln -s /usr/lib/x86_64-linux-gnu/libhdf5_serial_hl.so.10.0.2 /usr/lib/x86_64-linux-gnu/libhdf5_hl.so
```




Note that in my case the version number libhdf5\_serial.so is 10.1.0 and 10.0.2 for the libhdf5\_serial\_hl, just pay attention that you have same version, otherwise just change it to the version you have





8. Compile the Caffe
====================================================================================================================================================================================



Okay, finally we can compile Caffe package we need make and test the compilation as follow:



``` {.prettyprint}
make all
make test
make runtest
```

If everything went fine hopefully the compilation process you should get similar results:

![](https://paper.dropbox.com/ep/redirect/image?url=https%3A%2F%2Fd2mxuefqeaa7sj.cloudfront.net%2Fs_8A2A77A358E3169DD92D4304A9B14ED189F4CD5A9C9406CE34E5618566268596_1490317333764_Screenshot%2Bfrom%2B2017-03-21%2B14-27-14.png&hmac=w4gdIE3nip957cC9I2z9Obx29vg1S4UFjHELawahkYo%3D&width=1490)


9. Compile Caffe-Python Interface
=================================================================================================================================================================================================



Since Caffe support Python so we will install pycaffe [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}a python interface with Caffe), as follow:


``` {.prettyprint}
make pycaffe
echo export PYTHONPATH=/path/to/caffe/python:$PYTHONPATH >> ~/.bashrc
source ~/.bashrc
```



10. Try python caffe module
===========================================================================================================================================================================================



Now as a final step, just make sure that your pycaffe is working by importing caffe module into python, you can test that using python console as follow:


``` {.prettyprint}
python
>>>import caffe
```



Does it work with you? then congratulations!, if not, please leave a comment so I can help you with that.





Note I used multiple references and websites that helped me to do the installation, here is the complete list that can help you as well:


1.  <http://caffe.berkeleyvision.org/>
2.  <http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html>
3.  <https://chunml.github.io/ChunML.github.io/project/Installing-Caffe-CPU-Only/>
4.  <https://sandeeppalakkal.wordpress.com/2016/07/09/installation-of-caffe-on-cpu-only-without-gpu/>

 




