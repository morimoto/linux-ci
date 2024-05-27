#! /usr/bin/env python3
#===============================
#
# base
#
# 2019/11/18 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
import os
import sys
import subprocess
import yaml
import re

#====================================
#
# base
#
#====================================
class base:
    __top = os.path.abspath(__file__ + "/../../");

    # "arch" will be used for make
    #	ARM=arm make xxxx
    #
    # "gcc", "gcc_opt" will be used for gcc name
    #	x86_64-gcc-8.1.0-nolibc-aarch64-linux.tar.xz
    __architecture = {
        # arch		gcc		gcc_opt
        "x86":		{"gcc":"x86_64"},
        "arm":		{"gcc":"arm",	"gcc_opt":"-gnueabi"},
        "arm64":	{"gcc":"aarch64"},
        "sh":		{"gcc":"sh4"},
        "mips":		{"gcc":"mips"},
        "m68k":		{"gcc":"m68k"},
        "powerpc":	{"gcc":"powerpc64"},
        "xtensa":	{"gcc":"xtensa"},
        "sparc":	{"gcc":"sparc"},
        "openrisc":	{"gcc":"or1k"},
    };

    #--------------------
    # exit()
    #
    # it is used not under try-except
    #--------------------
    def die(self, text):
        self.print("========================")
        self.print(text)
        self.print("========================")
        sys.exit(1)

    #--------------------
    # error()
    #
    # it is used under try-except
    #--------------------
    def error(self, text):
        self.print("========================")
        self.print(text)
        self.print("========================")
        raise Exception(text)

    #--------------------
    # dir_top()
    #--------------------
    def dir_top(self):
        return base.__top

    #--------------------
    # file_setup()
    #--------------------
    def file_setup(self):
        return "{}/yaml/setup.yaml".format(self.dir_top())

    #--------------------
    # arch_all()
    #--------------------
    def arch_all(self):
        return base.__architecture.keys()

    #--------------------
    # arch_info()
    #--------------------
    def arch_info(self, arch):
        if (arch in base.__architecture):
            return base.__architecture[arch];
        self.error("{} is not supported".format(arch))

    #--------------------
    # print
    #--------------------
    def print(self, text):
        print(text, flush=True)

    #--------------------
    # run()
    #
    # do command
    #--------------------
    def run(self, command):
        return subprocess.run(command, shell=True).returncode

    #--------------------
    # do()
    #
    # do command, use return
    #--------------------
    def do(self, command):
        return re.sub(r"\n$", r"",
                      subprocess.check_output(command.split()).decode())

#====================================
#
# yml
#
#====================================
class yml:

    #--------------------
    # __init__
    #--------------------
    def __init__(self, file):
        if (not os.path.exists(file)):
            base().die("no file ({})".format(file))

        with open(file) as f:
            self.data = yaml.safe_load(f)

    #--------------------
    # val()
    #--------------------
    def val(self, key):
        return self.data.get(key)

    #--------------------
    # each_target()
    #--------------------
    def each_target(self):
        for cfg in self.val("target"):
            yield config(cfg)

#====================================
#
# file
#
#====================================
class file(base):

    #--------------------
    # __init__()
    #--------------------
    def __init__(self, filename):
        fullpath = os.path.abspath(filename)
        self._dir  = os.path.dirname(fullpath)
        self._name = os.path.basename(fullpath)

    #--------------------
    # name()
    #--------------------
    def name(self):
        return self._name

    #--------------------
    # dir()
    #--------------------
    def dir(self):
        return self._dir

    #--------------------
    # path()
    #--------------------
    def path(self):
        return "{}/{}".format(self.dir(),
                              self.name())
    #--------------------
    # exist()
    #--------------------
    def exist(self):
        return os.path.exists(self.path())

#====================================
#
# config
#
#====================================
class config(file):

    #--------------------
    # __init__()
    #--------------------
    def __init__(self, name):
        import linecache

        super(config, self).__init__(name)

        #
        # assumed name
        #	xxxx/xxxx/arch-target
        #
        # or see below
        #	arch-{command}
        #
        ret = re.match("(\\w+)-(.*)", self.name())
        if (not ret):
            self.die("file should arch-target ({})".format(self.name()))

        self._arch = ret.group(1)
        self._command = None;

        #
        # command
        # ex)
        #	xxx-allyesconfig
        #	xxx-allmodconfig
        #	...
        #
        if (not self.exist()):
            command = ret.group(2)
            self._command = command;

    #--------------------
    # arch()
    #--------------------
    def arch(self):
        return self._arch

    #--------------------
    # command()
    #--------------------
    def command(self):
        return self._command

#====================================
#
# binary
#
#====================================
class binary(file):

    #--------------------
    # __init__()
    #--------------------
    def __init__(self, config):
        super(binary, self).__init__("{}/binary/{}".format(self.dir_top(), config.name()))

#====================================
# chdir
#====================================
class chdir(base):
    def __init__(self, dir):
        self.dir = dir

    def __enter__(self):
        os.chdir(self.dir)

    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self.dir_top())
