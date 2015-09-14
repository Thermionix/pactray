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
source=()
md5sums=()

build() {
	python setup.py build
	python setup.py install --prefix=${pkgdir}/usr
}

