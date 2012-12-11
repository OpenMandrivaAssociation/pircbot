%define name	pircbot
%define version	1.5.0
%define release	%mkrel 1

Name:		%{name}
Summary:	Java IRC API
Version:	%{version}
Release:	%{release} 
Source0:	http://www.jibble.org/files/pircbot-1.5.0.zip
Source1:	pircbot.xml
URL:		http://www.jibble.org/pircbot.php

Group:		Development/Java
License:        GPLv2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ant
BuildRequires:	java-rpmbuild
BuildRequires:	unzip

Requires:	java

BuildArch:	noarch

%description
PircBot is a Java API for writing IRC bots quickly and easily. 
Its features include an event-driven architecture to handle common IRC events, 
flood protection, DCC resuming support, ident support, and more. 
Its comprehensive logfile format is suitable for use with pisg to generate 
channel statistics.

PircBot is written in pure Java, so it will run on any operating system that 
has a Java Virtual Machine.

%files
%defattr(-,root,root,-)
%_javadir/*.jar

#--------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for pircbot
Group:		Development/Java

%description javadoc
Javadoc for pircbot.


%files javadoc
%defattr(-,root,root,-)
%_javadocdir/*

#--------------------------------------------------------------------

%prep
%setup -q
%__cp %{SOURCE1} .

%build
export CLASSPATH="." 
%ant -f pircbot.xml all javadoc

%install
rm -rf $RPM_BUILD_ROOT

%__install -dm 755 $RPM_BUILD_ROOT%_javadir
%__install -m 644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%_javadir
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%_javadir/%{name}.jar

# javadoc
%__install -dm 755 $RPM_BUILD_ROOT%_javadocdir/%{name}-%{version}
pushd javadoc
cp -pr * $RPM_BUILD_ROOT%_javadocdir/%{name}-%{version}
popd
ln -s %{name}-%{version} $RPM_BUILD_ROOT%_javadocdir/%{name}

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Fri May 07 2010 Jonathan Bayle <mrhide@mandriva.org> 1.5.0-1mdv2011.0
+ Revision: 543074
- import pircbot


