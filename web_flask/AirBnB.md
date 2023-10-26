# AirBnB clone

![logo](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/logp.png)

I know you were waiting for it: it's here!

The AirBnB clone project starts now until... the end of the first year. The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/)

You won't implement all the features, only some of the them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database of files that store data (data=objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Final product

![fp1](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/final_prod1.png)

![fp2](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/final_prod2.png)

## Concepts to learn

* [Unittes](https://docs.python.org/3.4/library/unittest.html#module-unittest)-and please work all together on tests cases
* **Python packages** concept page
* Serialization/Deserialization
* <span style="color:red">**args, **kwargs*</span>
* <span style="color:red">*datetime*</span>
* More coming soon!

## Steps

You won't build this application all at once, but step by step.

Each step will link to a concept:

### The console

* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between "My object" and "How they are stored and persisted". This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won't have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

![The console](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/console.png)

### Web static
* learn HTML/CSS
* create the HTML of your application
* create template of each object

![web static](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/static.png)

### MySQL storage
* replace the file storage by a Database storage
* map your models to a table in database by using an O.R.M

![MySQL storage](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/storage.png)


### Web framework - templating
* create your first web server in Python
* make your static HTML file dynamic by using objects stored in a file or database

![templating](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/templating.png)


### RESTful API
* expose all your objects stored via a JSON web interface
* manipulate your objects nia a RESTful API

![RESTful API](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/restful_api.png)

### Web dynamic
* learn JQuery
* load objects from the client side by using your own RESTful API

![Web dynamic](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/dynamic.png)

## File and Directories


## Data diagram

![Data diagram](https://github.com/joshua-akuna/AirBnB_clone_v2/blob/main/web_flask/images/data.jpg)
