PYTHON=`which python`
PREFIX=/usr
DESTDIR=/
PKGNAME=pactray
VERSION=0.1.0

all: clean
	$(PYTHON) setup.py build

install: all
	$(PYTHON) setup.py install --prefix $(PREFIX) --root $(DESTDIR)

clean:
	$(PYTHON) setup.py clean
	rm -rf build/

distclean: clean
	rm -rf dist/
	rm -rf pkg/
	rm -rf $(PKGNAME)-*.tar.gz

dist: distclean
	mkdir -p /tmp/pkg/$(PKGNAME)-$(VERSION)
	cp -Rf * /tmp/pkg/$(PKGNAME)-$(VERSION)
	mv /tmp/pkg .
	find . -name *.pyc | xargs rm -rf
	find . -name .svn | xargs rm -rf
	cd pkg/ && tar -cvzf ../$(PKGNAME)-$(VERSION).tar.gz $(PKGNAME)-$(VERSION)
	rm -rf pkg/
