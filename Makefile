YAML	= $(subst .yaml,,$(subst yaml/,,$(shell ls ./yaml/*.yaml)))
CONFIG	=

all:
	make -f make.ci
	make clean

${YAML}:
	./script/makefile.py -y ./yaml/${@}.yaml
	make

config:
	./script/makefile.py -c ${CONFIG}
	make

clean:
	rm make.ci
