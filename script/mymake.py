#! /usr/bin/env python3
#===============================
#
# mymake
#
# 2019/11/26 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
import sys
import os

import base
import gcc
#====================================
#
# mymake
#
#====================================
class mymake(base.base):
    #--------------------
    # __init__()
    #--------------------
    def __init__(self, arch):
        self._arch = arch

    #--------------------
    # install()
    #--------------------
    def install(self):
        ccache = base.yml(self.file_setup()).val("ccache")
        warning= base.yml(self.file_setup()).val("warning")
        g = gcc.gcc(self._arch)

        file =  "mymake"
        ccache = "ccache " if (ccache) else ""
        warning = "W=1" if (warning) else ""

        with open(file, mode="w") as f:
            f.write("ARCH={} make {} CROSS_COMPILE=\"{}{}\" DTC_FLAGS=--symbols $@".
                    format(self._arch, warning, ccache, g.gcc()))
        os.chmod(file, 0o755)

#====================================
#
# As command
#
#====================================
if __name__=='__main__':
    mymake(sys.argv[1]).install()
