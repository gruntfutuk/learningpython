
all:
	@(cd sipgen; $(MAKE))
	@(cd siplib; $(MAKE))

install:
	@(cd sipgen; $(MAKE) install)
	@(cd siplib; $(MAKE) install)
	@test -d $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages || mkdir -p $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages
	cp -f sipconfig.py $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages/sipconfig.py
	cp -f /Users/stuartmoore/IDrive-Sync/pythonscratch/sip-4.19.6/sipdistutils.py $(DESTDIR)/Users/stuartmoore/.venv/qtproject/lib/python3.6/site-packages/sipdistutils.py

clean:
	@(cd sipgen; $(MAKE) clean)
	@(cd siplib; $(MAKE) clean)
