#! /usr/bin/env python3
#===============================
#
# gcc
#
#	Install latest version gcc for all arch
#	> ./script/gcc.py
#
#	Install x86, arm64 gcc 14.30.0
#	> ./script/gcc.py --arch x86,arm64 --ver 14.3.0
#
# 2019/11/18 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
import os
import sys
import argparse

import base
#====================================
#
# gcc
#
#====================================
class gcc(base.base):
    __latest_ver = "16.1.0"

    def ver(self):
        return self.__ver;

    def dir_download(self):
        return "{}/tools/download".format(self.dir_top())

    def dir_install(self):
        return "{}/tools".format(self.dir_top())

    def gcc(self):
        return "{}/tools/gcc-{}-nolibc/{}/bin/{}-".format(self.dir_top(),
                                                          self.ver(),
                                                          self.name(),
                                                          self.name())

    #--------------------
    # __init__()
    #--------------------
    def __init__(self, arch, ver = None):
        if (not arch in self.arch_all()):
            self.die("not supported arch ({})".format(arch))

        self.arch = arch
        self.__ver = self.__latest_ver
        if (ver):
            self.__ver = ver

    #--------------------
    # name()
    #
    # ex)
    #	aarch64-linux
    #--------------------
    def name(self):
        info = self.arch_info(self.arch)
        return "{}-linux{}".format(
            info["gcc"],
            info["gcc_opt"] if "gcc_opt" in info else "")

    #--------------------
    # tar_name()
    #
    # ex)
    #	x86_64-gcc-8.1.0-nolibc-aarch64-linux.tar.xz
    #--------------------
    def tar_name(self):
        return "x86_64-gcc-{}-nolibc-{}.tar.xz".format(
            self.ver(), self.name())

    #--------------------
    # url()
    #--------------------
    def url(self):
        return "https://mirrors.edge.kernel.org/pub/tools/crosstool/files/bin/x86_64/{}/{}".format(
            self.ver(), self.tar_name())

    #--------------------
    # download()
    #--------------------
    def download(self, gcc):
        dir = self.dir_download()

        # remove tmp dir
        self.run("rm -fr {}-tmp".format(dir))

        if (os.path.exists("{}/{}".format(
                dir, self.tar_name()))):
            return

        self.print("download {}".format(gcc))

        # download it to tmp dir
        ret = self.run("wget -q -P {}-tmp {}".format(dir, self.url()))
        if (ret == 0):
            self.run("mkdir -p {}".format(dir))
            self.run("mv {}-tmp/{} {}/{}".format(dir, self.tar_name(),
                                                 dir, self.tar_name()))
        else:
            self.run("rm -fr {}-tmp".format(dir))

    #--------------------
    # unpack()
    #--------------------
    def unpack(self, gcc):
        ddir = self.dir_download()
        idir = self.dir_install()

        if (os.path.exists("{}/{}".format(idir, gcc))):
            return

        self.print("install  {}".format(gcc))

        self.run("tar -Jxf {}/{} -C {}".format(
            ddir, self.tar_name(), idir))

    #--------------------
    # install()
    #--------------------
    def install(self):
        gcc = "gcc-{}-nolibc/{}".format(self.ver(), self.name())

        self.download(gcc)
        self.unpack(gcc)

#====================================
#
# As command
#
#====================================
if __name__=='__main__':
    ver = None

    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--arch", help="select target arch. If not, all arch will be selected")
    parser.add_argument("-v","--ver", help="select target gcc version. If not, latest version will be selected")
    args = parser.parse_args()

    arch_list = base.base().arch_all()
    if (args.arch):
        arch_list = args.arch.split(",")

    if (args.ver):
        ver = args.ver

    for arch in arch_list:
        gcc(arch, ver).install()
