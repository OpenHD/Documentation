# The Open.HD Ecosystem

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


**Github, Docker, Drone.io, Cloudsmith & Co.**

Github is where all of our code is stored. "Master" branches are the new future 3.0 OpenHD and is unfinished. 2.0 branches are where the current working code resides.

For distribution Open.HD makes use of a build-pipeline in order to speed up the build process and automate some tasks that otherwise would have to be done via means of tedious manual commands.

The pipeline starts with Github repository \([Open.HD · GitHub](https://github.com/OpenHD)\).  
Once new code gets comitted/merged drone.io \([Drone.io](https://cloud.drone.io/)\), which is an "_Open source continuous integration platform built on Docker_" starts taking over. Drone.io uses configuration \*.yml files in each github repository and builds a package from a script, packaage.sh, found in the same github repository.

Drone.io if successful pushes the Open.HD packages to [cloudsmith](https://cloudsmith.io/repos/), which is a universal package management solution, allowing creation, storeage, and shareing ready to install Linux packages.

In summary, if you want to try new code you commit to github, it gets merged, docker builds it automatically with drone.io, new package appears in cloudsmith. Of course it is recommended you build on your local machine and test any code prior to committing to github.

{% hint style="info" %}
untagged commits go to "testing" cloudsmith packages only
{% endhint %}

{% hint style="info" %}
In the past, travis was also used to package openhd 2.0
{% endhint %}

