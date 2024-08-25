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


---------------------------------------------------------------------------------------------------------------

# MVT

## **MVC Architecture**

- Most of the web frameworks implement the MVC (Model-View-Controller) architecture.
- The MVC design pattern separates the entire web application development process into three layers: [Model, View and Controller].

![image](https://github.com/user-attachments/assets/9321421c-37f7-40a9-aa4d-4d10ef62b3c4)


**In the MVC approach:**

- The controller intercepts the user requests. It coordinates with the view and model layers to send the appropriate response back to the client.
- The model is responsible for data definitions, processing logic and interaction with the backend database.
- The view is the presentation layer of the application. It takes care of the placement and formatting of the result and sends it to the controller, which in turn, redirects it to the client as the application's response.

## **MVT Architecture**

- The Django framework adapts a Model, View and Template (MVT) approach, a slight variation of the MVC approach.

![image](https://github.com/user-attachments/assets/57bb5cb2-5d4d-4f7e-9846-c36d3d56b393)


- The model is the data layer of the application.
- The view is, in fact, the layer that undertakes the processing logic.
- The template is the presentation layer.

**A Django application consists of the following components:**

- URL dispatcher
- View
- Model
- Template

### URL Dispatcher

- Url Dispatcher act as a controller in MVC approach.
- The **urls.py** module in the Django project's package folder acts as the dispatcher.
- When the server receives a request in the client URL, the dispatcher matches its pattern with the patterns available in the **urls.py**.
- It then routes the flow of the application toward its associated view.

### View

- The view function **reads the path, query, and body parameters included in the client's request** If required, it uses this data to interact with the models to perform CRUD operations.
- A view can be a user-defined function or a class.

### Model

- Python class.
- Django migrates the attributes of the model class to construct a database table of a matching structure.
- Django's Object Relational Mapper (ORM) helps perform CRUD operations in an object-oriented way instead of invoking SQL queries.

### Template

- It is a web page containing a mix of static HTML and Django Template Language code blocks.
- file.html
- Django's template processor uses any context data from the view inserted in these blocks to formulate a dynamic response.

<aside>
💡 **The view uses the client's and the model's data and renders its response using a template.**

</aside>

---

# Views

The primary role of the view function is to fetch the data from the client's request, apply a certain processing logic to it and send an appropriate response back to the client.

It receives the request data in an object of class **HttpRequest**. 

- Used to process HTTP request and HTTP response.
- In Django, a view is a function designed to handle a web request and return a web response. Each view function takes an HTTP Request object as its first parameter.

`def home(request):`

`content = “<html>hello world</html>”`

`return HTTPRespons(content)`

- Need to map view function to URL to get HTTP response. **THIS IS CALLED ROUTING.**
- Create [urls.py] file in app structure to route or map view functions with the urls.

![image](https://github.com/user-attachments/assets/028249df-cde0-45be-a163-d462d500f07d)


- The URL patterns list can contain multiple paths, and each path is created using the path function.
    - The function can accept arguments and two are acquired: [The first argument is the route, which is a string that contains a URL pattern - and the second argument is the view, which contains the relative path and the name of the view function].

- Django's URL dispatcher invokes a corresponding view function that matches the URL pattern.
- The view interacts with both the model and template layers.
- View interacts with Models (Structure of DB) in two ways:
    - 1 - Fetch objects from models.
    - 2 - Insert new instance to the model using the parameter which will create new record in the database.

# HTTP Request

- HTTP is the communication protocol you use to browse the internet.
- HTTP —> Hyper Text Transfer Protocol.
- It is Request-Response based protocol.
- Send data as plain text/html.

## Components of HTTP Request
![image](https://github.com/user-attachments/assets/b9e506f5-40d4-496a-b435-916885d6b0f2)

### Method
- It is the command that the user what to perform.
- Describes the type of action that the client wants to perform, and it communicates it to the server.
![image](https://github.com/user-attachments/assets/2dfbd5ba-708f-46b3-a112-eb98da831a93)

### HTTP Response

- Has similar format of http request + Status code which indicate request status.

### HTTPRequest and HTTPResponse in Django

- Django obtains the **HttpRequest** object from the context provided by the server.
- As a client request is received, Django’s URL dispatcher mechanism invokes a view that matches the URL pattern and passes this **HTTPRequest** object as the first argument so that all the request metadata is available to the view for processing.

> **Side Note to clarify:**
> 

View function always has its first argument(request).

عشان يقدر الURL DISPATCHER

 يطابق الREQUEST بالthe URL pattern and passes this **HTTPRequest** objectويبعت الداتا بتاعت الVIEW دا تحديدًا

```python
def home(request):
	body of the function
```

# HTTPS

- Secure version of HTTP.
- It is using encryption so that no one can access the request.
- Encrypted all data.

# URL

- Uniform Resource Locator.

## URL Components
![image](https://github.com/user-attachments/assets/a842c9ee-9fea-494c-9720-ef4c99ee8f3b)

- Scheme: Referred to HTTP or HTTPS.
- Domain consists of:
    - Second Level Domain (SLD): represent organization name like (little lemon in the example).
    - Top Domain: represent country or category (com - org - ie …etc).
- Parameter: Query string.

# Parameters

- The view function in Django is like any other Python function in that it receives its mandatory argument as the request object from the server context. The client may pass additional arguments via different methods.
- The parameter linked to the URL’s endpoint is called a **path** parameter.

  ![image](https://github.com/user-attachments/assets/265dcae0-5c55-4c04-869f-f2815b4bbc35)

  ![image](https://github.com/user-attachments/assets/3e72b672-07d8-40b6-adee-5ed1135d0cd6)

  ### Query Parameter

- A query string is a sequence of one or more **key=value** pairs concatenated by the **&** symbol. Each key is the query parameter. The query string ends with the **?** symbol after the URL endpoint.

> **Query strings are an alternative approach to URL parameters for adding URL configurations**
> 

---

> If you will pass parameter in the url, you should identify this para as argument in the view function that mapped with this url.
> 

```python
urlpattern=[
path(dishes/<str:dish>, views.menuitem),
]
```

```python
def menuitem(request, dish):
	items={'pasta':'pasta italian'}
	
	description = items[dish]
	return HTTPResponse (f"{dish}" + description) 
```

Django helps you design your custom url with dynamic parameters.

You can use regular expression in url.

### **URL Namespacing**

- The use of a namespace helps in resolving the same URL name in more than one app.
- this is a screenshot from [url.py]in app folder.

![Uploading image.png…]()





# How to use migrations

- Django’s migration is a version control system. Whenever you add a new model or effect changes in an existing model, you need to run the **makemigrations** command. It creates a script for making changes in the mapped table. Every time you run the **makemigrations** command and Django detects the changes, a script with its name and version number is created. To implement the changes according to the migration script, you need to run the **migrate** command.

![image](https://github.com/user-attachments/assets/17145bd1-c673-4ffd-bccd-95820e5b4880)

![image](https://github.com/user-attachments/assets/cf20e10b-2c5c-49d9-b991-62c1bfe78cdf)


# Object Relationship Mapping (ORM)

- The ORM layer maps a class to a table in a relational database, with its attributes matching the table's field structure.
- The ORM library lets you perform the database operations in an object-oriented way instead of executing raw SQL queries.
- Object Relational Mapping or ORM is the ability to create a SQL query using object-oriented programming language such as Python. This enables a quick turnaround time in fast production environments that need constant updates.
- A **QuerySet** represents a collection of objects from your database. It represents a **SELECT** query. To fetch all the objects, use the **all()** method of the Manager.


