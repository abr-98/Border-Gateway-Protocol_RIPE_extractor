
CC	= gcc -fPIC
CFLAGS	= -g  -Wall -Wsystem-headers -Wno-format-y2k -Wno-sign-compare -Wcast-align -Wmissing-prototypes -Wpointer-arith -Wreturn-type -Wswitch -Wshadow
COMPILE  = $(CC) $(CFLAGS) $(INCLUDES)

LD	= gcc
LDFLAGS	= 
SOFLAGS =  -shared
RANLIB	= ranlib

SYS_LIBS= -lbz2 -lz 

INSTALL  = install

prefix   = /usr/local
exec_prefix = ${prefix}
bindir   = ${exec_prefix}/bin
libdir   = ${exec_prefix}/lib
includedir = ${prefix}/include

LIB_H	 = bgpdump_attr.h bgpdump_formats.h bgpdump_lib.h bgpdump_mstream.h
LIB_O	 = bgpdump_lib.o bgpdump_mstream.o cfile_tools.o util.o inet_ntop.o
OTHER    = *.in configure bgpdump.spec README* ChangeLog License*

all: libbgpdump.so bgpdump 

libbgpdump.a: $(LIB_H) $(LIB_O) Makefile cfile_tools.h util.h
	ar r libbgpdump.a $(LIB_O)
	$(RANLIB) libbgpdump.a

libbgpdump.so: libbgpdump.a
	$(COMPILE) $(LDFLAGS) $(SOFLAGS) -o libbgpdump.so $(LIB_O) $(SYS_LIBS)

example: example.c libbgpdump.a
	$(COMPILE) $(LDFLAGS) -o example example.c libbgpdump.a $(SYS_LIBS)

bgpdump: bgpdump.c libbgpdump.a
	$(COMPILE) $(LDFLAGS) -o bgpdump bgpdump.c libbgpdump.a $(SYS_LIBS)

check-clean:
	rm -f test_out/*.bgp.gz

check: check-clean bgpdump
	./test.sh

clean: check-clean
	rm -f libbgpdump.so libbgpdump.a example bgpdump $(LIB_O)

distclean: clean
	rm -Rf config.log config.status *.dSYM core *.core autom4te.cache bgpdump-config.h Makefile
	rm -Rf $(PKG)

install: all
	$(INSTALL) -d $(DESTDIR)$(bindir) $(DESTDIR)$(includedir) $(DESTDIR)$(libdir)
	$(INSTALL) bgpdump $(DESTDIR)$(bindir)
	$(INSTALL) -m 0644 $(LIB_H) $(DESTDIR)$(includedir)
	$(INSTALL) libbgpdump.so libbgpdump.a $(DESTDIR)$(libdir)

PKG=libbgpdump-1.6.0
dist:
	mkdir $(PKG)
	ln *.h *.c $(OTHER) $(PKG)
	tar -czf $(PKG).tgz $(PKG)
	rm $(PKG)/* && rmdir $(PKG)

rpm: dist
	rpmbuild -v -ta $(PKG).tgz
