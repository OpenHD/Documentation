# Contributing

### Donations

Donations are handled through [OpenCollective](https://opencollective.com/openhd), a non-profit 501\(c\)\(6\) funding host.

You can make a single or monthly donation of any amount.

100% of donations are used for hardware purchases to ensure team members have access to the SBCs, cameras and radios they need to help work on the project.

### Contributing to OpenHD

The OpenHD project uses Github to manage its source code.
The code is split into multiple repositories which itself have multiple branches.
Github is also used to build all packages and images.
Packages are hosted on Cloudsmith, which hosts and distributes packages for OpenHD.

### Contacting Developers

If you're interested in contributing to OpenHD, the easiest way is to join our [Telegram development channel](https://t.me/openhddev).
The core-development group is also doing weekly meetings on Discord. Those are not open for everyone, but occasionally we invite guests.
If you are interested in cooperating with OpenHD, just write us a message at: development@openhdfpv.org and we'll schedule a meeting.


### Repositories

There are several repositories for different parts of the OpenHD system.
The most important ones are:
* [OpenHD/Open.HD](https://github.com/OpenHD/Open.HD), the main software which handles all the features that are needed to run the OpenHD project.
* [OpenHD/QOpenHD](https://github.com/OpenHD/QOpenHD), the GUI/Configuator app which displays the video and OSD, but is also the UI for OpenHD.
* [OpenHD/Open.HD\_Image\_Builder](https://github.com/OpenHD/Open.HD_Image_Builder), the repository containing the script which builds all our images.
* [OpenHD/Open.HD\Kernel\_Builder](https://github.com/OpenHD/OpenHDKernelBuilder), the repository containing the script which builds all our kernels.

### Branches

The most stable code is hosted in #master.
New branches are made for major and minor releases. These are either a development snapshot for older versions like #2.0 or contain actively developed non-stable code like #2.2.3-evo, which isn't ready to be pushed into #master yet.
The lead developers usually use branches like "consti-test", "rapha-test",... to develop new features and fix bugs. Those branches are highly unstable, aren't ready for non-dev usage and can change rapidly.

### Contributing a fix or feature

This is not intended to be a full guide to using Github.

To start start developing/fixing bugs, you should fork the [OpenHD/Open.HD](https://github.com/OpenHD/Open.HD) repository on Github _first_ before making any changes or cloning anything to your local machine, and then clone your fork rather than the main OpenHD/Open.HD repository. 


**Make a new branch**

Before you start making any changes to the files, you should now create a new branch specifically for your changes.

If you are working on a fix for a bug affecting the airspeed display, you might create a branch called `fix_airspeed`. You should always keep unrelated changes in different branches so they can be tested separately and submitted to the main repository as individual pull requests on Github.

Now make your changes to the files in the repository.

**Comment and Document your changes**

When programming changes, please comment as much as possible. Our current goal is to have a highly docomented/commented code in order to make mods and changes easier in the future.


**Opening a pull request**

To finally merge your code into OpenHD you need to open a pull request.

In your pull request, make sure you describe what you changed, why it was needed and the result of any testing you've done with those changes. If you need help building a new image that can be tested, ask in the [Telegram development channel](https://t.me/openhddev).

