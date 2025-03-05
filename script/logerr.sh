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
^  RSTRIP|\
^  CPUSTR|\
^  BOOTAS|\
^  BOOTCC|\
^  BOOTAR|\
^  INSTALL|\
^  IPE_POL|\
^  SEEDHDR|\
^  SHIPPED|\
^  STUBCPY|\
^  SYMLINK|\
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
^Generating|\
.*\.dt[bs][io]?\:)"
