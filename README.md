# **Image Search Application**



## **Description:**

This is a MEAN stack web application which is used for Content Based Image Search and Retrieval with explanation for the retrieved images.

Technology involved:

## **Front end:**

##### Angular js, Typescript, HTML, CSS, Bootstrap

#### Node Libraries used:

1. "highcharts": "^8.1.0"
2. "highcharts-angular": "^2.4.0"  - Design Responsive charts

## Backend

##### Javascript, express, mongodb

#### Node Libraries used:

1. "cors": "^2.8.5" - Cross origin resource sharing.
2. "express": "^4.17.1" - Create backend api for CRUD operations.
3. "mongoose": "^5.9.10" - Responsible for Mongo DB connection.
4. "multer": "^1.4.2" - File upload and storage mechanisms.

## Pre - Requisites:

1. Node JS
2. Mongo DB (If we are running in local mongo database, currently our application is connected to mongo cloud database)

## Application Structure

The application contains two folders as shown below:

Frontend: User Interface design and service classes

Backend: Business logic and database connection

![](E:\OVGU\Sem2_Summer2020\Subjects\Project\Milestone_2\structure.PNG)

## To Run the Application in Local:

1. Clone the project into local directory.

2. Open the project folder consisting of the frontend and backend sub-folders  in any IDE ( E.g. Visual Studio Code).

3. Open a new terminal in Visual Studio Code, Terminal => New Terminal

4. Navigate to the frontend folder using the below command:

   ​	cd frontend

5. Run the following commands

   1. '**npm install**' command - For installing node dependencies which we described above.
   2. **ng build** - This will create build with in the **folder backend/public**

6. Navigate to the backend folder using the below command:

   ​	cd backend

7. Run the following commands

   1. '**npm install**' command - For installing node dependencies which we described above.
   2. **'nodemon app.js/ node app.js'** - Run one of these two commands, This starts our web application in the local host **port 8080**

8. Hit the link **[http://localhost:8080/](http://localhost:8080/)** from browser to access our web application.

## Functionalities:

1. On server start up, it is noted that a csv file **'outputFeature.csv'** is generated within the **backend folder**. This is the file generated for the Toy dataset present within the folder **backend/image_dir/Toyset** (Consisting of 10 images)

2. User can now upload an images clicking on browse button shown below :

   ![](E:\OVGU\Sem2_Summer2020\Subjects\Project\Milestone_2\UI.png)

3. On click of **Search button**, the following functionalities are performed:

   1. The query image feature vector **'queryFeature.csv'** is generated and is stored in the directory **backend/queryFeature.csv**
   2. The query image itself is stored in the directory **backend/images **so that it can be used effectively    for some purposes.
   3. Creates an entry for query image in collection **qimages** in Mongo DB. Currently, Mongo DB consists one database called **imagesearcher** along with two collections **qimages and rimages**.
      1. **qimages** - For storing query image metadata
      2. **rimages** - For storing repository image metadata
   4. Retrieves the top ten images based on Similarity scores

4. On click of **Explain button**, the following functionalities are performed:

   1. Displays the pie chart depicting the feature contribution based on the json object which is retrieved from the backend python script(**Feature.py**) 

   2. To track user clicks, we are persisting the repository image id into the corresponding query image as shown below:

      ![](E:\OVGU\Sem2_Summer2020\Subjects\Project\Milestone_2\mongodb.png)

   

## Notes:

1. Image repository is referenced in the following directory: **backend/image_dir/Toyset**

2. Currently, only Toyset image entries are created within the mongo db collection **rimages**. Once the entries are created for other dataset, the application can be used with different dataset.







