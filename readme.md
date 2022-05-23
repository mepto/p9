# LITreview

## What it does
Allows authenticated users to create, edit, delete reviews on books, follow 
other users' reviews and comment

#TODO: add that PYTHONPATH var must be added at the project root

## How to install
1. Clone the repository on your computer.

`git clone https://github.com/mepto/p9.git`

2. Make sure you use python 3.10. Check your python version:

`python --version`

3. Create and activate your virtual environment. The methodology below uses the venv module but you may use your favorite
 virtual environment instead.
* Creation from project root:

`python -m venv <your-virtual-env-name>` 
 
* Activation in Windows:

`<your-virtual-env-name>\Scripts\activate.bat`

* Activation in Linux:

`source <your-virtual-env-name>/bin/activate`


4. Secret key

Create a .litreview.secret file in the Settings folder and add a json 
dictionary with the SECRET_KEY for Django.

5. Install the dependencies with pip

`pip install -r requirements.txt`

6. Database

The database is a sqlite3 database. One is provided with the project but 
should you wish to create your own, it should be named litreview.sqlite3 or 
the settings file updated locally accordingly.

### Migrations

If you create your own database, you will need to run the migrations.

`python manage.py migrate`

## How to use

