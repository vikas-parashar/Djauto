from __future__ import print_function
from builtins import input
from builtins import object
import os
import subprocess
import sys
# import djauto


project_name = sys.argv[1]
app_name = sys.argv[2]


new_project = "django-admin.py startproject "
new_app = "python manage.py startapp "

base = os.getcwd()
filename = base+"/"+project_name+"/"+project_name+"/settings.py"
fileout = base+"/"+project_name+"/"+project_name+"/settings.py"

u1 = "curl -u \'"
u2 = "\' https://api.github.com/user/repos -d \'{\"name\":\""
u3 = "\", \"description\":\""
u4 = "\"}\'"
add_repo = "git remote add origin git@github.com:"

class Chdir(object):

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

def create_repo(username, repo_name, repo_description):
	subprocess.call('git init', shell=True)
	subprocess.call(u1+username+u2+repo_name+u3+repo_description+u4,
					 shell=True)
	subprocess.call(add_repo+username+"/"+repo_name+".git", shell=True)
	subprocess.call('git add .', shell=True)
	subprocess.call('git commit -m \"initial commit\"', shell=True)
	subprocess.call("git push origin master", shell=True)
	print("created")

def main():
    # print "installing django.."
    subprocess.call("pip install django", shell=True)

    # print "creating project", project_name, "..."
    subprocess.call(new_project+project_name, shell=True)
    os.chdir(project_name)

    # print "creating app..."
    subprocess.call(new_app+app_name, shell=True)
    add_installed_app(filename)
    # create_repo(username, repo_name)
    prompt = input("Do you want to create repo on github [y/n]: ")
    if prompt =='y' or prompt == 'Y':
    	username = input("Enter github username: ")
    	# repo_name = raw_input("Enter valid repo name: ")
    	repo_description = input("Enter short description for repo: ")
    	create_repo(username, project_name, repo_description)

    print("We're done!")
