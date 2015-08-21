import os
import subprocess
import sys
import time

project_name = sys.argv[1]
new_project = "django-admin.py startproject "
new_app = "python manage.py startapp "

SETTINGS_FILE = project_name+"/settings.py"


class Chdir:

    def __init__(self, newPath):
        self.savedPath = os.getcwd()
        os.chdir(newPath)

    def __del__(self):
        os.chdir(self.savedPath)


def add_installed_app(filein, fileout):
    f = open(filein, 'r')
    filedata = f.read()
    f.close()
    olddata = "'django.contrib.staticfiles',"
    newdata = "'django.contrib.staticfiles',\n\t'"+app_name+"',"
    replaced_data = filedata.replace(olddata, newdata)

    f = open(fileout, 'w')
    f.write(replaced_data)
    f.close()


print "installing django.."
subprocess.call("pip install django", shell=True)
print "Django installed"

print "creating project", project_name, "..."
subprocess.call(new_project+project_name, shell=True)

os.chdir(project_name)
print "project created"

is_app = raw_input("Do you want to create new app?(y/n):")

if is_app == ('y' or 'Y'):
    app_name = raw_input("Provide valid app name:")
    print "creating app..."
    subprocess.call(new_app+app_name, shell=True)
    print app_name, "created."
    add_installed_app(SETTINGS_FILE, SETTINGS_FILE)

print "We're done!"
