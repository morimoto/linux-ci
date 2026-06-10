#! /bin/bash
#===============================
#
# mymake_title
#
# 2026/01/28 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
TGT=`grep include       Makefile | sed -e "s/\//\n/g" | tail -n 2 | head -n 1`
DIR=`grep KBUILD_OUTPUT Makefile | sed -e "s/\//\n/g" | tail -n 1`
SEP=
[ x${DIR} != x ] && SEP=" / "

echo "-----------------------"
echo "${TGT}${SEP}${DIR}"
echo "-----------------------"
