#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kwalletmanager
Version  : 18.08.0
Release  : 1
URL      : https://download.kde.org/stable/applications/18.08.0/src/kwalletmanager-18.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.08.0/src/kwalletmanager-18.08.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.08.0/src/kwalletmanager-18.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kwalletmanager-bin
Requires: kwalletmanager-lib
Requires: kwalletmanager-data
Requires: kwalletmanager-license
Requires: kwalletmanager-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kwalletmanager package.
Group: Binaries
Requires: kwalletmanager-data
Requires: kwalletmanager-license

%description bin
bin components for the kwalletmanager package.


%package data
Summary: data components for the kwalletmanager package.
Group: Data

%description data
data components for the kwalletmanager package.


%package doc
Summary: doc components for the kwalletmanager package.
Group: Documentation

%description doc
doc components for the kwalletmanager package.


%package lib
Summary: lib components for the kwalletmanager package.
Group: Libraries
Requires: kwalletmanager-data
Requires: kwalletmanager-license

%description lib
lib components for the kwalletmanager package.


%package license
Summary: license components for the kwalletmanager package.
Group: Default

%description license
license components for the kwalletmanager package.


%package locales
Summary: locales components for the kwalletmanager package.
Group: Default

%description locales
locales components for the kwalletmanager package.


%prep
%setup -q -n kwalletmanager-18.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535235572
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535235572
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kwalletmanager
cp COPYING %{buildroot}/usr/share/doc/kwalletmanager/COPYING
cp COPYING.LIB %{buildroot}/usr/share/doc/kwalletmanager/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kcmkwallet
%find_lang kwalletmanager

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/kcm_kwallet_helper5

%files bin
%defattr(-,root,root,-)
/usr/bin/kwalletmanager5

%files data
%defattr(-,root,root,-)
/usr/share/applications/kwalletmanager5-kwalletd.desktop
/usr/share/applications/org.kde.kwalletmanager5.desktop
/usr/share/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
/usr/share/icons/hicolor/128x128/apps/kwalletmanager.png
/usr/share/icons/hicolor/128x128/apps/kwalletmanager2.png
/usr/share/icons/hicolor/16x16/apps/kwalletmanager.png
/usr/share/icons/hicolor/16x16/apps/kwalletmanager2.png
/usr/share/icons/hicolor/22x22/actions/wallet-closed.png
/usr/share/icons/hicolor/22x22/actions/wallet-open.png
/usr/share/icons/hicolor/22x22/apps/kwalletmanager.png
/usr/share/icons/hicolor/32x32/apps/kwalletmanager.png
/usr/share/icons/hicolor/32x32/apps/kwalletmanager2.png
/usr/share/icons/hicolor/48x48/apps/kwalletmanager.png
/usr/share/icons/hicolor/48x48/apps/kwalletmanager2.png
/usr/share/icons/hicolor/64x64/apps/kwalletmanager.png
/usr/share/icons/hicolor/64x64/apps/kwalletmanager2.png
/usr/share/kservices5/kwalletconfig5.desktop
/usr/share/kservices5/kwalletmanager5_show.desktop
/usr/share/kxmlgui5/kwalletmanager5/kwalletmanager.rc
/usr/share/metainfo/org.kde.kwalletmanager5.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kwallet5/index.cache.bz2
/usr/share/doc/HTML/ca/kwallet5/index.docbook
/usr/share/doc/HTML/de/kwallet5/edit1.png
/usr/share/doc/HTML/de/kwallet5/edit2.png
/usr/share/doc/HTML/de/kwallet5/first-open-request.png
/usr/share/doc/HTML/de/kwallet5/index.cache.bz2
/usr/share/doc/HTML/de/kwallet5/index.docbook
/usr/share/doc/HTML/de/kwallet5/kwalletmanager.png
/usr/share/doc/HTML/de/kwallet5/openwallet-request.png
/usr/share/doc/HTML/de/kwallet5/save-login-information.png
/usr/share/doc/HTML/en/kwallet5/application-request-to-open-wallet.png
/usr/share/doc/HTML/en/kwallet5/error-nokey.png
/usr/share/doc/HTML/en/kwallet5/first-open-request.png
/usr/share/doc/HTML/en/kwallet5/index.cache.bz2
/usr/share/doc/HTML/en/kwallet5/index.docbook
/usr/share/doc/HTML/en/kwallet5/key-selection.png
/usr/share/doc/HTML/en/kwallet5/kwallet-access-control.png
/usr/share/doc/HTML/en/kwallet5/kwallet-applications.png
/usr/share/doc/HTML/en/kwallet5/kwallet-edit.png
/usr/share/doc/HTML/en/kwallet5/kwalletmanager.png
/usr/share/doc/HTML/en/kwallet5/openwallet-request.png
/usr/share/doc/HTML/en/kwallet5/save-login-information.png
/usr/share/doc/HTML/en/kwallet5/wallet-encryption-selection.png
/usr/share/doc/HTML/es/kwallet5/index.cache.bz2
/usr/share/doc/HTML/es/kwallet5/index.docbook
/usr/share/doc/HTML/it/kwallet5/index.cache.bz2
/usr/share/doc/HTML/it/kwallet5/index.docbook
/usr/share/doc/HTML/nl/kwallet5/index.cache.bz2
/usr/share/doc/HTML/nl/kwallet5/index.docbook
/usr/share/doc/HTML/pt/kwallet5/index.cache.bz2
/usr/share/doc/HTML/pt/kwallet5/index.docbook
/usr/share/doc/HTML/pt_BR/kwallet5/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kwallet5/index.docbook
/usr/share/doc/HTML/ru/kwallet5/index.cache.bz2
/usr/share/doc/HTML/ru/kwallet5/index.docbook
/usr/share/doc/HTML/sr/kwallet5/index.cache.bz2
/usr/share/doc/HTML/sr/kwallet5/index.docbook
/usr/share/doc/HTML/sv/kwallet5/index.cache.bz2
/usr/share/doc/HTML/sv/kwallet5/index.docbook
/usr/share/doc/HTML/uk/kwallet5/edit1.png
/usr/share/doc/HTML/uk/kwallet5/edit2.png
/usr/share/doc/HTML/uk/kwallet5/index.cache.bz2
/usr/share/doc/HTML/uk/kwallet5/index.docbook
/usr/share/doc/HTML/uk/kwallet5/kwalletmanager.png
/usr/share/doc/HTML/uk/kwallet5/openwallet-request.png
/usr/share/doc/HTML/uk/kwallet5/save-login-information.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_kwallet5.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/kwalletmanager/COPYING
/usr/share/doc/kwalletmanager/COPYING.LIB

%files locales -f kcmkwallet.lang -f kwalletmanager.lang
%defattr(-,root,root,-)

