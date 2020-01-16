#! /bin/sh
#===============================
#
# logerr
#
# 2019/12/17 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
egrep -v "(^  GEN|^  UPD|^  HDRINST|^  CC|^  CALL|^  AR|^  CHK|^  LD|^  GZIP|^  MODPOST|^  MODINFO|^  KSYM|^  SYSMAP|^  Building|^  DESCEND|^  HDRTEST|^  X32|^  VDSO|^  OBJCOPY|^  VDSO2C|^  EXPORTS|^  UNROLL|^  BIN2C|^  SORTEX|^  VOFFSET|^  RELOCS|^  HOSTCC|^  HOSTLD|^  MKPIGGY|^  AS|^  ZOFFSET|^  BUILD|^  TEST|^  Kernel:|^  DTC|^  ITS|^  ITB|^  WRAP|^Setup|^System|^CRC|^scripts|^Kernel|^make)" $@
