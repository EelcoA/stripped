# AESSET Resource Manager

## Installation instructions
For local deployment you can run it in 2 ways: 
- in Docker on your pc
- local on your pc

The preferred way is to deploy it in Docker, since all dependencies (python, 
libraries and postgres database) are included in the Docker images. 
Only debugging and accessing the database is harder.

### Installation in Docker on your desktop
Global steps (to be refined later)
1) install Docker, see <a href="https://www.docker.com/products/docker-desktop" target="_blank">docker.com</a>. 

    After installation:

    1.1 make sure that you have a 'docker' group and that your user account 
    has been added to it. If not, create the group and add your user. On linux:
    ```
    sudo groupadd docker
    sudo gpasswd -a ${USER} docker
    ```
    For mac, see here how to setup users and groups: 
    <a href="https://support.apple.com/guide/mac-help/set-up-other-users-on-your-mac-mtusr001/mac" 
    target="_blank">support.apple.com</a>
    
    1.2 and (re)start docker

2) install git, see <a href="https://git-scm.com/downloads" target="_blank">git-scm.com</a>
   
3) checkout the code

    On the command line, go to the location where the project directory has to be
    placed, e.g. /python/django. Clone the repository which will create a subdirectory
    'stripped' in there. Type:
    ```
    git clone https://github.com/EelcoA/stripped.git
    ```
4) go into the newly created directory:
    ```
    cd stripped
    ```
5) start app:
    ```
    docker-compose up --build 
    ```
    This first time it will take a while since the base images for Python and 
    Postgres have to be downloaded. If all goes well it should end with something 
    like:
    ```
    web_1  | [30/Nov/2020 16:46:36] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
    web_1  | Watching for file changes with StatReloader
    web_1  | Performing system checks...
    web_1  | 
    web_1  | System check identified no issues (0 silenced).
    web_1  | December 01, 2020 - 08:49:29
    web_1  | Django version 3.1.3, using settings 'config.settings'
    web_1  | Starting development server at http://0.0.0.0:8100/
    web_1  | Quit the server with CONTROL-C.
    ```

6) Create the database tables

    Open a new command line window for the next steps:
    ```
    docker-compose exec web python manage.py migrate
    ```

7) Create the admin user
    ```
    docker-compose exec web python manage.py createsuperuser
    ```
    Fill in: aesset-rm-admin with password testpass123, or something else ;-)

8) check the app on:
    - http://localhost:8100
    - http://localhost:8100/admin   -> log in with the user you created 

9) Stop the docker images with the application and database:
    
    By pressing CTRL+C in the window where you started the images.

## Start and stop the application
From now on you can start and stop the application with the following 
commands executed in the stripped/ directory: 
```
docker-compose up         # starts the application with log in foreground
docker-compose up -d      # starts the application in the background
docker-compose up --build # rebuilds and starts the application
docker-compose down       # shuts down the application
docker-compose logs -f    # follow the logging
```
 
## Database location
   
The database is placed local on your pc. The location depends on the
installation of Docker, but it is something like:
```
var/lib/docker/volumes/aesset-rm_postgres_data
```

## Upgrade the application

Update the sources: go to the 'stripped' directory on the command line and type:
```
git pull
```

Start the application, with the build option, maybe not needed, but sometimes it is:
```
docker-compose up --build
```

Go to a new commandline window in the 'stripped' directory and type:
```
docker-compose exec web python manage.py migrate
```
This updates the database with the latest structure changes

# Reinitialize the database

Want to start all over? Easy! The database is a 'volume' defined in the 
docker-compose. By removing that volume and restart the containers the
database is recreated. After that you run the migrates and create the 
superuser again:

Check the volumes: 
```
$ docker volume ls
DRIVER    VOLUME NAME
local     aesset-rm_postgres_data      <-- this is the one
```
If you want to get more info about it:
```
$ docker volume inspect aesset<tab> <-- press tab for auto completion
```
Then to remove:
```
$ docker volume rm aesset<tab>
```
Start the containers, create the tables and create superuser:
```
$ docker-compose up -d
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
```
Fill in: aesset-rm-admin with password testpass123, or something else ;-)

And you're back in business!

#### Author
- Eelco Aartsen
- eelco@aesset.nl
- AESSET IT - The Netherlands
- www.aesset.nl


