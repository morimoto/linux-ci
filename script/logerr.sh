#! /bin/sh
#===============================
#
# logerr
#
# 2019/12/17 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
sed -r "s/^\.+//"  $@ |
egrep -v "(\
^  AR|\
^  AS|\
^  CC|\
^  LD|\
^  GEN|\
^  UPD|\
^  X32|\
^  CHK|\
^  DTC|\
^  ITS|\
^  ITB|\
^  DTB|\
^  LEX|\
^  CALL|\
^  GZIP|\
^  KSYM|\
^  VDSO|\
^  TEST|\
^  WRAP|\
^  LINK|\
^  LOGO|\
^  YACC|\
^  SYNC|\
^  MKELF|\
^  MKREG|\
^  BIN2C|\
^  BUILD|\
^  MKCAP|\
^  CONMK|\
^  TABLE|\
^  SYSNR|\
^  MUNGE|\
^  MKDIR|\
^  POLICY|\
^  SYSMAP|\
^  UNROLL|\
^  VDSO2C|\
^  SORTEX|\
^  RELOCS|\
^  HOSTCC|\
^  HOSTLD|\
^  HYPREL|\
^  PASYMS|\
^  SYSTBL|\
^  SYSHDR|\
^  REMOVE|\
^  CPUSTR|\
^  BOOTAS|\
^  BOOTCC|\
^  BOOTAR|\
^  SHIPPED|\
^  STUBCPY|\
^  HDRINST|\
^  HYPCOPY|\
^  HOSTCXX|\
^  HDRTEST|\
^  MODPOST|\
^  MODINFO|\
^  DESCEND|\
^  OBJCOPY|\
^  EXPORTS|\
^  VOFFSET|\
^  MKPIGGY|\
^  ZOFFSET|\
^  PERLASM|\
^  PROMCHK|\
^  SORTTAB|\
^  MKREGTABLE|\
^  HYPERCALLS|\
^  EXTRACT_CERTS|\
^  Kernel:|\
^  Building|\
^###|\
^CRC|\
^make|\
^Setup|\
^System|\
^Kernel|\
^writing|\
^scripts|\
^Generating)"
