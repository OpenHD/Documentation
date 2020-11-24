# Contributing

### Donations

Donations are handled through [OpenCollective](https://opencollective.com/openhd), a non-profit 501\(c\)\(6\) funding host.

You can make a single or monthly donation of any amount.

100% of donations are used for hardware purchases to ensure team members have access to the SBCs, cameras, and radios they need to help work on the project.

### Contributing to Open.HD

The Open.HD project uses git to manage the source code used to build Raspberry Pi images, as well as companion apps for desktops and smartphones.

### Repositories

There are several repositories for different parts of the Open.HD system.

* [OpenHD/Open.HD](https://github.com/OpenHD/Open.HD), the main repository containing the custom code for sending/receiving video, telemetry, and RC control data
* [OpenHD/Open.HD\_Image\_Builder](https://github.com/OpenHD/Open.HD_Image_Builder), the repository containing the scripts used to build air/ground images for the Raspberry Pi
* [OpenHD/QOpenHD](https://github.com/OpenHD/QOpenHD), the new desktop/smartphone/ground station OSD and settings app

### Git

You don't need to be a git expert to work on Open.HD, but you should be familiar with the basics.

It is highly recommended to read through a Git tutorial and to use a Git GUI client, for example [Fork](https://git-fork.com/) \(_highly_ recommended, but Mac, Windows only\), [Github Desktop](https://desktop.github.com/) \(Mac, Windows, and community build for [Linux](https://github.com/shiftkey/desktop)\), or [SourceTree](https://www.sourcetreeapp.com/) \(Mac, Windows only\).

A GUI is not strictly required, but makes a lot of things _much_ easier, particularly if you need to see which commits are in a specific branch, or whether 2 branches have been merged yet. It also makes it much easier to create tags in a particular place in the repository history and "cherry-pick" specific commits into a separate branch, in order to create a pull request on Github.

A Git GUI can also automate the process of "logging in" to your Github fork whenever you push changes to it, without it you either need to setup SSH keys \(requires several steps, but not particularly complicated\), or enter your Github password every time you push changes back to Github.

This document will give instructions for the command line, because they can be used anywhere and the exact steps can be easily provided.

### Contributing a fix or feature

This is not intended to be a full guide to using Git \(it does not cover pulling changes from the upstream Open.HD repository, [merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging), [rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing), or other advanced concepts\), but it will walk through the steps needed to contribute a change or bugfix using the "feature branch" style workflow.

You should fork the [OpenHD/Open.HD](https://github.com/OpenHD/Open.HD) repository on Github _first_ before making any changes or cloning anything to your local machine, and then clone your fork rather than the main OpenHD/Open.HD repository. This ensures that the `origin` remote is pointing to your fork, which makes a lot of things easier if you're new to Git.

Once you have your own fork on Github, you can clone it to your local machine, replacing "username" with your Github username:

```text
$ git clone https://github.com/username/Open.HD.git
```

Note that when we clone a new repo from the Internet, Git will assign a new "remote" to the place it came from so that we can easily interact with it again.

By convention, the first remote is called "origin", so if you see references to "origin" later in this document, keep this in mind: it's just shorthand for referring to that particular remote repository on the Internet.

You can see the remotes registered in your local repository like this:

```text
$ git remote -v
origin	https://github.com/username/Open.HD.git (fetch)
origin	https://github.com/username/Open.HD.git (push)
```

**Make a new branch**

Before you start making any changes to the files, you should now create a new branch specifically for your changes.

If you are working on a fix for a bug affecting the airspeed display, you might create a branch called `fix_airspeed`. You should always keep unrelated changes in different branches so they can be tested separately and submitted to the main repository as individual "pull requests" on Github.

\(Once you're more familiar with Git, you can even switch back and forth between multiple branches on your machine in order to keep unrelated features or fixes separate from each other. This is particularly useful when one set of changes isn't quite done yet, you can "set it aside" in another branch and come back to it later.\)

Start by making sure you're in the master branch, which should be your starting point for any changes:

```text
$ git branch

 * master
   other_branch
 (END)
```

If not, checkout the master branch:

```text
$ git checkout master
```

Then create a new branch and check it out in one step \(the `-b` argument creates a new branch\):

```text
$ git checkout -b fix_airspeed
```

Now you can verify that you are in your new branch:

```text
$ git branch

 * fix_airspeed
   master
   other_branch
 (END)
```

Now make your changes to the files in the repository.

**Stage your changes**

Let's say we changed several lines in a file, and we want to see what changed before we continue.

```text
$ git status
On branch fix_airspeed
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   wifibroadcast-osd/render.c

no changes added to commit (use "git add" and/or "git commit -a")
```

We changed the `render.c` file, but we haven't yet _staged_ those changes.

Staging allows us to select which particular changes we want to commit right now, which makes it possible to commit things separately, even individual lines in a file. This is _significantly_ easier in a Git GUI, but for now all of our changes are in one file and they all go together, so we can stage all of our changes in that file:

```text
$ git add wifibroadcast-osd/render.c
```

Now `git status` should tell us that the file has been staged:

```text
$ git status
    On branch fix_airspeed
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
        modified:   wifibroadcast-osd/render.c
```

**Commit your changes**

Now we can commit those staged changes:

```text
$ git commit -m 'Fix airspeed in OSD'
    [fix_airspeed aa77948] Fix airspeed in OSD
     1 file changed, 13 insertions(+), 3 deletions(-)
```

The `-m` argument provides a commit message, and you should always use quotes around your message.

**Push to Github and open a pull request**

Now we can _push_ this change to our Github account:

```text
    $ git push origin fix_airspeed

    Enumerating objects: 9, done.
    Counting objects: 100% (9/9), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (5/5), done.
    Writing objects: 100% (5/5), 955 bytes | 955.00 KiB/s, done.
    Total 5 (delta 2), reused 0 (delta 0)
    remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
    remote: 
    remote: Create a pull request for 'fix_airspeed' on GitHub by visiting:
    remote:      https://github.com/username/Open.HD/pull/new/fix_airspeed
    remote: 
    To github.com:username/Open.HD.git
     * [new branch]      fix_airspeed -> fix_airspeed
```

Notice that our new branch has been created on Github as well, but in our own account.

Now we need to open a pull request, and Git has helpfully provided a link we can copy/paste \(or depending on the terminal you're using, click\).

In your pull request, make sure you describe what you changed, why it was needed, and the result of any testing you've done with those changes. If you need help building a new Raspberry Pi image that can be tested, ask in the [Telegram channel](https://t.me/OpenHD_HDFPV).

### Releases \(for those managing official releases\)

To make a new release, you just need to create a tag in your local Open.HD repo and push it to the `HD-Fpv/Open.HD` repository on Github.

In a Git GUI client, this very easy but how you do it will differ in each client. You can still follow the general steps below but use the GUI to do the same thing the commands do.

From the command line, you would need to do the following steps:

1. Make sure the local repo is in the state you want it. Check to make sure you're in the right branch \(run `git branch`\):

   ```text
    * master
    (END)
   ```

2. Make sure that you're tagging the commit you want to tag \(run `git log`, check the top commit\):

   ```text
    commit e868ff303a846793ae5cb9eab42c58b61db6321d
    Author: Luke <pilotnbr1@gmail.com>
    Date:   Sun Nov 24 17:56:44 2019 +0100

        rssirx.c with ant 0 and radiotap_rc

    commit feac7fd9cc7ff759f14249455799ef90b993894b
    Author: Luke <pilotnbr1@gmail.com>
    Date:   Thu Nov 21 22:59:26 2019 +0100
 
        Fix rssi dbm just showing best and better

        This is a bandaid fix some sane numbers... untested
   ```

3. Run `git tag -a -m '' 2.0.0rc1.2`, or whatever you would like the tag to be.
4. Check the tag to make sure it shows up where you expected, run `git log` and you should see your new tag on the most recent commit in parenthesis:

   ```text
    commit e868ff303a846793ae5cb9eab42c58b61db6321d (tag: 2.0.0rc1.2)
    Author: Luke <pilotnbr1@gmail.com>
    Date:   Sun Nov 24 17:56:44 2019 +0100
 
        rssirx.c with ant 0 and radiotap_rc
   ```

5. Push the new tag to the main repo on Github \(run `git push origin master --tags`\)

Keep in mind that this command will _also_ push any commits in your local `master` branch that are not already in the main repo on Github.

Once you have created a new tag, head over to the [Github Releases](https://github.com/OpenHD/Open.HD/releases) page and click "Draft a new release". You will be able to select your new tag at the top of the screen and enter any release notes or other information about the release in the box below it. You can refer to Issues that have been fixed/closed using the syntax `#1`, which automatically creates a link to issue 1. You can also just make a list and copy/paste any commit messages that outline changes/bugfixes.

You can then click the "Attach binaries" area and select any files you would like to be part of the release, such as SD card images or Android APK files.

