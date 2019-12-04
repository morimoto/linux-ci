#! /usr/bin/env python3
#===============================
#
# makefile
#
# 2019/11/26 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
import sys
import os

import base
import gcc

#====================================
#
# makefile
#
#====================================
class makefile(base.base):
    #--------------------
    # __init__()
    #--------------------
    def __init__(self):
        self.makefile = None

        self._file = "{}/make.ci".format(self.dir_top())
        if (self.exist()):
            self.die("previous make not yet finished")

        self.setup    = base.yml(self.file_setup())
        self.makefile = open(self._file, mode='w')
        self.done     = 0

    #--------------------
    # __del__()
    #--------------------
    def __del__(self):
        if (self.makefile):
            self.makefile.close()
            if (not self.done):
                os.remove(self._file)

    #--------------------
    # exist()
    #--------------------
    def exist(self):
        return os.path.exists(self._file)

    #--------------------
    # write()
    #--------------------
    def write(self, text):
        self.makefile.write(text)

    #--------------------
    # create_target_name()
    #--------------------
    def create_target_name(self, config):
        self.write("{}:\n".format(config.name()))

    #--------------------
    # create_bin_dir()
    #--------------------
    def create_bin_dir(self, config):

        bin	= base.binary(config)
        kernel	= self.setup.val("kernel")

        if (not bin.exist()):
            self.write("	cd {};\\\n".format(kernel))
            self.write("	make O={} olddefconfig\n".format(bin.path()))

    #--------------------
    # create_make()
    #--------------------
    def create_make(self, config):
        bin  = base.binary(config)
        log  = self.setup.val("log")
        jobs = self.setup.val("jobs")

        jobs = " -j {}".format(jobs) if (jobs) else ""

        gcc.gcc(config.arch()).install()

        self.create_target_name(config)
        self.create_bin_dir(config)

        # at binary
        self.write("	cd {};\\\n".format(bin.path()))
        self.write("	rm -fr log;\\\n")
        self.write("	../../script/mymake.py {};\\\n".format(config.arch()))
        self.write("	cp {} .config;\\\n".format(config.path()))
        self.write("	./mymake olddefconfig;\\\n")

        # *Note*
        #
        # We *can't* get error code from make if we used "tee" command.
        # The code is always "success", because it come from "tee".
        # But, let's use this behavior, because we want to keep Linux-CI
        # eventhough error case if many target are selected.
        #
        # OTOH, Gitlab needs to get error code, otherwise,
        # the result always loged as "success" eventhough it was error.
        # But, it don't need to record log.
        #
        # "mail.py" will return 0 eventhough previous mymake was failed.
        # But, we need it if Gitlab.
        # We don't needed it if "log" was not selected
        if (log):
            self.write("	./mymake{} 2>&1 | tee ./log;\\\n".format(jobs))
            self.write("	../../script/mail.py {}\n".format(bin.name()))
        else:
            self.write("	./mymake{}\n".format(jobs))

        self.write("\n")

    #--------------------
    # create_via_yaml()
    #--------------------
    def create_via_yaml(self, file):
        yaml	= base.yml(file)

        self.write("all:")
        for config in yaml.each_target():
            self.write(" {}".format(config.name()))
        self.write("\n\n")

        for config in yaml.each_target():
            self.create_make(config)

        self.done = 1

    #--------------------
    # create_save_config()
    #--------------------
    def create_save_config(self):

        self.write("all:")

        for arch in base.base().arch_all():
            for config in ["allyesconfig", "allmodconfig"]:
                self.write(" {}-{}".format(arch, config))
        self.write("\n\n")

        for arch in base.base().arch_all():

            gcc.gcc(arch).install()

            for config in ["allyesconfig", "allmodconfig"]:
                cfg = base.config("{}-{}".format(arch, config))
                bin = base.binary(cfg)

                self.create_target_name(cfg)
                self.create_bin_dir(cfg)

                self.write("	cd {};\\\n".format(bin.path()))
                self.write("	../../script/mymake.py {};\\\n".format(arch))
                self.write("	./mymake {};\\\n".format(config))
                self.write("	cp .config {}\n".format(cfg.path()))
                self.write("\n")

        self.done = 1

    #--------------------
    # create_via_config()
    #--------------------
    def create_via_config(self, config):

        self.create_make(config)

        self.done = 1

    #--------------------
    # create_git_push()
    #--------------------
    def create_git_push(self, args):
        self.print("ref: {}".format(args[0]))
        self.print("old: {}".format(args[1]))
        self.print("new: {}".format(args[2])) # pushed commit

        commit		= args[2]
        setup		= base.yml(self.file_setup())
        yaml		= base.yml("{}/{}".format(self.dir_top(),
                                                  setup.val("ci_yaml")))
        kernel		= setup.val("kernel")
        ci_branch	= setup.val("ci_branch")

        self.write("all: kernel_update linuxci_update")
        for config in yaml.each_target():
            self.write(" {}".format(config.name()))
        self.write("\n\n")

        self.write("kernel_update:\n")
        self.write("	cd {};\\\n".format(kernel))
        self.write("	git --git-dir=.git prune;\\\n")
        self.write("	git --git-dir=.git gc;\\\n")
        self.write("	git --git-dir=.git repack;\\\n")
        self.write("	git --git-dir=.git remote update --prune;\\\n")
        self.write("	git --git-dir=.git checkout {};\n".format(commit))
        self.write("\n")

        self.write("linuxci_update:\n")
        self.write("	cd {};\\\n".format(self.dir_top()))
        self.write("	git --git-dir=.git prune;\\\n")
        self.write("	git --git-dir=.git gc;\\\n")
        self.write("	git --git-dir=.git repack;\\\n")
        self.write("	git --git-dir=.git remote update --prune;\\\n")
        self.write("	git --git-dir=.git checkout {};\n".format(ci_branch))
        self.write("\n")

        for config in yaml.each_target():
            self.create_make(config)

        self.done = 1

#====================================
#
# As command
#
#====================================
if __name__=='__main__':

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('-y', '--yaml', dest='yaml',
                      action='store_true', default=False,
                      help='create makefile via yaml')
    parser.add_option('-c', '--config', dest='config',
                      action='store_true', default=False,
                      help='create makefile via config')
    parser.add_option('-s', '--save', dest='save',
                      action='store_true', default=False,
                      help='save configs')
    parser.add_option('-p', '--push', dest='push',
                      action='store_true', default=False,
                      help='git push makefile')

    option, args = parser.parse_args(sys.argv[1:])

    mk = makefile()

    if (option.yaml):
        mk.create_via_yaml(args[0])
    elif (option.config):
        mk.create_via_config(base.config(args[0]))
    elif (option.save):
        mk.create_save_config()
    elif (option.push):
        mk.create_git_push(args)
    else:
        base.base().die("unknown command")
