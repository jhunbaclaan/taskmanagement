# About TaskMaster
*TaskMaster* is an application created with the collaborative effort of Jhun Baclaan, Noel Ah Mook Sang, and Adriane Fiesta.
This application is a project for our CSCI-3911 class and is meant to be a demo of a web-based, user-friendly task management app.
# Concept
TaskMaster is developed using HTML/CSS, with implementation via Django. Django implementation means that there will be a local database that can be used to store
essential information like user info and task history. This makes it easier to keep track of what tasks you've already done, and it also means that you don't have to redo everything
if you accidentally close the app.
## Features
There will be multiple screens that a user can access. For example, one of these screens will be a task creation screen, which allows the user to create tasks and give each task
basic information like a title, description, and due date.

Tasks will have the following features:
- Creation & deletion
- Titles
- Due dates
- Categories & priority levels
- General, manually-written descriptions and notes
- Editable details
- Filtering
- Local storage and access

As more features are added, this section will be updated to match.
# Installation and Use
The installation and use of TaskMaster assumes that you have **basic** knowledge of
your system's Command Line/Terminal. **It also assumes that you have the latest version of python (or python3 on macOS) installed
on your system. If you do not have it installed, find their releases page [here](https://www.python.org/downloads/).**

The only release of TaskMaster can be found under (filename). Download it and unpack in a place that you can easily access.

After unpacking the .zip, navigate to its directory on your Command Line with 'cd'. Once you're at the base directory,
use the following command:
```
source venv/bin/activate
```
This will activate the venv, and allow you to run the app.

Running TaskMaster is equally as easy. After activating the venv, run the server with:
```
python manage.py runserver
```
Your command line will return a line along the lines of `Starting development server at...` alongside a URL. 
This URL can be copied and pasted into any browser to access TaskMaster. From here, you can add and manage your tasks as you'd like.
