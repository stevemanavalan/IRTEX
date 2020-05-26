# IRTEX
There are two folders- 'frontend' and 'backend'

Currently we have build the frontend code into backend/public folder. So that only backend folder is enough for running the application in local. In case of any modifications in frontend,we will have to take the frontend code and build it again.

Pre requisites:

1. Node JS
2. Mongo DB (If we are running in local mongo database, currently our application is connected to mongo cloud database)

To run the application in local:

1. Clone the project into local directory.
2. Open the project folder in any IDE(E.g. Visual Studio Code) and open a new terminal.
3. Navigate to backend folder and run the following commands:
4. Run 'npm install' command and wait for node modules to get installed
5. To start the application, run nodemon app.js or node app.js
6. Server will be started in localhost:8080 by default.
7. Hit the url http://localhost:8080/ from browser to access web applciation.

Note: Image repository is referenced within the folder in the following location: backend/image_dir/Toyset In case image directory has to be changed, backend source code has to be changed in two places in app.js. Otherwise copy the images into Toyset folder and run the application.
