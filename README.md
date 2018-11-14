Toast Chest
===========

This repository contains the source code for the **Toast Chest** application. The Toast Chest is a database of dinner/drinking toasts with a web-based front-end to get a toast on the go. An Alexa Skill is also available to bring the Toast Chest to your home (see link).

This application uses Django, Gunicorn, Nginx, and PostgreSQL. It also uses the Django REST API to create an endpoint that can be used to return a random toast to another application using JSON (/random.json). Docker and Docker Compose are used for easy setup.



Environment Setup
-----------------
1. Install Docker and Docker Compose
2. Run the following commands to run a debug environment:
    ```
    docker-compose run web python3 manage.py createsuperuser (if not created already)
    docker-compose up
    ```

3. Run the following commands for a production environment:
    ```
    docker-compose -f docker-compose.prod.yml run web python3 manage.py createsuperuser (if not created already)
    docker-compose -f docker-compose.prod.yml up
    ```



License
-------
The material in this repository is released under a GNU General Public License v2.0.

Copyright (c) 2018.