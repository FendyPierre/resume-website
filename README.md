
# Introduction

The goal of this project is to provide a website for me to host my resume and tell a  bit about me. 
It will continue to evolve over time.


### Main features

* Optional Notifications on user visit

* Models and fields for most texts, images, and elements

* Bootstrap static files included

* Separated requirements files


# Usage

Use this to deploy your custom resume website. 

# TODOs

* Add testing.
  
* Make Readme more descriptive.


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

Create superuser to login:

    $ python manage.py createsuperuser

Go to admin panel:

    /admin

Create a Profile object. Profile will be used to fill in many of the details such as profile photo, name etc..
Create different elements like Work Experience, Education, Projects.