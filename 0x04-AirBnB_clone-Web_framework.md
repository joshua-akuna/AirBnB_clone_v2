# 0x04. AirBnB clone - Wb framework

### Concepts
* [AirBnB clone]()

## Resources
##### Read or watch:
* [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
* [A Minimal Application](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application)
* [Routing](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing) (except "HTTP Methods")
* [Rendering Templates](https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates)
* [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
* [variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
* [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
* [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
* [List of Control Structures](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures) (read up to "Call")
* [Flask](https://palletsprojects.com/p/flask/)
* [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)

#### Recommended YouTube playlist to get you started


## Learning Objectives
At the end of this projects, you are expected to be able to [explain to anyone](), **without the help of Google:**

### General
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* How is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions...)
* How to display in HTML data from a MySQL database

## More Info
### Install Flask
```
$ pip3 install Flask
```

### **Manual QA Review**
**It is your responsibility to request a review for this project from a peer before the project's deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

#### video library


## Tasks
### 0. Hello Flask!

Write a script that starts a Flask web application:
* Your web application must be listening on *0.0.0.0*, port *5000*
* Routes:
    * */*: display "Hello HBNB!"
* You must use the option *strict_slashes= False* in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
```

File: [0-hello_route.py](), [__init__.py]()

### 1. HBNB
* Your web application must be listening on *0.0.0.0*, port *5000*
* Routes:
    * */*: display "Hello HBNB!"
* You must use the option *strict_slashes= False* in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$
```

File: [1-hbnb_route.py]()
