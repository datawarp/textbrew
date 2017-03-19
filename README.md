# textbrew

[![Join the chat at https://gitter.im/rishy/textbrew](https://badges.gitter.im/rishy/textbrew.svg)](https://gitter.im/rishy/textbrew?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Brew your raw text to a more structured and Machine Learning complaint format.

This README file contain all the information you need to start contributing to this repo. If you are still facing any difficulty with the code or setup then simply create an **Issue**.

## Contribution Guidelines

Fork this repository to your account, using the **Fork** button on the top right corner.

Use `git clone` to clone your forked repo to your local machine:
(replace 'your_username' with appropriate value)
```
git clone https://github.com/<your_username>/textbrew.git
```
<br>
`cd` into cloned repo:
```
cd textbrew
```

Obviously setting up SSH for interacting with github is a much more secure and hassle free way.
So, it is highly recommended that you setup ssh for Github using: [Setting up SSH - Github](https://help.github.com/articles/generating-ssh-keys/).

<br>
Set the `upstream` to this repo:

The easiest way is to use the https url:
```
git remote add upstream https://github.com/datawarp/textbrew.git
```

or if you have ssh set up you can use that url instead:
```
git remote add upstream git@github.com:datawarp/textbrew.git
```

<br>
Working branch for **textbrew** will always be the `develop` branch. Hence, all the latest code will always be on the *develop* branch.
You should always create a new branch for any new piece of work branching from *develop* branch:
```
git branch new_branch
```
**NOTE:** You must not mess with `master` branch or BAD THINGS will happen.
*master* branch contains the latest stable code, so just leave it be.

Before starting any new piece of work, move to *develop* branch:
```
git checkout develop
```
<br>
Now you can fetch latest changes from main repo using:
```
git fetch upstream
```
<br>
`merge` the latest code with *develop* branch:
```
git merge upstream/develop
```
<br>
`checkout` to your newly created branch:
```
git checkout new_branch
```
<br>
Rebase the code of *new_branch* from the code in *develop* branch, run the `rebase` command from your current branch:
```
git rebase develop
```
Now all your changes on your current branch will be based on the top of the changes in *develop* branch.

Push your changes to your forked repo
```
git push origin new_branch
```
<br>
Now, you can simply send the Pull Request to Parent Repo from within the Github.

## Installation:

For local development we suggest(requires [miniconda](http://conda.pydata.org/miniconda.html) installed):

* Install apt deps `sudo apt-get install build-essential python-dev git`(use `brew install build-essential python-dev git` on Mac OSX). 
* Create local environment - `conda create --name textbrew python=3.5`
* Activate local environment - `source activate textbrew`
* Install pip deps - `pip install -r requirements.txt`
* Download Spacy Models - `python -m spacy.en.download all`


## A note about Commit Messages:
* Commit messages shouldn't span for more than 7-8 words
* Commit messages should be meaningful and not something like - "made some changes", etc.
* Never use shorthand in commit messages
* If required add a few more words about your commit messages on Github Web Platform right before sending the pull request
* Each commit message should be structured as:
    <blockquote>(COMMIT_KEYWORD): COMMIT_MESSAGE_BODY<br><br>
Here, COMMIT_KEYWORD should take one of the values as given below - 
    1. module - after adding a new functionality/module in existing code
    2. init - for commiting some basic code structure file, for example during the start of a new project
    3. fix - for any bug fixes
    4. merge-conflict - if there was some merge conflict in the code that you just fixed</blockquote>

## Few more points to keep in mind:
1. Always fetch the code from upstream and rebase your current branch with it, before starting with any new work.
2. Create a new branch from develop branch for any new code, so that you don't end up breaking the previous code, and merge these changes back to the develop branch
3. It is always advisable to keep a separate "fixes" branch for bug fixes, branched out from "develop" branch
4. After every small and separate change in the code, commit it
5. Always squash up your commits into a single commit before sending the Pull Request or pushing the code. Use `git rebase -i` for this purpose. For example to squash last 3 commits into a single commit, simply run:
```
git rebase -i HEAD~3
```

Have a look at [Git-flow](http://nvie.com/posts/a-successful-git-branching-model/) for a structured way of working with Github.