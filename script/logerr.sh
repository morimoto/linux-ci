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
^  NM|\
^  CHK|\
^  CAT|\
^  DTB|\
^  DTC|\
^  GEN|\
^  UPD|\
^  X32|\
^  ITS|\
^  ITB|\
^  LEX|\
^  PAD|\
^  OVL|\
^  CALL|\
^  CERT|\
^  COPY|\
^  GZIP|\
^  KSYM|\
^  VDSO|\
^  TEST|\
^  WRAP|\
^  PERL|\
^  LINK|\
^  LOGO|\
^  YACC|\
^  PERL|\
^  SYNC|\
^  BIN2C|\
^  BUILD|\
^  CONMK|\
^  DTOVL|\
^  MUNGE|\
^  MKDIR|\
^  MKMAP|\
^  MKELF|\
^  MKREG|\
^  MKCAP|\
^  SYSNR|\
^  STRIP|\
^  TABLE|\
^  BOOTAS|\
^  BOOTCC|\
^  BOOTAR|\
^  CPUSTR|\
^  HOSTCC|\
^  HOSTLD|\
^  HYPREL|\
^  PASYMS|\
^  POLICY|\
^  REMOVE|\
^  RSTRIP|\
^  RELOCS|\
^  SYSTBL|\
^  SYSHDR|\
^  SYSMAP|\
^  SORTEX|\
^  UNROLL|\
^  VDSO2C|\
^  EXPORTS|\
^  DESCEND|\
^  Kernel:|\
^  HDRINST|\
^  HYPCOPY|\
^  HOSTCXX|\
^  HDRTEST|\
^  INSTALL|\
^  IPE_POL|\
^  MKPIGGY|\
^  MODPOST|\
^  MODINFO|\
^  OBJCOPY|\
^  PERLASM|\
^  PROMCHK|\
^  SORTTAB|\
^  SEEDHDR|\
^  SHIPPED|\
^  STUBCPY|\
^  SYMLINK|\
^  VOFFSET|\
^  ZOFFSET|\
^  Building|\
^  HYPERCALLS|\
^  MKREGTABLE|\
^  EXTRACT_CERTS|\
^###|\
^CRC|\
^make|\
^Setup|\
^System|\
^Kernel|\
^writing|\
^scripts|\
^Generating|\
.*\.dt[bs][io]?\:)"
