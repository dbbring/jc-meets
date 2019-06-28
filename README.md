# JC-Meets

JC-Meets is a simple meeting application. You can add new groups, or upload a CSV containing users, groups and their roles.

## Required Dependencies

- Python 3.x ( As a System Enviroment Variable As Well)
- Python PIP
- Node (NPM)

## Getting Started

### Install Back-End Dependencies 

To get started, you first want to navigate the ../jc-meets/api folder in your terminal. Im going to use "python" as my system enviroment variable, which is just a shortcut for activating the Python interpreter. Anyways, back to it, Once there enter the following command:
```
python -m pip install -r requirements.txt
```
This simply locates the requirments.txt file, and PIP installs the required packages. This is a windows command, so if you are using Linux or Mac, ¯\_(ツ)_/¯... You will need to find the proper commands to run on your machine..

## Fire Up the Server

Once the dependencies have installed correct, and still within the same folder (../jc-meets/api), go ahead and run this command:
```
python routes.py
```

Again, here we are just running the routes.py file with the python interpreter. Also again, a windows command, so do what you have to do to fire up a python file on your machine after the dependencies have installed.

With any luck 👍 , you will see the Werkzurg server running.

## Install the Front End Dependencies

Now lets move the front end. In a seperate terminal, navigate to the ../jc-meets/meets-app folder. Once there, run the following command:
```
npm install
```

This will use NPM to go out and download the required dependencies for the front end. I used Vue-CLI to generate the files for the front-end so there will be quite a few dev dependencies.

## Fire Up the Front-End

Still in the same folder (../jc-meets/meets-app), fire up the node server in your seperate terminal using the following command:
```
npm run dev
```

This will start a server on port 8080, and allow for hot-reloads while editing the project.

Again, With any luck 👍 , you see all your modules load and have a project waiting for you.

## View the project

Now, simply open your chrome browser and navigate to http://localhost:8080 !

👏👏👏👏👏👏👏👏
