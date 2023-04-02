
# README

## Description :
 
<b>Colibri HR System Django REST API </b>

## Setup Steps

### 1. Clone github code
```
   git clone https://github.com/btrif/django_hr_system_api.git
```
### 2. Setup virtual environment

   To create new environment, 
go to project folder and create the virtual env :

```
python -m venv .hr_system_venv
```
### 3. Activate virtual environment

```
.hr_system_venv\Scripts\activate.bat           (Windows)
./.hr_system_venv/bin/activate                 (Linux, Mac)
```

### 4. Install requirements.txt

Install the Python libraries inside virtual environment :
```
(.hr_system_venv) D:\workspace\django_hr_system_api> pip install -r requirements.txt
```

### 5. Start Django server

```
(.hr_system_venv) D:\workspace\django_hr_system_api> python manage.py runserver

```

# Docker alternative
#### Advantage : You can completely ignore the manual setup from above. This will be done automatically for you by Docker.
If you have installed Docker locally on you machine you can do the following
in the root folder of the application :

```bash
D:\workspace\django_hr_system_api>docker build . -t django_hr_system_api:latest
D:\workspace\django_hr_system_api>docker run -p 8000:8000 django_hr_system_api
```

Now  you can already use in the same way the host machine Web Browser Application API.
You should get something like this :
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 07, 2022 - 15:48:35
Django version 4.0.5, using settings 'django_hr_system_api.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```