# Building an Image

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


This is one of the first things any new comer to the developer side of the project will want to attempt. This image builder is really designed to distribute images. It takes a base image, downloads and installs packages we need (some our own and others from sources), then applies patches and other changes to suit our needs.

As of now in all repos “master” branch is referred to as 3.0 and is the new stuff. Branch “2.0” is the working current version of OpenHD for the pi as of this writing. In a few places (cloudsmith or maybe droneio) there are “2.1” references which again is the “new” 3.0

Instructions for build:\
`git clone https://github.com/OpenHD/Open.HD_Image_Builder.git`  \
`cd Open.HD_Image_Builder`  \
`git checkout 2.0`

`./build.sh pi buster 2.0.10`

NOTE for Master branch the build.sh is slightly different where you will have to go into another script and change the package target.\
In a text editor go to: `00-run-chroot.sh` This is NOT REQUIRED FOR 2.0 BRANCH

{% hint style="info" %}
Option
{% endhint %}

To change the target package of the build in 2.0 go to stage 2 of the builder and modify 00-run-chroot (only change the bright green fields)

![](<../.gitbook/assets/grafik (4) (1).png>)

The gpg signing key and links are found on cloudsmith with the package you are targeting\
Also change in that same script

![](../.gitbook/assets/grafik.png)
