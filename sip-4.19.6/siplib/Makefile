TARGET = sip.so
OFILES = siplib.o apiversions.o descriptors.o qtlib.o threads.o objmap.o voidptr.o array.o int_convertors.o bool.o
HFILES = sip.h sipint.h array.h 

CC = cc
CXX = c++
LINK = c++
CPPFLAGS = -DNDEBUG -I. -I/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/include/python3.6m
CFLAGS = -pipe -fPIC -Os -Wall -W
CXXFLAGS = -pipe -fPIC -Os -Wall -W
LFLAGS = -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = 
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages || mkdir -p $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages
	cp -f $(TARGET) $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages/$(TARGET)
	@test -d $(DESTDIR)/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/include/python3.6m || mkdir -p $(DESTDIR)/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/include/python3.6m
	cp -f /Users/stuartmoore/IDrive-Sync/pythonscratch/sip-4.19.6/siplib/sip.h $(DESTDIR)/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/include/python3.6m/sip.h
	@test -d $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages || mkdir -p $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages
	cp -f /Users/stuartmoore/IDrive-Sync/pythonscratch/sip-4.19.6/sip.pyi $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages/sip.pyi

clean:
	-rm -f $(TARGET)
	-rm -f siplib.o
	-rm -f apiversions.o
	-rm -f descriptors.o
	-rm -f qtlib.o
	-rm -f threads.o
	-rm -f objmap.o
	-rm -f voidptr.o
	-rm -f array.o
	-rm -f int_convertors.o
	-rm -f bool.o
