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
1.	Go to __domain__/app/register/, then, it will display a create user account page.
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

**※ In this web-app, Friend is one directional relationship**

# URL page structure and its functions
## __domain__/app/register
-	Register a new people. After registering, it will redirect you to the login page of the web-app to complete the Profile and Uploading Image.
## __domain__/app
-	Login is required (if you are not logged in, it will redirect you to login page)
-	Shows list of recommended lists of people. You can click “Profile” to see their Profile (will be redirect to their profile page).
-	People already added as you friend will not appear in this list.
## __domin__/app/profile/__id__(id is number of User id)
-	Can view your Profile if you visit this page from “Your Profile” menu above the page. If it is your Profile, you can change your profile and image.
-	If it is other people’s profile, and you are not yet added them as friend, you will be able to add the person as friend. After adding, you will redirect to friend list page.
-	**The email of the other people will be shown only if you and the person is mutually added opponent as friend.**
## __domain__/app/friends
-	Show your friend list (even if the person did not add you as friend, you can see them in this list if you added them).
-	You can click “Profile” to see their Profile.
-	You can click “Delete” to delete the person from your friends list.
## __domain__/app/friends_request
-	Show people added you as friend, but you did not add as friend.
-	You can click “Profile” to jump to their Profile page and ad them as friends.
## __domain__/app/find
-	By input Keyword in Search box, you can search specific user in the system.
-	Search result will be shown as list, and you can click “Profile” to jump to their Profile
-	Unfortunately, the Search function is not very powerful. It can only accept one key word, and can not do AND OR search. This is because the main purpose of this web-app is recommendation, not SNS like function. SQL search input was considered, but due to avoid SQL injection, it is denied.

# Recommendation Algorithm
-	Since this project is just prototype, it did not support complex recommendation system like algorithm using past history of user-friend matrix, etc.
-	For recommendation, **Cosine Similarity** is used.
-	Converting content of Profile as Vector, Users can be represented as Vectors. Algorithm calculates Cosine Similarity between login user and other users in system, and return sorted user based on this similarity.
-	People with high similarity will be sorted to the top of the recommendation list in this web-app.

# Note
-	There is no function for automatically delete the unnecessary image in img file. Which means, this web-app continue to hold previous image even if user updated their Profile picture. Automatic process which deletes the unnecessary images from folder periodically will be needed to be implemented. 
-	Due to problem of **Curse of dimensionality**, if the vector extracted from user Profile is **Sparse Vector**, the accuracy of the recommendation algorithm will decline. To solve this problem, classic approach uses **PCA(Principle Component Analysis)**. In addition, adding another metric for recommendation will help it too.
-	**Do not just clone and deploy this online!! There is many Security Problems (e.g. Secret_Key is revealed in setting.py).**

# License
LGPL (GNU Lesser General Public License)
