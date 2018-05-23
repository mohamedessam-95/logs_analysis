#Objective
To host the website previously developed on a public IP address through linux OS.

#Pre-requisites
1. URL for the hosted website - http://159.89.170.61/
2. Port number 2200

#Instructions
##Setting up the user account
1. Launch your virtual machine that has linux OS
2. Login to the account using the SSH key provided
3. Update all the available packages `sudo apt-get update`
4. Upgrade all the existing packages `sudo apt-get upgrade`
5. Install Finger `sudo apt-get install finger`
6. Create a new user 'grader' `sudo adduser grader`
7. Add grader to sudo group `gpasswd -a grader sudo`
8. Login to the grader
9. Create a new .ssh directory in the home directory `sudo mkdir .ssh`
10. Change its privileges to 700 `sudo chmod 700 .ssh`
11. Create a file called authorized_keys inside .ssh and paste the public SSH
    key provided earlier inside it
12. Change back the permission of .ssh to 600
13. Exit the user using `exit`
14. Open sshd_config file using `sudo nano /etc/ssh/sshd_config` and change line
    `PermitRootLogin yes` to `PermitRootLogin no`.
    Also change `PasswordAuthentication yes` to  `PasswordAuthentication no`.
    Change the port number from 22 to 2200. Save and exit the file.
    `service ssh restart`

## Setting up the firewall
15. Add firewall to your account by executing the following commands
`sudo ufw allow ssh`
`sudo ufw allow 2200/tcp`
`sudo ufw allow 80/tcp`
`sudo ufw allow 123/udp`
`sudo ufw allow www`
`sudo ufw enable`
16. Restart ssh by using `service ssh restart`
17. Check if you are able to access grader by opening a fresh terminal and
executing `ssh grader@159.89.170.61`. The account will open if it works fine.

## Install required packages
18. Login to grader account , execute the following commands to install required
packages
`sudo apt-get install apache2`
`sudo apt-get install postgresql`
`sudo apt-get install python-setuptools libapache2-mod-wsgi`
`sudo apt-get install git`
`sudo apt-get install pip`
`sudo pip install --upgrade oauth2client`
`sudo pip install requests`

##Configuring database
19. Configure the database using following commands
`sudo su - postgres`
`postgres=# CREATE DATABASE catalog;`
`postgres=# CREATE USER catalog;`

Set the password for the user catalog
`postgres=# ALTER ROLE catalog WITH PASSWORD 'password';`

Grant permission for the catalog user to access the catalog database
`postgres=# GRANT ALL PRIVILEGES ON DATABASE catalog TO catalog;`
20. Quit postgresql y typing `\q`
21. Exit from the user postgres .by using `exit`

##Configuring flask application
22. Go to /var/www `cd /var/www/`
23. Create a folder called FlaskApp - `sudo mkdir FlaskApp`
23. Clone the catalog project from git using the below url
    `https://github.com/TheMadSushi/Catalog.git`
24. Change the project name from 'Catalog' to 'FlaskApp' `sudo mv Catalog FlaskApp`
25. Go into FlaskApp project and rename project.py to __init__.py
    `sudo mv project.py __init__.py`
26. In database_setup.py, __init__.py and foodmenu.py, change the line
    `engine = create_engine('sqlite:///restaurantmenuwithusers.db')` to
    `engine = create_engine('postgresql://catalog:password@localhost/catalog')`
27. Install psycopg2 `sudo apt-get -qqy install postgresql python-psycopg2`
28. Execute database_setup.py `python database_setup.py`
29. Create FlaskApp.conf to edit: `sudo nano /etc/apache2/sites-available/FlaskApp.conf`
30. Add the following lines of code to the file to configure the virtual host.

`<VirtualHost *:80>
	ServerName 159.89.170.61
	ServerAdmin surabhi.shivmath@gmail.com
	WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
	<Directory /var/www/FlaskApp/FlaskApp/>
		Order allow,deny
		Allow from all
	</Directory>
	Alias /static /var/www/FlaskApp/FlaskApp/static
	<Directory /var/www/FlaskApp/FlaskApp/static/>
		Order allow,deny
		Allow from all
	</Directory>
	ErrorLog ${APACHE_LOG_DIR}/error.log
	LogLevel warn
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>`

31. Enable the virtual host with the following command: `sudo a2ensite FlaskApp`
32. Create the .wsgi File under /var/www/FlaskApp:
    `cd /var/www/FlaskApp
    sudo nano flaskapp.wsgi`
33. Add the following lines of code to the flaskapp.wsgi file:
    `#!/usr/bin/python
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0,"/var/www/FlaskApp/")

    from FlaskApp import app as application
    application.secret_key = 'Add your secret key'`

34. Restart Apache `sudo service apache2 restart`

Notes
35. Go to `/var/log/apache2/error.log` for any error
36. For unsuported locale settings error
`export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales`
37. Give absolute path in case of "No such file or directory": 'client_secrets.json' error.


#References
https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

#Third party applications used
DigitalOcean's droplet
