# ff-disable-ai-ml
Disable AI/ML features in FF, and keep "disabled feature" 
list updated against current FF versions

# Environment
This is intended to be packaged as `rpm` for Fedora or its
interwoven downstream distributions (CentOS Stream, AlmaLinux, 
RockyLinux) and used in conjunction with that distribution's 
default Firefox build. It is assumed this package is kept
updated through an update repository that is aligned with the
distribution's default Firefox build (default repo or epel).

**Only Fedora has been tested at this time.**

# Description 
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
