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
        g = gcc.gcc(self._arch)

        file =  "mymake"

        self.run("cp {}/script/mymake_template ./{}".format(self.dir_top(), file))
        with open(file, mode="a") as f:
            f.write("ARCH={} make CROSS_COMPILE=\"ccache {}\" DTC_FLAGS=--symbols $@".
                    format(self._arch, g.gcc()))
        os.chmod(file, 0o755)

#====================================
#
# As command
#
#====================================
if __name__=='__main__':
    mymake(sys.argv[1]).install()
