import os
import subprocess
import sys
import djauto


project_name = sys.argv[1]
app_name = sys.argv[2]
new_project = "django-admin.py startproject "
new_app = "python manage.py startapp "

base = os.getcwd()
filename = base+"/"+project_name+"/"+project_name+"/settings.py"
fileout = base+"/"+project_name+"/"+project_name+"/settings.py"


class Chdir:

    def __init__(self, newPath):
        self.savedPath = os.getcwd()
        os.chdir(newPath)

    def __del__(self):
        os.chdir(self.savedPath)


def add_installed_app(filename):
    f = open(filename, 'r')
    filedata = f.read()
    f.close()
    olddata = "'django.contrib.staticfiles',"
    newdata = "'django.contrib.staticfiles',\n\t"+"'"+app_name+"',"
    replaced_data = filedata.replace(olddata, newdata)

    f = open(fileout, 'w')
    f.write(replaced_data)
    f.close()


def main():
    # print "installing django.."
    subprocess.call("pip install django", shell=True)

    # print "creating project", project_name, "..."
    subprocess.call(new_project+project_name, shell=True)
    os.chdir(project_name)

    # print "creating app..."
    subprocess.call(new_app+app_name, shell=True)
    add_installed_app(filename)

    print "We're done!"
