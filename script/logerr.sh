#! /bin/sh
#===============================
#
# logerr
#
# 2019/12/17 Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>
#===============================
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
^  CALL|\
^  GZIP|\
^  KSYM|\
^  VDSO|\
^  TEST|\
^  WRAP|\
^  LINK|\
^  LOGO|\
^  YACC|\
^  MKELF|\
^  BIN2C|\
^  BUILD|\
^  MKCAP|\
^  CONMK|\
^  TABLE|\
^  SYSNR|\
^  MUNGE|\
^  SYSMAP|\
^  UNROLL|\
^  VDSO2C|\
^  SORTEX|\
^  RELOCS|\
^  HOSTCC|\
^  HOSTLD|\
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
^  MODPOST|\
^  MODINFO|\
^  DESCEND|\
^  HDRTEST|\
^  OBJCOPY|\
^  EXPORTS|\
^  VOFFSET|\
^  MKPIGGY|\
^  ZOFFSET|\
^  PERLASM|\
^  SORTTAB|\
^  HYPERCALLS|\
^  EXTRACT_CERTS|\
^  Kernel:|\
^  Building|\
^CRC|\
^Setup|\
^System|\
^Kernel|\
^scripts|\
^make)" $@
