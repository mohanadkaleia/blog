Title: Install Quartus || 10.0 on UBUNTU
Date: 2012-10-28 14:56
Author: admin
Category: Application, GNULinux
Slug: install-quartus-10-0-on-ubuntu
Status: published

Hi

to install quartus \|\| 10.0 you will maybe face some problems during installation ..

Apparently there is a conflict with the file libX11.so.6. Here is a simple workaround:

-   Add the option --confirm to execute the install script.

```{=html}
<!-- -->
```
    sh altera_installer.external.sh --confirm
    Creating directory bin
    Verifying archive integrity... All good.
    About to extract 49568 KB in bin ... Proceed ? [Y/n] Y
    Uncompressing Altera Installer............................................................................................................................
    OK to execute: ./altera_installer_gui --gui  ? [Y/n]

-   Before proceeding, in another terminal, go in the same directory than the install script and delete the file ./bin/libX11.so.6.

```{=html}
<!-- -->
```
    rm bin/libX11.so.6

-   Now you can proceed.

```{=html}
<!-- -->
```
    OK to execute: ./altera_installer_gui --gui  ? [Y/n] Y
    Fontconfig error: "conf.d", line 1: no element found
    Fontconfig warning: line 73: unknown element "cachedir"
    Fontconfig warning: line 74: unknown element "cachedir"

-   The installer GUI should pop up.

That's it :) enjoy quartus bye

source :

http://fpga4u.epfl.ch/wiki/Install\_Quartus\_II\#Download\_the\_Installer\_2

http://ubuntuforums.org/showthread.php?t=1616509

//for modelSim installation follow this page

http://www.philpem.me.uk/elec/fpga/quartus-ubuntu/
