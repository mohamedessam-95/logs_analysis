# Item Catalog project
This web application application provides a list of items within a variety of categories Registered users will have the ability to post, edit and delete their own items. 

## Prerequisites
- A Debian system is recommended but not necessary.
- The following packages are required.
  - build-essentail (from the debian repo)
  - pip (from the debian repo)
  - postgreSQL 9.6.7
  - psycopg2
  - flask
  - httplib2
  - google api client for python
  - requests

- The following commands can be run to get all the prerequisites up and running.
  ```bash
  sudo apt-get install binutils
  sudo apt-get install postgresql
  sudo apt-get install python-pip
  sudo pip install flask
  sudo pip install psycopg2
  sudo pip install httplib2
  sudo pip install --upgrade google-api-python-client
  sudo pip install requests
  ```

## Setup
To get the source/ app it is recommended to get it from github
```bash
git clone https://github.com/findNico/itemCatalog.git
```

To setup the database and populate it run the following *(enter sudo password when prompted)*
```bash
cd itemCatalog/setupScripts/
./setup.sh
```

Inside the config folder there are file config.json and client_secrets.json
The client_secrets.json is provided by google for Oauth
The config.json holds the configuration fort the server edit this file if you want it to run differently, by default :
- Application  runs in debug mode, change **debug** to **False** for production.
- All ip's are allowed, change **allowedIp** to change this.
- The default port is 5000 change **port** if a different port has been desired.
- It is important to generate a secret key of your own and replace **secretKey** with it.
- The db settings is for a "vanilla" setup change these value if a different database settings are being used
```json
{
        "host": {
                "port": 5000,
                "allowedIp": "0.0.0.0",
                "secretKey": "this should be a secretKey",
                "debug":"True"
        },
        "db":{
                "host":"localhost",
                "db":"catalog",
                "user":"devuser",
                "password":"devuser"
        }
}
```

## Running the project
To run the project/app navigate to the root folder and run the following
```bash
python app.py
```

## file layout
```bash
├── app.py
├── bluePrints
│   ├── api.py
│   ├── connect.py
│   └── __init__.py
├── config
│   ├── client_secrets.json
│   └── config.json
├── libs
│   ├── appHelper.py
│   ├── myDb.py
│   └── myErr.py
├── README.md
├── setupScripts
│   ├── db.sql
│   ├── populate.sql
│   └── setup.sh
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       ├── jquery-3.3.1.min.js
│       └── platform.js
└── templates
    ├── baseEdit.html
    ├── base.html
    ├── categDel.html
    ├── categEdit.html
    ├── index.html
    ├── itemDel.html
    ├── itemEdit.html
    ├── items.html
    ├── macroCategories.html
    ├── macroHeader.html
    ├── macroItems.html
    ├── macroLatestItems.html
    └── register.html
```

| file/folder                | description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| app.py                     | The main server code                                         |
| config                     | Folder containing the configuration files                    |
| config/config.json         | Configuration for the server                                 |
| config/client_secrets.json | Configuration for Oauth (google api)                         |
| libs                       | Folder for my library's                                      |
| libs/appHelper.py          | Helper function for app.py                                   |
| libs/myDB.py               | Database driver (postgress)                                  |
| libs/myErr.py              | Error classes                                                |
| setupScripts               | A small collection of scripts to setup for the db            |
| setupScripts/setup.sh      | A hail Mary script the setupt the db and populates it with sample data |
| setupScripts/db.sql        | sql file that creates tables/views/storedFunctions           |
| setupScripts/populate.sql  | Populate the DB with sample  data                            |
| static                     | Folder containing static files for the client (style-sheets and javascript) |
| templates                  | A collection of jinja templates for the client               |
| bluePrints                 | A collections of flask blueprint to make the project more managable |
| bluePrints/connect         | This contains the auth code                                  |
| bluePrints/api             | This contains json api endpoint                              |

## Connecting to the web front end / client
In the address bar of your web browser enter the ip address of the machine/host that the server is running with the listening port.

Examples:
```
localhost:5000
192.168.1.42:5000
```

## making use of the json api 
- to get a json list of all the catalog items
  ```bash
  curl "http://localhost:5000/catalog.json"
  {
  	"categories": [{
  		"item": [{
  			"cat_id": "slackline",
  			"title": "dyneema sling",
  			"description": "A sling or ,
  			"id": "9f0bbeb2-30f9-4b64-8aa5-f79a45d08607"
  ...		
  ```
- to get a json list of all the items belonging to a categorie
  ```bash
   curl "http://localhost:5000/catalog/slackline/items.json"
  {
  	"items": [{
  		"category": "slackline",
  		"name": "dyneema sling"
  	}, {
  		"category": "slackline",
  		"name": "Tree pro"
  	}, {
  		"category": "slackline",
  		"name": "Webbing"
  	}, {
  		"category": "slackline",
  		"name": "Weblocks"
  	}]
  }
  ```
- to get more information about an item
  ```bash
  curl "localhost:5000/catalog/slackline/Tree%20pro.json"
  {
  	"item": {
  		"name": "Tree pro",
  		"desc": "It is used to protect the trees when that slacklines are rigged on"
  	}
  }
  ```
## Other Notes
- Sublime text editor with autopep8 plug-in installed was used to edit the source.
- Typora was used to create the md file.
- I can be contacted by sending a mail to find.nicovw@gmail.com.
- It might be necessary to delete the cookies from your browser.



## Possible further developmet 

- Add local auth
- Add more Oath2 signing options
- Refreshing of acces token and shorter timeouts
- Activity and usage  logging
- Server statistics