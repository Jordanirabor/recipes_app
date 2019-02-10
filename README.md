## Introduction

This is the repository for a tutorial that teaches how to set up a server side rendered web application using Django and Nuxt.js. 

## Requirements
* [Python3](https://www.python.org/download/releases/3.0/)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Npm](https://www.npmjs.com/) (or [Yarn](https://yarnpkg.com/en/))

## Running the application
1. Clone the project to your machine ```[git clone https://github.com/Jordanirabor/recipes_app]```
2. Navigate into the diretory ```[cd recipes_app]```
3. Source the virtual environment ```[pipenv shell]```
4. Install the dependencies ```[pipenv install]```
5. Navigate into the backend directory ```[cd api]```
6. Start the backend server ```[python manage.py runserver]```
7. Open up a new instance of the terminal (from the parent directory of the project) and navigate into the frontend directory ```[cd client]```
8. Install dependencies ```[npm install]```
9. Start the frontend development server ```[npm run dev]```
10. Explore the server-side rendered application i.e create a new recipe on this address - ```[http://localhost:3000]```

## Built With

* [Python](https://www.python.org/) - A programming language that lets you work quickly and integrate systems more effectively.
* [Django](http://djangoproject.org/) - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Nuxt](https://nuxtjs.org/) - Nuxt.js is a minimal framework for creating Vue.js applications with server side rendering, code-splitting, hot-reloading, static generation and more.