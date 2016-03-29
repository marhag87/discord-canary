Name:           discord-canary
Version:        0.0.1
Release:        1%{?dist}
Summary:        All-in-one voice and text chat

License:        Copyright only
URL:            https://discordapp.com
Source0:        https://storage.googleapis.com/discord-developer/test/%{name}-%{version}.tar.gz

# Don't build debug package
%define debug_package %{nil}

%define discorddir /opt/%{name}

%description
All-in-one voice and text chat for gamers that's free,
secure, and works on both your desktop and phone.

%prep
%setup -q -n "DiscordCanary"

%build

%install
install -p -d -m 0755 %{buildroot}%{discorddir}
mv * %{buildroot}%{discorddir}/
mkdir -p %{buildroot}%{_bindir}
ln -fs %{discorddir}/DiscordCanary %{buildroot}%{_bindir}/discord-canary

%files
%{discorddir}
%{_bindir}/discord-canary

%changelog
* Thu Mar 31 2016 Martin Hagstrom <marhag87@gmail.com> 0.0.1-1
- Initial release
