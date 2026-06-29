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
    # install()
    #--------------------
    def install(self, arch):
        g = gcc.gcc(arch)

        file =  "mymake"

        self.run("cp {}/script/mymake_template ./{}".format(self.dir_top(), file))
        with open(file, mode="a") as f:
            f.write("ARCH={} make ".format(arch))
            f.write("CROSS_COMPILE=\"ccache {}\" ".format(g.gcc()))

            # parisc special
            if (arch == "parisc"):
                f.write("CROSS32_COMPILE=\"ccache {}\" ".format(g.gcc()))

            f.write("DTC_FLAGS=--symbols $@\n")

        os.chmod(file, 0o755)

#====================================
#
# As command
#
#====================================
if __name__=='__main__':
    mymake().install(sys.argv[1])
