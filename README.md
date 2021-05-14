# Human Resources Matching WebApp
Matching App for Human resource major in Computer Science. Recently, it is required to find out human resource effectively to start up at the company. This web-app can be used as matching app for IT human resource. By registering, you will get list of people registered in this web app which is sorted out by the recommendation system of the system.

# Environment Requirements
-	Python3 (Anaconda or Miniconda’s virtual environment is recommended)
-	Django3
-	Pillow (for dealing with Images)
-	Numpy (for dealing with internal recommendation algorithm)

# Usage
## Start Server
At the root directory of repository run:

```
python manage.py runserver
```

## Login as administrator
1.	After run server, go to __domain__/admin/, thin it will display login page.
2.	Input Username = **admin**, Password = **adminadmin**
3.	You will have a full access to the Web-app database.

## Login as a test user
1.	There are 25 test users prepared for you to understand and play with web-app function. Each username is test__number__, and password are __password__(name of the user is randomly generate Japanese name, sorry for not using English name).
2.	From __domain__/app/, you can login as test user.
3.	If you done with testing and understanding with function of the web-app, you can delete all the test user from User database by Admin privilege.

## Register a new people
1.	Go to __domain__app/register/, then, it will display a create user account page.
2.	By filling the form and register, it will redirect you to login page of the web-app. You need to login and complete the form for your personal profile and image uploading.
3.	After completing the task, you are able to use web-app

# Data Base Structure
## User
Built in User database is used for using django3’s default login system. This is the Primary table of the databases.
Important Fields:
-	Id (int)
-	Password (hashed)
-	Username (str)
-	Email (email)
-	First_name (str)
-	Last_name (str)
## Profile
One to one relationship with User record which is for managing Profile of the User.
Important Fields:
-	Owner (Foreign key, User)
-	Age (int)
-	Major (str)
-	Prog_langs (str)
-	Comment (str)
## Image
One to one relationship with User record which is for managing Profile Image Uploaded by User.
Important Fields:
-	Owner (Foreign key, User)
-	Image (path of the Image)
## Friend
Many to many relationship with User records which manage the friend list of the User.
Important Fields:
-	Owner (Foreign Key, User)
-	User (Foreign Key, User)

