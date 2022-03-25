# Flags Protoype Readme

IMPORTANT: new GitHub repository: https://github.com/danharrison73/Uniflags

Clone from GitHub

Firstly Google cloud SDK needs to be installed.

Then the cloud SQL proxy needs to be installed.
The download file can be found at:

https://dl.google.com/cloudsql/cloud_sql_proxy_x64.exe

Then you need to navigate to the same directory and run the following command:

    cloud_sql_proxy.exe -instances="ctf-group-project:us-central1:uniflags-instance"=tcp:3306

You then need to navigate to the folder /flags and run the following command:

    python manage.py runserver

It is also necessary to install and run both mySQL server client in order for the application to run.

## Deployment

In order to deploy this app, navigate to the same folder as manage.py in the project and run the following command
within the google cloud shell:

    gcloud app deploy


