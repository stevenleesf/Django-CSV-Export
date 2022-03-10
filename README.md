# Django-CSV-Export

## Project Description
<br />

This repository provided a simple solution for you to export data from database into CSV file.

<br />

## How to Install the Project
<br />

1. You need to have Python installed in your machine (3.8 or higher is recommended);

2. Create a new folder in your machine, go inside it and clone this repository. 
<span style="margin-left: 25px;">```git clone https://github.com/stevenleesf/Django-CSV-Export.git```</span> 

3. Install the required Python modules (`django`):
<span style="margin-left: 25px;">```pip install -r requirements.txt```</span>

<br />

## Using a clean database
<br />
1. Delete db.sqlite3 from the folder

2. Run `python manage.py makemigrations` and `python manage.py migrate` to create the necessary tables in the database;

3. Run `python manage.py createsuperuser` to create a super user to access to the admin panel

** I have include the database for easier access for you to test the function in the website
<br />
username : admin
<br />
password : admin
<br />

## How to Use the Project
<br /> 

1. Start the local server with `python manage.py runserver`. 8000 is the default port used by Django;

2. On your browser, access the address http://localhost:8000;

3. Explore the posts funcionalities: 

* list all posts;
* list details from one post;
* create a new post; 
* update and delete a post.
* export list of post into CSV

<br />

