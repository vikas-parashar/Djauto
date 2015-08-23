import os
import subprocess
import sys
import djauto

project_name = raw_input("Project name>>")
new_project = "django-admin.py startproject "
new_app = "python manage.py startapp "
settings = project_name+"/"+project_name+"/settings.py"

class Chdir:
      def __init__( self, newPath ):
        self.savedPath = os.getcwd()
        os.chdir(newPath)

      def __del__( self ):
        os.chdir( self.savedPath )

def add_installed_app(filename):
	f = open(filename,'r')
	filedata = f.read()
	f.close()
	olddata = "'django.contrib.staticfiles',"
	newdata = "'django.contrib.staticfiles',\n,'"+new_app+"',"
	replaced_data = filedata.replace(olddata,newdata)

	f = open(fileout,'w')
	f.write(replaced_data)
	f.close()
	print filename,"2657"

def main():
	# print "installing django.."
	subprocess.call("pip install django", shell=True)
	# print "Django installed"
	print subprocess.call('pwd', shell=True)

	# print "creating project", project_name, "..."
	subprocess.call(new_project+project_name, shell=True)

	os.chdir(project_name)
	# print "project created"

	is_app = raw_input("Do you want to create new app?(y/n):")

	if is_app == ('y' or 'Y'):
		app_name = raw_input("Provide valid app name:")
		# print "creating app..."
		subprocess.call(new_app+app_name, shell=True)
		# print app_name, "created."
		add_installed_app(settings)


	print "We're done!"
