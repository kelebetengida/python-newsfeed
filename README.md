# python-newsfeed
![MIT license badge](https://img.shields.io/badge/license-MIT-green)


## Discription 
Just Tech News, is a website where users can post, upvote, and comment on links to news articles. The aplication was bulit using Python as the backend and Python Flask framework for front end. The aplication is pawored with Python, Python Flask, SQL, SQLAlchemy, Javascript, Pricfile, HTML, CSS and Heroku. The reasone for bulding this aplication is to further my lskills as developer in python based frameworks. Please be respectful of others view on this platform. Through bulding this aplication I have learned how to bulid and deploy to the cloud a Flask API with correct project structure and necessary dependencies. I also have learned how to connect the application to an RDBMS database using SQL Alchemy to support the API model, templating to the application to allow for user interactions and perform basic DevOps and deploy to a cloud infrastructure. The next fetures of this aplication at the core will encompass machine learning algorithms to refine the UI for a user friendly experince. 


## Table of Contents
  * [Installation](#installation)
  * [Usage](#usage)
  * [License](#license)
  * [Technologies](#technologies)
  * [Testing](#testing)
  * [Questions](#questions)
  
## Installation
Copy project url from GitHub.
On Windows open a PowerShell terminal.  
Navigate into the directory where you want to keep your project.    
Run 
```
git clone <repo_url>   
```
and cd into python-news directory.

Run
```
python -m venv venv
```
to create a virtual environment.

Run
```
.\venv\Scripts\activate
```
to launch virtual environment

Run
```
pip install -r requirements.txt
```
to install dependencies in the venv/Lib/site-packages folder

Create a .env file in the root of the project and add the following configuration code for your database connection.  Replace PASSWORD with the password of your root MySQL user
```
DB_URL=mysql+pymysql://root:PASSWORDd@localhost/python_news_db

```

Run 
```
python seeds.py
```
to seed database.

Run
```
python -m flask run
```
to start the server on localhost:5000.

## Usage
Open localhost:5000 in browser and sign up to create posts with links to your favorite articles.  Add comments and upvotes.

## License 
This project is covered under the MIT license 

## Technologies 
HTML5, CSS3, JavaScript, Python, MySQL, Flask, Jinja

## Testing
Tests coming soon

## Questions
Visit me at GitHub  
[Kelebet Engida](https://github.com/kelebetengida)
  
If you have any questions or would like to contact me, please email me at  
[kelebetaengida@gmail.com](kelebetaengida@gmail.com)