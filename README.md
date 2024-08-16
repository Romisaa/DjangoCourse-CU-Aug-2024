# DjangoCourse---CU-Aug-2024
CU Aug 2024
<h1>Notes</h1>
1- 
![image](https://github.com/user-attachments/assets/6c79eda8-1de0-4695-8731-be4288c99e42)

2- 
![image](https://github.com/user-attachments/assets/012b4639-6f25-403f-bed5-152a214c3364)

3- 
![image](https://github.com/user-attachments/assets/0e8fc52e-0b94-449f-acb8-f6034df9b8b1)

4- 
![image](https://github.com/user-attachments/assets/a9167c64-d4cd-4c05-b842-9ee39fe7e22b)

5-
![image](https://github.com/user-attachments/assets/19b333e6-3574-44eb-9349-3e3424220d24)

6-
# Notes

# **Project Structure**

- A Django project is a Python package containing the database configuration used by various sub-modules (Django calls them apps) and other Django-specific settings.
- Django project is representation for the entire web app project.

![Diagram represent what is the project vs app](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/c7391f09-aa69-48b9-8af4-5b935163bd08/9dea69cc-48d2-445d-8cf5-eb0d272ca460.png)

Diagram represent what is the project vs app

- After installing Django, You work with `django-admin` to use admin commands.

To start build your first project, run:

```python
django-admin startproject projectname
```

My Project Name is **(LimonRestProject).**

This is the structure file in the project folder that created by run `startproject`command.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/0c721f93-5b23-4cdc-80c0-c4d97ec76633/Untitled.png)

The **`manage.py`** script has the same role as the **`django-admin`** utility.

You can use it to perform various administrative tasks. In that sense, it is a local copy of the **`django-admin`** utility.

 using **`manage.py`** is more straightforward.

**The general usage of** **`manage.py --> python manage.py <command>`**

To start building your apps, you need to run command to create your first app:

```python
python manage.py startapp <name of app>
```

# **Project package**

**`startproject`command working on the following:**

- Create new folder with the Project name (The Parent Folder).
- Create inside this folder another folder (The Child Folder) with the project name + [`manage.py](http://manage.py).` file.
- The Child folder contains some files .py.
- The Child folder treated as Python Package so it must have **`__init__.py`**. file.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/43a446bd-869f-4019-98eb-51e167ba5bad/Untitled.png)

## [Settings.py](http://Settings.py) File

This file defines the attributes that influence the function of a Django application. The **startproject** template assigns some default values to these attributes.

### **INSTALLED_APPS**

list of strings represents the path of apps inside the project.

This list must be updated by adding its name whenever a new app is installed.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/bf16520d-75e7-42ce-bdff-8e1864be4970/Untitled.png)

### **Databases**

This attribute is a dictionary that specifies the configuration of one or more databases to be used by the current Django application. 

By default, Django uses the SQLite database.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/8204588a-29ea-4220-92e9-4dafedc03065/Untitled.png)

### **DEBUG = True**

By default, the development server runs in debug mode. This helps develop the application as the server picks up changes in the code and the output can be refreshed without restarting.

### **ALLOWED HOSTS**

This attribute is a list of strings. By default, it is empty. Each string represents the fully qualified host/domain where this Django site can be served. For example, to make the site running on localhost externally visible, you may add 0.0.0.0:8000 to this list.

### **ROOT_URLCONF**

This setting is a string pointing toward the [urls.py](http://urls.py/) module in which the project’s URL patterns are found. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/abc37c20-ca7e-40e1-96b2-41913f5ab752/Untitled.png)

### **STATIC_URL**

This setting points to the folder where the static files, such as JavaScript code, CSS files and images, are placed.

---

**NOTE:** to run development server means you run commands like `startproject`command and [`manage.py](http://manage.py) runserver` command.

---

# App Structure

- Django project contains one or more sub-modules called APPS.
- An app is responsible for performing one single task so that you can easily reuse this app inside other projects.
- When run `python [manage.py](http://manage.py) startapp AppOne` a folder with the app name created in the parent folder with files.py. inside the app folder.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/6e65a64d-057f-414c-a855-c58a5f301545/Untitled.png)

## Views.py

- A view is a user-defined function that’s called when Django’s URL dispatcher identifies the client’s request URL and matches it with a URL pattern defined in the [urls.py](http://urls.py/) file.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/a7a2ab61-227c-42fd-a9d6-94e2a1d9bf9a/Untitled.png)

- by adding index routing to url file in the app, the view of the django will be a white screen with “Hello” word.
- {{ A view is to output text..etc to a user}}.

## urls.py

- **The project package has a file of this name** that defines the URL patterns for the project.
- **You need to create a file with the same name in the app structure.**
- **the urls.py** **file can be configured at both the project and app level.**

Steps to define urls in project and app:

1- You create [URLs.py](http://URLs.py) file in App folder.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/2de48d7e-e500-4ea7-b38b-220ec052e591/Untitled.png)

2- Implement view function in [views.py](http://views.py) file in the app.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/729926c9-af70-43b1-9509-b8a9f889bd7a/Untitled.png)

3- Create your urlpattern inside URLs file in App folder with view function name.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/8d6903a1-1e97-4c3e-b81d-4ebca8d50792/Untitled.png)

4- Insert urlpattern of the app in URLs file in the project folder.

![We should import include from django.urls import include](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/5ab8ddda-c269-4a45-8a6c-e12632a29a37/Untitled.png)

We should import include from django.urls import include

**NOTE:** You can implement or map your app url directly in the url file in the project.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/982e373b-430b-4bc9-b3db-d40311e990b6/f77a74b3-a6ea-4f9d-a32c-eb2be6ebfea2/Untitled.png)

**`name=’home’` is like an attribute used for naming the URL patterns which can be useful sometimes.** 

## Models.py

- It represents Python classes inside the app.
- All the models present here are migrated to the database tables.
- Class based on **django.db.modelsclass.**

## Tests.py

- to implement tests that will run with the app.




