# short-link-app
This is short link web service.
To work with is you need to follow this steps:
1. Clone repository
2. Set virtual enviroment for application
  To make this, run `$ python3 -m venv myvenv`
3. After this you need to activate your venv:
  `$ source path_to_venv/bin/activate`
When you did it you will see venv name at the start of the command line
4. Now you need to install Django
  `pip install django`
  If you don't have pip, read how to [get pip](https://pip.pypa.io/en/stable/installing/)
5. Now you need to go to web service folder `$ cd short-link-app/webservice/` and run local server `python manage.py runserver`. In terminal you will get some logs and local address.
```
System check identified no issues (0 silenced).
July 19, 2018 - 14:39:56
Django version 2.0.7, using settings 'webservice.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
6. All work is done, now you can use this service.
![alt text][example]


[example]: https://pp.userapi.com/c846020/v846020219/a1e2e/Ud3r-R1DHWc.jpg "Web Service"
