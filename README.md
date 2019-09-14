# pyramid-surveymonkey-example
A boiler plate web app that connects to the SurveyMonkey v3 API

## Install Python 3.7 & pip
### Windows Instructions
Python 3.7 can be installed along with pip with one of the links below.
- [Windows x86](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe).
- [Windows x86-64](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe).

We'll want to add the `python` & `pip` commands to our `Path` variable.

   1. Open the `Environment Variables` window. On Windows 10 this can be done by searching `edit environment variables for your account` in the Start menu.
   1. Edit the `Path` variable either for the current User or the System.
   1. Add the full path to the folder containing `python.exe` to the beginning of the `Path` variable. For example, mine was located at `C:\Users\Scott\AppData\Local\Programs\Python\Python37-32`.
   1. Also add the full path to the folder containing `pip.exe` to the beginning of the `Path` variable. For example, mine was located in the same path as `python.exe` under the `Scripts` folder.
   1. Confirm the changes.
   1. Open up Command Prompt (`cmd` in Start menu) and type `python --version`, you should see `Python 3.7.0`.

**Note: Restarting the computer may be required for these changes to be recognized**

### Mac Instructions
Python 3.7 can be installed along with pip with one of the links below.
- [OS X 10.9 and up](https://www.python.org/ftp/python/3.7.0/python-3.7.0-macosx10.9.pkg).
- [OS X 10.6 and up](https://www.python.org/ftp/python/3.7.0/python-3.7.0-macosx10.6.pkg).

Open up Terminal and type `python3 --version`, you should see `Python 3.7.0`.

**Note: Mac OS usually comes with Python 2.7 preinstalled, so make sure to use the command `python3` to reference this version**

### What is Python 3.7?
Python is the programming language we're using with this example codebase. Python is an interpreted language, which means we need to install an interpreter to run our Python scripts. More information [here](https://www.python.org/doc/essays/blurb/).

### What is pip?
pip is a package management system used to install and manage software packages written in Python. This is similar to composer in PHP, NuGET in C#, npm in JavaScript...etc.

## Install virtualenv
### Windows Instructions
In Command Prompt, run `pip install virtualenv`.

### Mac Instructions
In Terminal, run `pip3 install virtualenv`.

### What is virtualenv?
virtualenv is a tool to create isolated Python environments. This is useful for keeping all the packages we install with `pip` in one project separated from the packages in another project. We can even use virtual environments to run different versions of Python from the one specified in the `Path`.

## Create & Activate a Virtual Environment
### Windows Instructions
   1. If you haven't already, clone this repo to the local machine.
   1. With Command Prompt, navigate to the root of this project and run `virtualenv pyenv`.
   1. Activate the virtual environment by running `pyenv\Scripts\activate` from the project root.
   1. `(pyenv)` should now be visible to the left of the command prompt.
   1. All future instructions should be followed from within this activated virtual environment.
   
### Mac Instructions
   1. If you haven't already, clone this repo to the local machine.
   1. With Terminal, navigate to the root of this project.
   1. Run `virtualenv --python==python3.7 pyenv`.
      1. If your terminal spits out something like `virtualenv: command not found` then in another tab locate where `virtualenv` is located. For example mine was located at `/Library/Frameworks/Python.framework/Versions/3.7/bin`.
      1. Run `/PATH/FROM/ABOVE/virtualenv --python==python3.7 pyenv`.
   1. Activate the virtual environment by running `source pyenv/bin/activate` from the project root.
   1. `(pyenv)` should now be visible to the left of the command prompt.
   1. All future instructions should be followed from within this activated virtual environment.

### What happened?
We've just created a virtual environment folder named `pyenv`. We've also activated the virtual environment, which means all future `python` & `pip` commands will be run in this isolated environment. So if we install a package using `pip` it'll be available to us when we use a Python shell, but it won't be available if we leave this environment or activate a different virtual environment where we haven't installed the package.

**NOTE: To leave a virtual environment, simply run `deactivate` from within the virtual enviroment.**

## Install Requirements
Run `pip install -e .`. This installs all the Python packages specified in the `setup.py` file.

## Run Waitress Server
Run `pserve development.ini --reload`. This will start a server that serves our application based on our configs in `development.ini`. We've specified that we want to use waitress as our server and serve our application on `localhost:8080`. The `--reload` command tells pserve to reload the application when it detects file changes. Additional configuration options for waitress are available [here](https://docs.pylonsproject.org/projects/waitress/en/latest/index.html).

**At this point, if you visit `localhost:8080` you should be greeted with a home page with a list of example pages. The SurveyMonkey API example won't work yet if you click that link. Follow the instructions below to make it work.**

## Setting up the SurveyMonkey API
There's two ways to use SurveyMonkey's API

1. For accessing your own SurveyMonkey account programmatically
1. For building an app that any SurveyMonkey account holder can use

For this example we're going to be focusing on option 1.

Visit the [developer portal](https://developer.surveymonkey.com/).

   - Click 'Get Started' and then either sign into your existing SurveyMonkey account or create a new one.
   - Click 'Create New App', give it a nickname and choose public.
   - Click on the 'SETTINGS' tab at the top of the page.
   - At the bottom of the SETTINGS page is the Scopes section. For now, enable 'View Surveys' by clicking on it. You can read more about scopes [here](https://developer.surveymonkey.com/api/v3/#scopes).
   - Locate your 'Access Token' on the SETTINGS page and copy it. Replace '\<your api key goes here\>' in `development.ini` with that value.
   - If you haven't created a survey yet in this account, go [here](https://www.surveymonkey.com) and create at least one.
   - Go to `localhost:8080/example/sm_api`. You should see a list of titles that match the survey(s) in your account.
