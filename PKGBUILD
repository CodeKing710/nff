pkgname=nff
pkgver=0.1.0
pkgrel=1
arch=('any')
depends=('python' 'python-yaml' 'nftables')
source=('nff.py' 'nff-defaults.yml')
sha256sums=('SKIP' 'SKIP')

package() {
  install -Dm755 nff.py "$pkgdir/usr/bin/nff"
  install -Dm644 nff.yml "$pkgdir/etc/nff.yml"
  mkdir -p "$pkgdir/etc/nff.d"
  chmod 755 "$pkgdir/etc/nff.d"
}
