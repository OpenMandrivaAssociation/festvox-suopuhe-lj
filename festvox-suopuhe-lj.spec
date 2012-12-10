
%define name	festvox-suopuhe-lj
%define version	1.0g
%define date	20051204
%define rel	4
%define release	%mkrel %date.%rel

Summary:	Festival Voice - Finnish female speaker (suo_fi_lj)
Name:		%name
Version:	%version
Release:	%release
License:	LGPL
Group:		Sound
URL:		http://phon.joensuu.fi/suopuhe/
Source:		http://phon.joensuu.fi/suopuhe/tulosaineisto/suo_fi_lj-%version-%date.tar.bz2
Source1:	README.MDV
# patches from debian
Patch0:		festvox-suopuhe-lj-paths.diff
Patch1:		festvox-suopuhe-lj-funcname.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	festvox-suopuhe-common
# other festvox packages seem to provide these:
Provides:	festival-voice
Provides:	festival-voice-finnish
Provides:	festival-voice-fi_FI
# per Mandriva locale-specific package policy:
Requires:	locales-fi

%description
This is a Finnish female speaker for the Festival speech synthesis
system. It was developed as part of the Suopuhe project at
the universities of Helsinki and Joensuu.

%package -n	festvox-suopuhe-common
Summary:	Common files for Festival Finnish speakers
Group:		Sound
Suggests:	festvox-suopuhe-mv
Suggests:	festvox-suopuhe-lj

%description -n	festvox-suopuhe-common
This package contains the common files between the two Finnish
Festival speech synthesis speakers, festvox-suopuhe-mv and
festvox-suopuhe-lj.

%prep
%setup -q -n festival
%patch0 -p1
%patch1 -p1
cp -a %{SOURCE1} .
cat > README.install.urpmi <<EOF
See suopuhe usage instructions in
%{_docdir}/festvox-suopuhe-common/README.MDV.
EOF

%install
rm -rf %{buildroot}

install -d -m755 %{buildroot}%{_datadir}/festival/voices/finnish/suopuhe.common
cp -a lib/voices/finnish/suo_fi_lj_diphone/festvox/* \
	%{buildroot}%{_datadir}/festival/voices/finnish/suopuhe.common

install -d -m755 %{buildroot}%{_datadir}/festival/voices/finnish/suo_fi_lj_diphone
cp -a lib/voices/finnish/suo_fi_lj_diphone/group \
	%{buildroot}%{_datadir}/festival/voices/finnish/suo_fi_lj_diphone

ln -s ../suopuhe.common %{buildroot}%{_datadir}/festival/voices/finnish/suo_fi_lj_diphone/festvox

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc lib/voices/finnish/suo_fi_lj_diphone/README.lj
%{_datadir}/festival/voices/finnish/suo_fi_lj_diphone

%files -n festvox-suopuhe-common
%defattr(-,root,root)
%doc README.MDV README.install.urpmi
%{_datadir}/festival/voices/finnish/suopuhe.common
%dir %{_datadir}/festival/voices/finnish


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0g-20051204.4mdv2011.0
+ Revision: 618267
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0g-20051204.3mdv2010.0
+ Revision: 428716
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0g-20051204.2mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Anssi Hannula <anssi@mandriva.org> 1.0g-20051204.2mdv2008.0
+ Revision: 77423
- add documentation from Debian
- fix a function name (P1 from Debian)
- add Suggests to festvox-suopuhe-common for better festival behaviour


* Sun Aug 06 2006 Anssi Hannula <anssi@mandriva.org> 1.0g-20051204.1mdv2007.0
- initial Mandriva release

