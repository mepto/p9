# LITreview


## What it does

Allows authenticated users to create, edit, delete reviews on books, follow 
other users' reviews and comment


## How to install

### Clone the repository on your computer

`git clone https://github.com/mepto/p9.git`

### Python version

Make sure you use python 3.10. Check your python version:

`python --version`

### Virtual environment

Create and activate your virtual environment. The methodology below uses the venv module but you may use your favorite
 virtual environment instead.

* Creation from project root:

`python -m venv <your-virtual-env-name>` 
 
* Activation in Windows:

`<your-virtual-env-name>\Scripts\activate.bat`

* Activation in Linux:

`source <your-virtual-env-name>/bin/activate`

### Secret key

Create a .litreview.secret file in the settings folder and add a json 
dictionary with the SECRET_KEY for Django.

### Requirements

Install the required python packages with pip

`pip install -r requirements.txt`

### Database

The database is a sqlite3 database. One is provided with the project but 
should you wish to create your own, it should be named litreview.sqlite3 or 
the settings file updated locally accordingly.

If you create your own database, you will need to run the migrations.

`python manage.py migrate`

### Retrieve static files

`python manage.py collectstatic`

### Start server

`python manage.py runserver`

NB: If you experience issues when running the server, it might be because the 
PYTHONPATH is not properly declared. You need it to run your server in your 
virtual environment. This might easily happen if, when installing the python 
version, you didn't tick the "Add to Python <version> to PATH."
The following link may help you with adding it to you environment variables:
https://www.edureka.co/blog/add-python-to-path/

### Changes to the project

#### Frontend compilation

If you need to do changes to the scss files or javascript files for example, 
you will need to recompile the project. 

First, install the javascript dependencies. From the terminal, run

`npm install`

then

`npm run build`

#### Commits

The pre-commit package is there to make sure that checks such as imports and 
PEP8 are properly respected. After requirements are set, run

`pre-commit install`

You can also run the checks separate from commit by running

`pre-commit run --all-files`


## How to use

### Access

Users needs to register in order to access the website. Once registered, 
they can log in and start using the application. The page "My profile" 
displays the username and email for the account, as well as the avatar image 
selected. The logout button will disconnect the user.

### Followers and following users

The page "Followed users" will lets users follow others whose name they know.
It also displays the list of users followed, and the users following them.

### Feeds

The homepage displays the list of review requests from users followed and 
the users' own items. The "My posts" page displays only the items created by 
the user.

### Asking for a review

The "create a request ticket" button lets a user fill out a form with a 
title, a description and an image of the item for which they would like a 
review.

### Answering a request ticket

On ticket review requests, a "Submit review" button will open a form where 
the user will be able to add a headline, a description and a rating.

### Adding a review for a book whithout request

The "Create a review" button will let the user fill out a form where all the 
items for the review request and the actual review need to be filled out at 
once.

### Edition

The user can edit the review requests or review they have created, or delete 
them altogether. If a ticket for a review request is deleted, related 
reviews posted will be deleted as well.


## Possible future improvements

* User profile modification
* Profile deletion (needs assessment of consequences on tickets and reviews)
* Notifications for posts from followed users, reviews to user requests, 
  user account changes
