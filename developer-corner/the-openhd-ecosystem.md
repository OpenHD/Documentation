# The Open.HD Ecosystem

**Github, Docker, Drone.io, Cloudsmith & Co.**

Open.HD makes use of a sophisticated build-pipeline in order to speed up the build process and automate some tasks that otherwise would have to done via means of tedious manual work.   
  
The pipeline starts with Github repository \([Open.HD · GitHub](https://github.com/OpenHD)\).   
Once new code gets submitted/merged drone.io \([Drone.io](https://cloud.drone.io/)\), which is an "_Open source continuous integration platform built on Docker_" starts taking over. Docker automatically begins building via actions on github \(more info here: [drone-io-vs-github-actions](https://stackshare.io/stackups/drone-io-vs-github-actions)\).  

Drone.io if successful updates the Open.HD packages on [cloudsmith](https://cloudsmith.io/repos/), which is a universal package management solution, allowing to create, store and share ready to install Linux packages.

If you want to try new code you commit to github, it gets merged, docker builds it automatically with drone.io, new package appears in cloudsmith.

{% hint style="info" %}
For QOpenHD it is the 2.0-testing repo that gets updated
{% endhint %}

{% hint style="info" %}
In the past, travis was also used to package openhd 2.0
{% endhint %}

  






