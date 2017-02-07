Name:           pgdbf
Version:        0.6.2
Release:        1%{?dist}
Summary:        Convert XBase / FoxPro databases to PostgreSQL

License:        GPLv3+
URL:            https://github.com/kstrauser/pgdbf
Source0:        https://github.com/kstrauser/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libtool autoconf automake gettext-devel

%description
PgDBF is a program for converting XBase databases - particularly FoxPro tables
with memo files - into a format that PostgreSQL can directly import. It's a
compact C project with no dependencies other than standard Unix libraries.

While the project is relatively tiny and simple, it's also heavily optimized
via profiling - routine benchmark were many times faster than with other Open
Source programs. In fact, even on slower systems, conversions are typically
limited by hard drive speed.

%prep
%autosetup


%build
libtoolize --force
aclocal
autoheader
automake --force-missing --add-missing
autoconf
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Feb  7 2017 Pavel Alexeev (aka Pahan-Hubbitus) <Pahan@Hubbitus.info> - 0.6.2-1
- Initial spec
