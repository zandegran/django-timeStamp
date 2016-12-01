timeStamps
==========


#### A library to keep track of user login times in Django

###Installation

**Run  `python setup.py install`  to install.**

or

**Copy timeStamps folder to python `site-packages` folder (Mannual installation)**

Once you’ve installed django-timeStamps, you can verify successful installation by opening a Python interpreter and typing `import timeStamps`

###Quick Start
Add `'timeStamps',` to INSTALLED_APPS in settings.py

and

run `manage.py migrate` to install needed database tables

#####Required setting 
`MAX_TIMESTAMPS = 5` in settings.py
5 is the maximum number of timestamps stored per user

:smile:
