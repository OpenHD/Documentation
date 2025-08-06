# Change packet source on a Pi

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


In order to change where apt or apt-get pull the openhd packages \(to test a custom package for instance\) you might want to alter the package-repo path in: `/etc/apt/sources.list.d/openhd-2-0.list`

The default for 2.0.8 is:

![](https://lh3.googleusercontent.com/ZABfZTpmn_TJN561nkijWKKD-Ix2jaTAMKs0zZuGiKHzDl83qZ67eo9ZId8dWtVrS_Ne2byYesEg71Vos4yHc-agkRAZwZOO1mqp3lzVeLeOMwGPV1uQQi3JuQ4kqZe5w8J0wNhW)

Nano to the package list file and modify to the list you want. For Example "openhd-2-0-testing.list"

To clear out old key and avoiding the error associated with an unsigned repo… get the error key by doing `sudo apt-get update`  
`sudo gpg --keyserver dl.cloudsmith.io --recv-key F856E94C65F425D6`

Then  
`sudo apt-get upgrade openhd`

