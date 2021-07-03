# Making a Release

In order to push to the cloudsmith package group that is NOT for testing you have to create a tag in github from a terminal. It cannot be a lightweight tag. Correct format is:  
`git tag -a 2.0.9 -m "2.0.9"`  
  
Other useful commands in terminal in git playing with tags:

* See if there is a match `git describe --exact-match HEAD`
* Push your new tag \(will also trigger the build in drone.io since its a commit\) `git push --tags`
* Delete a tag `git tag -d 2.0.9`

This way the package.sh script will see the tag in the git describe command and thus trigger a push to the appropriate directory.  
  
To pull the correct version of openhd you must define the version in the image builder stage 2  
`OPENHD_PACKAGES="openhd=2.0.9"`

