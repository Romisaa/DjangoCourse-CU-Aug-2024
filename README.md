# DjangoCourse---CU-Aug-2024
CU Aug 2024
<h1>Notes</h1>

# **Project Structure**

- A Django project is a Python package containing the database configuration used by various sub-modules (Django calls them apps) and other Django-specific settings.
- Django project is representation for the entire web app project.

![image](https://github.com/user-attachments/assets/b1f8fed5-f251-45e5-bcb9-1f9a1fdb665a) 

                      Caption: Diagram represent what is the project vs app

- After installing Django, You work with `django-admin` to use admin commands.

To start build your first project, run:

```
django-admin startproject projectname
```

My Project Name is **(LimonRestProject).**

This is the structure file in the project folder that created by run `startproject`command.

![image](https://github.com/user-attachments/assets/3c21a35d-7cca-4f40-9345-3e74b6b492b8)


The **`manage.py`** script has the same role as the **`django-admin`** utility.

You can use it to perform various administrative tasks. In that sense, it is a local copy of the **`django-admin`** utility.

 using **`manage.py`** is more straightforward.

**The general usage of** **`manage.py --> python manage.py <command>`**

To start building your apps, you need to run command to create your first app:

```
python manage.py startapp <name of app>
```

# **Project package**

**`startproject`command working on the following:**

- Create new folder with the Project name (The Parent Folder).
- Create inside this folder another folder (The Child Folder) with the project name + [`manage.py](http://manage.py).` file.
- The Child folder contains some files .py.
- The Child folder treated as Python Package so it must have **`__init__.py`**. file.

![image](https://github.com/user-attachments/assets/caa61a73-204a-41f7-8f89-8ba50155d878)


## [Settings.py]File

This file defines the attributes that influence the function of a Django application. The **startproject** template assigns some default values to these attributes.

### **INSTALLED_APPS**

list of strings represents the path of apps inside the project.

This list must be updated by adding its name whenever a new app is installed.

![image](https://github.com/user-attachments/assets/492eeebe-9e5a-417f-a621-12dd326a9d22)


### **Databases**

This attribute is a dictionary that specifies the configuration of one or more databases to be used by the current Django application. 

By default, Django uses the SQLite database.

![image](https://github.com/user-attachments/assets/f50e3e0c-333f-40c9-8527-86c678af86bd)


### **DEBUG = True**

By default, the development server runs in debug mode. This helps develop the application as the server picks up changes in the code and the output can be refreshed without restarting.

### **ALLOWED HOSTS**

This attribute is a list of strings. By default, it is empty. Each string represents the fully qualified host/domain where this Django site can be served. For example, to make the site running on localhost externally visible, you may add 0.0.0.0:8000 to this list.

### **ROOT_URLCONF**

This setting is a string pointing toward the [urls.py](http://urls.py/) module in which the project’s URL patterns are found. 

![image](https://github.com/user-attachments/assets/f1be0a43-e0d2-4cbe-8f4f-95503078b30b)


### **STATIC_URL**

This setting points to the folder where the static files, such as JavaScript code, CSS files and images, are placed.

---

**NOTE:** to run development server means you run commands like `startproject`command and [`manage.py](http://manage.py) runserver` command.

---

# App Structure

- Django project contains one or more sub-modules called APPS.
- An app is responsible for performing one single task so that you can easily reuse this app inside other projects.
- When run `python [manage.py](http://manage.py) startapp AppOne` a folder with the app name created in the parent folder with files.py. inside the app folder.

![image](https://github.com/user-attachments/assets/57707522-3bc6-467e-8b45-7f0116573aa8)


## Views.py

- A view is a user-defined function that’s called when Django’s URL dispatcher identifies the client’s request URL and matches it with a URL pattern defined in the [urls.py] file.

![image](https://github.com/user-attachments/assets/88dbce7c-a14d-4642-9011-0276f166dcc8)


- by adding index routing to url file in the app, the view of the django will be a white screen with “Hello” word.
- {{ A view is to output text..etc to a user}}.

## urls.py

- **The project package has a file of this name** that defines the URL patterns for the project.
- **You need to create a file with the same name in the app structure.**
- **the urls.py** **file can be configured at both the project and app level.**

Steps to define urls in project and app:

1- You create [URLs.py]file in App folder.

![image](https://github.com/user-attachments/assets/d1602c1f-b03d-4d32-ad5c-fd03d753de76)


2- Implement view function in [views.py] file in the app.

![image](https://github.com/user-attachments/assets/bcc58b14-23e9-4e84-9194-e583ed8ab8e0)


3- Create your urlpattern inside URLs file in App folder with view function name.

![image](https://github.com/user-attachments/assets/a08796e6-3af9-4296-a949-53d1b53128b7)


4- Insert urlpattern of the app in URLs file in the project folder.

![image](https://github.com/user-attachments/assets/88eba4df-cf08-46a7-b423-c68b5bfc03e4)



We should import include from django.urls import include

**NOTE:** You can implement or map your app url directly in the url file in the project.

![image](https://github.com/user-attachments/assets/de088ee1-f986-4096-bc0c-b570c9d81ff1)


**`name=’home’` is like an attribute used for naming the URL patterns which can be useful sometimes.** 

## Models.py

- It represents Python classes inside the app.
- All the models present here are migrated to the database tables.
- Class based on **django.db.modelsclass.**

## Tests.py

- to implement tests that will run with the app.




