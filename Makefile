YAML	= $(subst .yaml,,$(subst yaml/,,$(shell ls ./yaml/*.yaml)))

all:
	make -f make.ci
	make clean

${YAML}:
	./script/makefile.py -y ./yaml/${@}.yaml
	make

save_defconfig:
	./script/makefile.py -s
	make

clean:
	rm make.ci
