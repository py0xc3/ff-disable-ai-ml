# ff-disable-ai-ml
Disable AI/ML features in FF, and keep "disabled feature" list updated against current FF versions

# Environment
This is intended to be packaged as `rpm` for Fedora or its interwoven downstream distributions (CentOS Stream, AlmaLinux, RockyLinux) and used in conjunction with that distribution's default Firefox build. It is assumed this package is kept updated through an update repository that is aligned with the distribution's default Firefox build (default repo or epel).

**Only Fedora has been tested at this time.**

# Description 
By default, Firefox enables certain AI and ML preferences. The "Block AI" option in the settings does not disable them but only hide them. This means, users must disable these preferences manually in about:config and thus know what they are doing. At the same time, there are many AI/ML settings, which over time could change: this forces users to monitor and maintain their settings themselves if they do not want AI/ML enabled. This package will disable AI/ML preferences automatically and if Firefox changes its AI/ML preferences over time, the package can auto-update the preferences in order to keep AI/ML disabled for users who want it that way.

**Note:**

When the "Block AI" option is updated to disable AI features (patched in Fedora's build or upstream), this package is intended to be obsoleted but it is aimed to set the "Block AI" option to disabled during the package's removal (if the removal takes place through obsoleting during an update) in order to retain the known user preference that the user expects. 

Changes about this will be aligned with downstream (CentOS Stream, Alma, Rocky).

# Implementation

This package uses Mozilla's [AutoConfig](https://support.mozilla.org/en-US/kb/customizing-firefox-using-autoconfig) to implement the disabling. Using `policies.json` is intentionally avoided to not accidentally delete/override user, admin or enterprise/organization policies and customizations: `policies.json` is not intended to be be owned by a separate package.

Disabling the AI features in Firefox by default will not be possible and this package is intended to be installed manually by the user/admin.
