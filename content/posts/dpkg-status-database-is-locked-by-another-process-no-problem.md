Title: dpkg status database is locked by another process - no problem
Date: 2016-11-29 02:05
Author: mohanad
Category: GNULinux, howto
Tags: dpkg, locked
Slug: dpkg-status-database-is-locked-by-another-process-no-problem
Status: published

In case you got this nasty error when trying to install new package on Ubuntu/Debian:  
"dpkg status database is locked by another process",  
Then all you need to do is to run the following two commands in the terminal,

sudo rm /var/lib/dpkg/lock

sudo dpkg --configure -a

It worked perfectly with me,
