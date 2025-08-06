# QOpenhd Tips

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


**Custom Mavlink**

Make modifications to definitions xml file for mavlink. From there run mavlink generator script. In generator choose c+. I also deselected validate because it would see enum errors otherwise

**QT and Android Integration**

Install android studio Install dependencies:&#x20;

`sudo apt-get install libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386`&#x20;

`sudo apt-get install libsdl1.2debian:i386 Go get jdk 11 and note location`

In QT creator go to manage kits, then devices, then android.

\-Browse to  jdk location

\-setup sdk&#x20;

\-select to download openssl

To debug on phone enable developer options (usually tap build number 7 times)&#x20;

\-Enable “usb debugging” on phone&#x20;

\-Give permission when you plug phone into computer via usb

&#x20;Now when you build in QT and your phone is connected the app will launch in debug mode on your phone.
