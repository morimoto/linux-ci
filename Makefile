YAML	= $(subst .yaml,,$(subst yaml/,,$(shell ls ./yaml/*.yaml)))
CONFIG	= $(shell ls ./config)

all:
	make -f make.ci
	make clean

${YAML}:
	./script/makefile.py -y ./yaml/${@}.yaml
	make

${CONFIG}:
	./script/makefile.py -c ${@}
	make

save_defconfig:
	./script/makefile.py -s
	make

clean:
	rm make.ci
