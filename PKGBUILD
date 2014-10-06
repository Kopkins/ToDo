# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# See http://wiki.archlinux.org/index.php/Python_Package_Guidelines for more
# information on Python packaging.

# Maintainer: Kyle Hopkins <kylehopkins1215@gmail.com>
pkgname='python-todo-gtk'
pkgver='0.1'
pkgrel=1
pkgdesc="A simple GTK+3 todo list application"
arch=(any)
url=""
license=('GPL')
groups=()
depends=('python' 'git' 'gtk3' 'pygtk')
makedepends=('python-setuptools')
provides=('todo-gtk')
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install='todo.install'
source=()
md5sums=()
_gitroot='https://github.com/Kopkins/ToDo'
_gitname='ToDo'

build() {
  cd "$srcdir"
  msg "Getting files from git server...."
  git clone "$_gitroot" "$_gitname-build"
  cd "$srcdir/$_gitname-build"
}

package() {
  
  python setup.py install --root="$pkgdir/" --optimize=1
  install -D -m644 todo.desktop /usr/share/applications/
	install -D -m644 COPYING.txt /usr/share/licenses/python-todo-gtk/COPYING.txt

}

# vim:set ts=2 sw=2 et:

