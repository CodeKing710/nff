pkgname=nff
pkgver=1.0.0
pkgrel=1
pkgdesc="An nftables firewall tool built in Python. Not as robust as direct nftables usage but nice to load static rules similar to ufw"
arch=('any')
depends=('python' 'python-yaml' 'nftables')
backup=('etc/nff.yml' 'etc/nftables.d/00-nff.nft')
install=nff.install
source=('nff.py' 'nff-defaults.yml' '00-nff.nft' 'version')
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')

package() {
  # Create necessary directories
  install -d "$pkgdir/usr/share/nff"
  install -d "$pkgdir/usr/bin"
  install -d "$pkgdir/etc/nff.d"
  install -d "$pkgdir/etc/nftables.d"

  # Install main executable
  install -Dm755 nff.py "$pkgdir/usr/bin/nff"

  # Install configs
  install -Dm644 nff-defaults.yml "$pkgdir/etc/nff.yml"
  install -Dm644 00-nff.nft "$pkgdir/etc/nftables.d/00-nff.nft"

  # Backup defaults to the share
  install -Dm644 nff-defaults.yml "$pkgdir/usr/share/nff/nff-defaults.yml"
  install -Dm644 00-nff.nft "$pkgdir/usr/share/nff/00-nff.nft"

  # Install Misc data
  install -Dm644 help "$pkgdir/usr/share/nff/help"
  install -Dm644 version "$pkgdir/usr/share/nff/version"
}
