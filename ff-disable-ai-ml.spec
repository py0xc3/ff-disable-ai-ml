Name:       ff-disable-ai-ml
Version:    0.1
Release:    %autorelease
Summary:    Disable all AI and ML preferences in Firefox
License:    MIT
URL:        https://github.com/py0xc3/ff-disable-ai-ml
Source0:    https://github.com/py0xc3/ff-disable-ai-ml/archive/refs/tags/v%{version}.tar.gz

Requires: firefox

BuildRequires: systemd-rpm-macros

%global mozappdir     %{_libdir}/firefox

%description
By default, Firefox enables certain AI and ML preferences.
The "Block AI" option in the settings does not disable them
but only hide them. This means, users must disable these
preferences manually in about:config and thus know what they
are doing. At the same time, there are many AI/ML settings,
which over time could change: this forces users to monitor
and maintain their settings themselves if they do not want
AI/ML enabled. This package will disable AI/ML preferences
automatically and if Firefox changes its AI/ML preferences
over time, the package can auto-update the preferences in
order to keep AI/ML disabled for users who want it that way.

%prep
%autosetup -n %{name}-%{version}

%build
#not applicable

%install
%make_install

%files
%license LICENSE
%{buildroot}%{mozappdir}/defaults/pref/autoconfig.js
%{buildroot}%{mozappdir}/ff_disable_ai_ml.cfg

%changelog
%autochangelog
