# django-imager

**Authors**: Steven Starwalt, Shannon Tully

**Version**: 1.0.2

## Overview
A site that hosts images

## Getting Started
*  Project-specific env variables
* `export SECRET_KEY='secret key'`
* `export DEBUG=True`
* `export DB_NAME='imager'`
* `export DB_USER=''` set these two if need for linux
* `export DB_PASSWORD=''`
* `export DB_HOST='localhost'` 

### initalize and run server
* `dropdb $DB_NAME`
* `createdb $DB_NAME`
* `./manage.py makemigrations`
* `./manage.py migrate`
* `./manage.py check`
* `./manage.py test`
* `./manage.py runserver`

### Routes
* Home
* Admin
* Login
* Register
* logout
* Activate


### Requirements
- Python

## Architecture
This app is written using Python 3.6.4 and Django framework, for full environmental requirements check requirements.txt

## Change Log
- 23 April 2018 - Start, Added git ignore, added ENV, django and req.txt, added factory.Faker. new requirements.txt, added tests for proper responses. version 1.0.0

- 24 April 2018 - added code for registration and django registration, new requirements.txt, added static css SMACSS file system and started styling, added image for the home page, new tests for registration. version 1.0.1

- 25 April 2018 - added imager_images app, added Album and Photo models, MEDIA folder with an images folder, added sorl.thumbnail & pillow, new requirements.txt, added tests for the imager_images app. version 1.0.2
