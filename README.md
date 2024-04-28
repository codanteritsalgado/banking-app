# Banking App
Welcome to the Learning Example App! This project serves as a sandbox for exploring different frontend frameworks integrated with a Django backend to build RESTful APIs. Please note that this is a non-commercial project created solely for educational purposes.

## Purpose
The primary goal of this project is to facilitate learning by implementing the same functionality across various frontend frameworks. By building a Django backend as a REST API and integrating it with multiple frontend frameworks such as React, Angular, and Vue, developers can gain insights into the strengths and weaknesses of each framework and how they interact with backend systems.

### Disclaimer
It's important to clarify that this project is not intended for commercial use, and there are no plans to monetize it or attract real users. Any code, features, or functionalities implemented within this project are solely for educational and demonstrative purposes.

### License
This project is licensed under the MIT License, which permits unrestricted use, distribution, and modification for educational and non-commercial purposes.

# Getting Started
To get started with this project, please create your own branch for making changes or aditions and once you're satisfied with your changes, make a pull request.

1. In order to setup your REST API, you need to navigate to the "/backend" folder
2. Once there you can run a command with docker-compose or use the docker plugin for visual studio
    - Using the plugin: right click on the `docker-compose.yml` and click on `Compose Up`
    - Using terminal: run `docker-compose up -d` this will run both images on the background, same as visual studio.
3. Now the virtual machines are working, run `docker ps` to show the instance's data, search the instance called `django`, sometimes it's called something like `backend_django_1`
4. use the following terminal code to access the backend SSH `docker exec -it DJANGO_INSTANCE_NAME /bin/sh`
5. Once you're inside the backend instance, let's run some migrations..! run: 
    - `python manage.py makemigrations`
    - `python manage.py migrate`
6. You're good to go! now you can test the available endpoints.

### Storage Folder
In this section you'll find access to a Google Drive folder, this will contain all the elements required for creating a new brand, including the brand's identity pdf 

https://drive.google.com/drive/folders/1_hQUVcf73VCGgjq2tWB3eWpPrG0yCzlV?usp=sharing