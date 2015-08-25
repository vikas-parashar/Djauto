Django-project-generator
========================
Create Django projects the easy way. From installing django to creating app for project, One command, that's all!

Install
-------

    pip install djauto

How to use it?
--------------

  djauto PROJECT_NAME APP_NAME

What does above command do?
---------------------------
1. Downloads latest version of [Django](https://www.djangoproject.com/) using pip
2. Creates a django project named "PROJECT_NAME" in current directory.
3. Creates and add the app named "APP_NAME" in INSTALLED_APPS in `settings.py`.
4. Asks if you want to create github repository. If yes, then
	1. Asks for github username.
	2. Creates repo named PROJECT_NAME.
	3. Asks for short description.
	4. Asks for password.
	5. Adds all file and push it on github.
5. We're done!