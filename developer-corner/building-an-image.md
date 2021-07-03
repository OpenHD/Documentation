# Building an Image

As of now in all repos “master” branch is referred to as 3.0 and is the new stuff. Branch “2.0” is the working current version of OpenHD for the pi as of this writing. In a few places \(cloudsmith or maybe droneio\) there are “2.1” references which again is the “new” 3.0   
  
Instructions for build:  
`git clone https://github.com/OpenHD/Open.HD_Image_Builder.git  
cd Open.HD_Image_Builder  
git checkout 2.0`  
  
Now you have to modify one line within the image builder code to reflect the build you want...   
In a text editor go to: `/Open.HD_Image_Builder/stages/02-Packages/00-run-chroot.sh`  
  
Change this line to:  
`OPENHD_PACKAGES="openhd=2.0.10"`  
  
now in a console/terminal /Open.HD\_Image\_Builder  
`./build.sh pi buster`  


{% hint style="info" %}
Option
{% endhint %}

To change the target package of the build in 2.0 go to stage 2 of the builder and modify 00-run-chroot \(only change the bright green fields\)  


![](../.gitbook/assets/grafik%20%281%29.png)

The gpg signing key and links are found on cloudsmith with the package you are targeting  
Also change in that same script

![](../.gitbook/assets/grafik.png)

