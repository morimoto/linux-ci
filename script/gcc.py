#! /usr/bin/env python3
#===============================
#
# gcc
#
# 2019/11/18 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
import os

import base
#====================================
#
# gcc
#
#====================================
class gcc(base.base):
    def ver(self):
        return "12.2.0"

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
    def __init__(self, arch):
        if (not arch in self.arch_all()):
            self.die("not supported arch ({})".format(arch))

        self.arch = arch

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

        if (os.path.exists("{}/{}".format(
                dir, self.tar_name()))):
            return

        self.print("download {}".format(gcc))

        self.run("wget -q -P {} {}".format(
            dir, self.url()))

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
    for arch in base.base().arch_all():
        g = gcc(arch)
        try:
            g.install()
        except:
            g.die("gcc failed")
