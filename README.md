Toast Chest
===========

This repository contains the source code for the **Toast Chest** application. The Toast Chest is a database of dinner/drinking toasts with a web-based front-end to get a toast on the go. An Alexa Skill is also available to bring the Toast Chest to your home (see link).

This application uses Django, Gunicorn, Nginx, and PostgreSQL. It also uses the Django REST API to create an endpoint that can be used to return a random toast to another application using JSON (/random.json). Docker and Docker Compose are used for easy setup.



Environment Setup
-----------------
1. Rename **.env-example** to **.env** and adjust variables as needed
2. Install Docker and Docker Compose
3. Run the following command to run a debug environment:
    ```
    docker-compose up
    ```

4. Run the following command for a production environment:
    ```
    docker-compose -f docker-compose.prod.yml up
    ```



Deploying on Heroku
-------------------
This project also has the necessary configuration to run on Heroku. You can deploy to Heroku by creating a new app and attaching a Postgres instance. You must also set the following Config Vars:

* DATABASE_URL (automatically set by Heroku)
* DJANGO_SETTINGS_MODULE=toast_chest.heroku (to force Heroku settings)
* SECRET_KEY (any key you want to use for Django)



License
-------
The material in this repository is released under a GNU General Public License v2.0.

Copyright (c) 2018.
