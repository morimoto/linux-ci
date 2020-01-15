#! /usr/bin/env python3
#===============================
#
# mail
#
# 2019/11/26 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
import sys
import os

import base
#====================================
#
# mail
#
#====================================
class mail(base.base):

    #--------------------
    # __init__()
    #--------------------
    def __init__(self, config):
        setup = base.yml(self.file_setup())
        logerr = setup.val("logerr")
        mail = base.yml(self.file_setup()).val("mail")
        cfg = base.config(config)
        bin = base.binary(cfg)
        log = "{}/log".format(bin.path())

        if (not mail):
            return

        if (not bin.exist()):
            return

        if (not os.path.exists(log)):
            return

        if (logerr):
            self.run("{}/script/logerr.sh {} | mail -s \"Linux-CI error: {}\" {}".
                     format(self.dir_top(), log, config, mail))
        else:
            self.run("mail -s \"Linux-CI: {}\" {} < {}".
                     format(config, mail, log))

#====================================
#
# As command
#
#====================================
if __name__=='__main__':
    mail(sys.argv[1])
