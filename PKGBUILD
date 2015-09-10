# Maintainer: Thermionix

pkgname=pactray
pkgver=1.0
pkgrel=1
pkgdesc="Pacman tray notifier."
arch=('any')
license=('GPL')
url=""
depends=('pacman' 'python-gobject')
optdepends=('cower: check aur packages')
source=('pactray.py' 'archlogo.png')
md5sums=('')

build() {
	mkdir -p ${pkgdir}/usr/bin

	cp -f ${srcdir}/pactray.py ${pkgdir}/usr/bin/pactray

	chmod -R 755 ${pkgdir}/
}
