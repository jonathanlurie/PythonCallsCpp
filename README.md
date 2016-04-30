# What?
This repo shows with simple examples how to wire some low-level C/C++ code to Python using only [Ctypes](https://docs.python.org/2/library/ctypes.html). The C/C++ code will be compiled into a dynamic library (.so), while the Python code remains py files (eh).

# Why?
In some case, it's nice to get the speed of a low level language (such as C or C++) **and** the *quick setup* of a *pseudo*-interpreted language (such as Python).  

There are 3 common ways to execute C/C++ code from a Python script:
- Using [SWIG](http://www.swig.org/Doc1.3/Python.html)
- Using [Boost.Python](https://wiki.python.org/moin/boost.python/GettingStarted)
- Using [Ctypes](https://docs.python.org/2/library/ctypes.html)

While the two firsts can be quite cumbersome and require more time to set up, they are also more suitable for large projects and a *true* object oriented interface. This project is about **the later**: quick, easy and efficient for most small projects.

# How?
First, compile the C++ code into a dynamic library:
```shell
$ cd cpp
$ make
```
You have just created the dylib `cpp/bin/release/mydylib.so`.  

Then, you can run your python script:
```shell
$ cd python
$ python run.py
```

This should print something like that:   
```shell
Hello, Johnny Bravo, welcome onboard!
result: 144.300003052
6.75
```


# Thanks
A special thanks to [Micheal Crowford](https://github.com/mbcrawfo)'s [Generic Makefile](https://github.com/mbcrawfo/GenericMakefile) project.  
In order to adapt it into compiling a dynamic library (rather than an executable program), I just changed that:
- l:205 adding -dynamiclib
- l:218 adding -fPIC

**License**  
Who cares? It's just an example...
