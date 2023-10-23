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

Directory: [web_flask]()
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

Directory: [web_flask]()
File: [1-hbnb_route.py]()

### 2. C is fun!
Write a script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes
    * */*: display "Hello HBNB!"
    * */hbnb*: display "HBNB"
    * */c/<text>*: display "C" followed by the value of the *text* variable (replace underscore *_* symbols with a space * *)
* You must use the option *strict_slashes=False* in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```

Directory: [web_flask]()
File: [2-c_route.py]()

### 3. Python is cool!
Write a script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes
    * */*: display "Hello HBNB!"
    * */hbnb*: display "HBNB"
    * */c/<text>*: display "C" followed by the value of the *text* variable (replace underscore *_* symbols with a space * *)
    * */python/<text>*: display "Python", followedd by the value of the *text* variable (replace the underscore *_* with a space * *)
        * The default value of *text* is "is cool"
* You must use the option *strict_slashes=False* in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 
```

Directory: [web_flask]()
File: [3-python_route.py]()

### 4. Is it a number?
Write a script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes
    * */*: display "Hello HBNB!"
    * */hbnb*: display "HBNB"
    * */c/<text>*: display "C" followed by the value of the *text* variable (replace underscore *_* symbols with a space * *)
    * */python/<text>*: display "Python", followedd by the value of the *text* variable (replace the underscore *_* with a space * *)
        * The default value of *text* is "is cool"
    * */number/<n>*: display "*n* is a number" **only** if *n* is an integer
* You must use the option *strict_slashes=False* in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```

Directory: [web_flask]()
File: [4-number_route.py]()

### 5. Number template
Write a script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes
    * */*: display "Hello HBNB!"
    * */hbnb*: display "HBNB"
    * */c/<text>*: display "C" followed by the value of the *text* variable (replace underscore *_* symbols with a space * *)
    * */python/<text>*: display "Python", followedd by the value of the *text* variable (replace the underscore *_* with a space * *)
        * The default value of *text* is "is cool"
    * */number/<n>*: display "*n* is a number" **only** if *n* is an integer
    * */number_template/<n>*: display a HTML page **only** if *n* is an integer:
        * *H1* tag: "Number: *n*" inside the tag *BODY*
* You must use the option *strict_slashes=False* in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```

Directory: [web_flask]()
File: [5-number_template.py](), [templates/5-number.html]()

### 6. Odd or even?
Write a script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes
    * */*: display "Hello HBNB!"
    * */hbnb*: display "HBNB"
    * */c/<text>*: display "C" followed by the value of the *text* variable (replace underscore *_* symbols with a space * *)
    * */python/<text>*: display "Python", followedd by the value of the *text* variable (replace the underscore *_* with a space * *)
        * The default value of *text* is "is cool"
    * */number/<n>*: display "*n* is a number" **only** if *n* is an integer
    * */number_template/<n>*: display a HTML page **only** if *n* is an integer:
        * *H1* tag: "Number: *n*" inside the tag *BODY*
    * */number_odd_or_even/<n>*: display a HTML page **only** if *n* is an integer:
        * *H1* tag: "Number: *n* is *even|odd*" inside the tag *BODY*
* You must use the option *strict_slashes=False* in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```

Directory: [web_flask]()
File: [6-number_odd_or_even.py](), [templates/6-number_odd_or_even.html]()

### 7. Improve engines
Before using Flask to display our HBNB data, you will need to update some part of the engine:

Update <span style="color=red">*FileStorage*</span>: (<span style="color:red">*models/engine/file_storage.py*</span>)

* Add a public method <span style="color:red">*def close(self):*</span>: call <span style="color:red">*reload()*</span> method for deserializing the JSON file to objects

Update <span style="color=red">*DBStorage*</span>: (<span style="color:red">*models/engine/db_storage.py*</span>)

* Add a public method <span style="color:red">*def close(self):*</span>: call <span style="color:red">*remove()*</span> method on the private session attribute (<span style="color:red">*self.__session*</span>)[tips]() or <span style="color:red">*close()*</span> on the class <span style="color:red">*Session*</span> <span style="color:red">[tips]()</span>

Update <span style="color=red">*State*</span>: (<span style="color:red">*models/state.py*</span>)-If it's not already present

* If your storage engin is not <span style="color:red">*DBStorage*</span>, add a public getter method <span style="color:red">*cities*</span> to return the list of <span style="color:red">*City*</span> objects from <span style="color:red">*storage*</span> linked to the current <span style="color:red">*State*</span>

```
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
>>> from models import storage
>>> from models.state import State
>>> len(storage.all(State))
5
>>> len(storage.all(State))
5
>>> # Time to insert new data!
```

At this moment, in another tab:

```
guillaume@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545","2017-03-25 19:42:40","2017-03-25 19:42:40","Alabama");' | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$
```

And let's go back to the Python console:

```
>>> # Time to insert new data!
>>> len(storage.all(State))
5
>>> # normal: the SQLAlchemy didn't reload his `Session`
>>> # to force it, you must remove the current session to create a new one:
>>> storage.close()
>>> len(storage.all(State))
6
>>> # perfect!
```

And for the getter <span style="color:red">*cities*</span> in the <span style="color:red">*State*</span> model:

```
guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 
```

File: [models/engine/file_storage.py](), [models/engine/db_storage.py](), [models/state]()

### 8. List of states
Write a scriptt that starts a Flask web application:

* Your web application must be listening on <span style="color red">*0.0.0.0*</span>, <span style="color red">*5000*</span>
* You must use <span style="color red">*storage*</span> for fectching data from the storage engine (<span style="color red">*FileStorage*</span> or <span style="color red">*DBStorage*</span>) => <span style="color red">*from models import storage*</span> and <span style="color red">*storage.all(...)*</span>
* After each request, you must remove the current SQLAlchemy Session:
    * Declare a method to handle <span style="color red">*@app.teardown_appcontext*</span>
    * Call in this method <span style="color red">*storage.close()*</span>
* Routes:
    * <span style="color red">*/states_list*</span>: display a HTML page: (inside the tag span style="color red">*BODY*</span>)
    * <span style="color red">*UL*</span> tag: with the list of all <span style="color red">*State*</span> objects present in <span style="color red">*DBStorage*</span> **sorted by** span style="color red">*name*</span> (A->Z)[tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
        * <span style="color red">*LI*</span> tag: description of one <span style="color red">*State*</span>: <span style="color red">*<state.id>: <B><state.name></B>*</span>
* Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
* You must use the option <span style="color red">*strict_slashes=False*</span> in your route definition

#### **IMPORTANT**
* Make sure you have a running and <span style="color:red">*setup_mysql_dev.sql*</span> in your <span style="color:red">*AirBnB_clone_v2*</span> repository([Task]())
* Make sure all tables are created when you run <span style="color:red">*echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py*</span>

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>
    </BODY>
</HTML>
guillaume@ubuntu:~$ 
```

File: [web_flask/7-states_list.py](), [web_flask/templates/7-states_list.html]()

### 9. Cities by states
Write a scriptt that starts a Flask web application:

* Your web application must be listening on <span style="color red">*0.0.0.0*</span>, <span style="color red">*5000*</span>
* You must use <span style="color red">*storage*</span> for fectching data from the storage engine (<span style="color red">*FileStorage*</span> or <span style="color red">*DBStorage*</span>) => <span style="color red">*from models import storage*</span> and <span style="color red">*storage.all(...)*</span>
* To load all the cities of a <span style="color:red">*State*</span>
    * If your storage engine is <span style="color:red">*DBStorage*</span>, you must use <span style="color:red">*cities*</span> relationship
    * Otherwise, use the public getter method <span style="color:red">*cities*</span>
* After each request, you must remove the current SQLAlchemy Session:
    * Declare a method to handle <span style="color red">*@app.teardown_appcontext*</span>
    * Call in this method <span style="color red">*storage.close()*</span>
* Routes:
    * <span style="color red">*/city_by_states*</span>: display a HTML page: (inside the tag <span style="color red">*BODY*</span>)
    * <span style="color red">*UL*</span> tag: with the list of all <span style="color red">*State*</span> objects present in <span style="color red">*DBStorage*</span> **sorted by** span style="color red">*name*</span> (A->Z)[tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
        * <span style="color red">*LI*</span> tag: description of one <span style="color red">*State*</span>: <span style="color red">*<state.id>: <B><state.name></B>*</span> + <span style="color:red">*UL*</span> tag: with the list of <span style="color:red">*City*</span> objects linked to the  <span style="color:red">*State*</span> sorted by <span style="color:red">*name*</span> (A->Z)
            * <span style="color:red">*LI*</span> tag: description of one <span style="color:red">*City*</span>: <span style="color:red">*<city.id>: <B><city.name></B>*</span>
* Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
* You must use the option <span style="color red">*strict_slashes=False*</span> in your route definition

#### **IMPORTANT**
* Make sure you have a running and <span style="color:red">*setup_mysql_dev.sql*</span> in your <span style="color:red">*AirBnB_clone_v2*</span> repository([Task]())
* Make sure all tables are created when you run <span style="color:red">*echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py*</span>

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479545: <B>Akron</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479545: <B>Babbie</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479545: <B>Calera</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479545: <B>Fairfield</B></LI>

                </UL>
OB            </LI>
OBOBOB
            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B>
OBOB                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479546: <B>Douglas</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479546: <B>Kearny</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479546: <B>Tempe</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B>
                <UL>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479547: <B>Fremont</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479547: <B>Napa</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479547: <B>San Francisco</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479547: <B>San Jose</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479547: <B>Sonoma</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479548: <B>Denver</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479549: <B>Miami</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479549: <B>Orlando</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479551: <B>Honolulu</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479551: <B>Kailua</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479551: <B>Pearl city</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479554: <B>Baton rouge</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479554: <B>Lafayette</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479554: <B>New Orleans</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479555: <B>Saint Paul</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479556: <B>Jackson</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479556: <B>Meridian</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479556: <B>Tupelo</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479557: <B>Eugene</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479557: <B>Portland</B></LI>

                </UL>
            </LI>

        </UL>
    </BODY>
</HTML>
guillaume@ubuntu:~$ 
```

In the browser: [http://localhost:5000/cities_by_states](http://localhost:5000/cities_by_states)

File: [web_flask/8-cities_by_states.py](), [web_flask/templates/8-cities_by_states.html]()

### 10. States and State
Write a script that starts a Flask web application:

* Your web application must be listening on <span style="color:red">*0.0.0.0*</span>, port <span style="color:red">*5000*</span>
* You must use <span style="color:red">*storage*</span> for fetching data from the storage engine (<span style="color:red">*FileStorage*</span> or <span style="color:red">*DBStorage*</span>) => from <span style="color:red">*from models import storage*</span> and <span style="color:red">*storage.all(...)*</span>
* To load all cities of a <span style="color:red">*State*</span>:
    * If your storage engine is <span style="color:red">*DBStorage*</span>, you must use <span style="color:red">*cities*</span> relationship
    * Otherwise, use the public getter method <span style="color:red">*cities*</span>
* After each request, you must remove the current SQLAlchemy Session:
    * Declare a method to handle <span style="color red">*@app.teardown_appcontext*</span>
    * Call in this method <span style="color red">*storage.close()*</span>
* Routes:
    * <span style="color:red">*/states*</span>: display a HTML page: (inside the tag <span style="color:red">*BODY*</span>)
    * <span style="color red">*UL*</span> tag: with the list of all <span style="color red">*State*</span> objects present in <span style="color red">*DBStorage*</span> **sorted by** span style="color red">*name*</span> (A->Z)[tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
        * <span style="color red">*LI*</span> tag: description of one <span style="color red">*State*</span>: <span style="color red">*<state.id>: <B><state.name></B>*</span>
    * <span style="color red">*/states/<id>*</span>: display a HTML page: (inside the tag <span style="color red">*BODY*</span>)
        * If a <span style="color red">*State*</span> object is found with this <span style="color red">*id*</span>:
            * <span style="color red">*H1*</span> tag: "State:"
            * <span style="color red">*H3*</span> tag: "Cities:"
            * <span style="color red">*UL*</span> tag: with the list of <span style="color red">*City*</span> objects linked to the <span style="color red">*State*</span> **sorted by** <span style="color red">*name*</span>
                * <span style="color:red">*LI*</span> tag: description of one <span style="color:red">*City*</span>: <span style="color:red">*<city.id>: <B><city.name></B>*</span>
        * Otherwise:
            * <span style="color:red">*H1*</span> tag: "Not found!"
* You must use the option <span style="color red">*strict_slashes=False*</span> in your route definition
* Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data

#### **IMPORTANT**
* Make sure you have a running and <span style="color:red">*setup_mysql_dev.sql*</span> in your <span style="color:red">*AirBnB_clone_v2*</span> repository([Task]())
* Make sure all tables are created when you run <span style="color:red">*echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py*</span>

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>State: Illinois</H1>
        <H3>Cities:</H3>
        <UL>
                <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>
        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>
guillaume@ubuntu:~$ 
```

File: [web_flask/9-states.py](), [web_flask/templates/9-states.html]()

## 11. HBNB filters
Write a script that starts a Flask web application:

* Your web application must be listening on <span style="color:red">*0.0.0.0*</span>, port <span style="color:red">*5000*</span>
* You must use <span style="color:red">*storage*</span> for fetching data from the storage engine (<span style="color:red">*FileStorage*</span> or <span style="color:red">*DBStorage*</span>) => from <span style="color:red">*from models import storage*</span> and <span style="color:red">*storage.all(...)*</span>
* To load all cities of a <span style="color:red">*State*</span>:
    * If your storage engine is <span style="color:red">*DBStorage*</span>, you must use <span style="color:red">*cities*</span> relationship
    * Otherwise, use the public getter method <span style="color:red">*cities*</span>
* After each request, you must remove the current SQLAlchemy Session:
    * Declare a method to handle <span style="color red">*@app.teardown_appcontext*</span>
    * Call in this method <span style="color red">*storage.close()*</span>
* Routes:
    * <span style="color:red">*/hbnb_filters*</span>: displays a HTML page like <span style="color:red">*6-index.html*</span>, which was done during the project [0x01.AirBnB clone - Web static]()
        * Copy files <span style="color:red">*3-footer.css*</span>, <span style="color:red">*3-header.css*</span>, <span style="color:red">*4-common.css*</span> and <span style="color:red">*6-filters.css*</span> from <span style="color:red">*web_static/styles/*</span> to the folder <span style="color:red">*web_flask/static/styles*</span>
        * Copy files <span style="color:red">*icon.png*</span> and <span style="color:red">*logo.png*</span> from <span style="color:red">*web_static/images/*</span> to the folder <span style="color:red">*web_flask/static/images*</span>
        * Update <span style="color:red">*.popover*</span> class in <span style="color:red">*6-filters.css*</span> to allow scrolling in the popover and a max height of 300pixels
        * Use <span style="color:red">*6-index.html*</span> content as source code for the template <span style="color:red">*10-hbnb_filters.html*</span>:
            * Replace the content of the <span style="color:red">*H4*</span> tag under each filter title(<span style="color:red">*H3*</span> States and <span style="color:red">*Amenities*</span>) by <span style="color:red">*&nbsp*</span>
        * <span style="color:red">*State*</span>, <span style="color:red">*City*</span> and <span style="color:red">*Amenity*</span> objects must be loaded from <span style="color:red">*DBStorage*</span> and **sorted by name** (A-Z)
* You must use the option <span style="color red">*strict_slashes=False*</span> in your route definition
* Import this [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql) to have some data

#### **IMPORTANT**
* Make sure you have a running and <span style="color:red">*setup_mysql_dev.sql*</span> in your <span style="color:red">*AirBnB_clone_v2*</span> repository([Task]())
* Make sure all tables are created when you run <span style="color:red">*echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py*</span>

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In the browser: [http://localhost:5000/hbnb_filters](http://localhost:5000/hbnb_filters)

File: [web_flask/10-hbnb_filters.py](), [web_flask/templates/10-hbnb_filters.html](), [web_flask/static/]()

### 12. HBNB is alive!
Write a script that starts a Flask web application:

* Your web application must be listening on <span style="color:red">*0.0.0.0*</span>, port <span style="color:red">*5000*</span>
* You must use <span style="color:red">*storage*</span> for fetching data from the storage engine (<span style="color:red">*FileStorage*</span> or <span style="color:red">*DBStorage*</span>) => from <span style="color:red">*from models import storage*</span> and <span style="color:red">*storage.all(...)*</span>
* To load all cities of a <span style="color:red">*State*</span>:
    * If your storage engine is <span style="color:red">*DBStorage*</span>, you must use <span style="color:red">*cities*</span> relationship
    * Otherwise, use the public getter method <span style="color:red">*cities*</span>
* After each request, you must remove the current SQLAlchemy Session:
    * Declare a method to handle <span style="color red">*@app.teardown_appcontext*</span>
    * Call in this method <span style="color red">*storage.close()*</span>
* Routes:
    * <span style="color:red">*/hbnb*</span>: displays a HTML page like <span style="color:red">*8-index.html*</span>, done during the [0x01.AirBnB clone - Web static]() project.
        * Copy files <span style="color:red">*3-footer.css*</span>, <span style="color:red">*3-header.css*</span>, <span style="color:red">*4-common.css*</span>, <span style="color:red">*6-filters.css*</span> and <span style="color:red">*8-places.css*</span> from <span style="color:red">*web_static/styles/*</span> to the folder <span style="color:red">*web_flask/static/styles*</span>
        * Copy files <span style="color:red">*web_static/images/*</span> to the folder <span style="color:red">*web_flask/static/images*</span>
        * Update <span style="color:red">*.popover*</span> class in <span style="color:red">*6-filters.css*</span> to allow scrolling in the popover and set max height to 300pixels
        * Update <span style="color:red">*8-places.css*</span> to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)
        * Use <span style="color:red">*6-index.html*</span> content as source code for the template <span style="color:red">*100-hbnb.html*</span>:
            * Replace the content of the <span style="color:red">*H4*</span> tag under each filter title(<span style="color:red">*H3*</span> States and <span style="color:red">*Amenities*</span>) by <span style="color:red">*&nbsp*</span>
            * Make sure all HTML tags from objects are correctly used (example: <span style="color:red"><BR /></span> must generate a new line)
        * <span style="color:red">*State*</span>, <span style="color:red">*City*</span> and <span style="color:red">*Amenity*</span> objects must be loaded from <span style="color:red">*DBStorage*</span> and **sorted by name** (A-Z)
* You must use the option <span style="color red">*strict_slashes=False*</span> in your route definition
* Import this [100-dump]() to have some data

#### **IMPORTANT**
* Make sure you have a running and <span style="color:red">*setup_mysql_dev.sql*</span> in your <span style="color:red">*AirBnB_clone_v2*</span> repository([Task]())
* Make sure all tables are created when you run <span style="color:red">*echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py*</span>

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 100-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 100-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In the browser: [http://localhost:5000/hbnb](http://localhost:5000/hbnb)

File: [web_flask/100-hbnb.py](), [web_flask/templates/100-hbnb.html](), [web_flask/static/]()
