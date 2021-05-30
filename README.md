


# Udacitrivia - Full Stack Trivia App

Udacitrivia is a trivia app born out of the desire to create an intimate, fun, bonding exeperience for the employees and students of Udacity. The Udacitrivia app is a  web application designed to manage and play the trivia game using React for the frontend and Flask Python web framework to manage the backend.  

The Udacitrivia app has the following functionality:

1. Display questions - The app can display all questions in the database as well as by category. Question are displayed showing the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

# Getting Started
This full stack application has backend and frontend dependencies which are as follows:

## Backend Dependencies

To set-up the backend install the following dependencies: 

1. **Python 3.9** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - It is recommended that you  working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

 ### Database Setup:

 Use the trivia.psql file provided to restore the database containing the neccesary informationl for this trivia app. Navigate into you backend folder and in the terminal run the following command: 

 ```bash
psql trivia < trivia.psql
```
### Running the server:

In your terminal run the following command to run the 
server:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development  
flask run 
```
The `FLASK_ENV=development` command will ensure that the server automatically restarts should any changes to the flask app be detected. 

## Frontend Dependencies

To set-up the backend install the following dependencies: 

1. **Installing Node and NPM**<br>
This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

2. **Installing project dependencies**<br>
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```
### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. Make sure that the backend server is running at the same time in a seperate CLI to ensure that the trivia app works correctly. Instructions on how to run your backend server available in the Backend dependencies section. 


Once you've executed the ```npm start``` command and have your backend server running in a seperate window  go to your browswer and open [http://localhost:3000](http://localhost:3000) to view the Udacitrivia app. <br>

```bash
npm start
```

## Testing 
 Testing is conducted using unittest.

In order to run tests navigate to the backend folder and run the following commands in your terminal:

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

```

The first time you run the tests, omit the dropdb command. 

All tests are kept in the test_flaskr.py file and should be maintained as updates are made to app functionality. 


# API Reference

## Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 


## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found!"
}
```
The API will return the following error types when requests fail:
- 404: Resource Not Found
- 422: Not Processable 

## Endpoints

### GET /categories

- General: This endpoint returns a list categories.

Sample: `curl http://127.0.0.1:5000/categories`
``` 
 {
      "categories": {
          "1": "Science", 
          "2": "Art", 
          "3": "Geography", 
          "4": "History", 
          "5": "Entertainment", 
          "6": "Sports"
      }, 
      "success": true
  }

``` 
### GET /questions
- General: This endpoint returns a list questions. The results are paginated in groups of 10. The endpoint also returns list of categories and total number of questions. 

 - Sample: `curl http://127.0.0.1:5000/questions`
```
  {
      "categories": {
          "1": "Science", 
          "2": "Art", 
          "3": "Geography", 
          "4": "History", 
          "5": "Entertainment", 
          "6": "Sports"
      }, 
      "questions": [
          {
              "answer": "Colorado, New Mexico, Arizona, Utah", 
              "category": 3, 
              "difficulty": 3, 
              "id": 164, 
              "question": "Which four states make up the 4 Corners region of the US?"
          }, 
          {
              "answer": "Muhammad Ali", 
              "category": 4, 
              "difficulty": 1, 
              "id": 9, 
              "question": "What boxer's original name is Cassius Clay?"
          }, 
          {
              "answer": "Apollo 13", 
              "category": 5, 
              "difficulty": 4, 
              "id": 2, 
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          }, 
          {
              "answer": "Tom Cruise", 
              "category": 5, 
              "difficulty": 4, 
              "id": 4, 
              "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          }, 
          {
              "answer": "Edward Scissorhands", 
              "category": 5, 
              "difficulty": 3, 
              "id": 6, 
              "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
          }, 
          {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
          }, 
          {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
          }, 
          {
              "answer": "George Washington Carver", 
              "category": 4, 
              "difficulty": 2, 
              "id": 12, 
              "question": "Who invented Peanut Butter?"
          }, 
          {
              "answer": "Lake Victoria", 
              "category": 3, 
              "difficulty": 2, 
              "id": 13, 
              "question": "What is the largest lake in Africa?"
          }, 
          {
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
          }
      ], 
      "success": true, 
      "total_questions": 19
  }
```

### DELETE /questions/<int:id>
- General: This endpoint deletes a question based on a given ID if it exists. The endpoint returns the ID of the deleted question upon success.

 - Sample: `curl http://127.0.0.1:5000/questions/6 -X DELETE`
```
  {
      "deleted": 6, 
      "success": true
  }
```

### POST /questions/add

- General : This endpoint creates a new question using JSON request parameters. Returns JSON object with newly created question, as well as paginated questions.

- Sample: `curl http://127.0.0.1:5000/questions/add -X POST -H "Content-Type: application/json" -d '{ "question": "Which US state contains an area known as the Upper Penninsula?", "answer": "Michigan", "difficulty": 3, "category": "3" }'`

```
  {
      "created": 173, 
      "question_created": "Which US state contains an area known as the Upper Penninsula?", 
      "questions": [
          {
              "answer": "Apollo 13", 
              "category": 5, 
              "difficulty": 4, 
              "id": 2, 
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          }, 
          {
              "answer": "Tom Cruise", 
              "category": 5, 
              "difficulty": 4, 
              "id": 4, 
              "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          }, 
          {
              "answer": "Muhammad Ali", 
              "category": 4, 
              "difficulty": 1, 
              "id": 9, 
              "question": "What boxer's original name is Cassius Clay?"
          }, 
          {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
          }, 
          {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
          }, 
          {
              "answer": "George Washington Carver", 
              "category": 4, 
              "difficulty": 2, 
              "id": 12, 
              "question": "Who invented Peanut Butter?"
          }, 
          {
              "answer": "Lake Victoria", 
              "category": 3, 
              "difficulty": 2, 
              "id": 13, 
              "question": "What is the largest lake in Africa?"
          }, 
          {
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
          }, 
          {
              "answer": "Agra", 
              "category": 3, 
              "difficulty": 2, 
              "id": 15, 
              "question": "The Taj Mahal is located in which Indian city?"
          }, 
          {
              "answer": "Escher", 
              "category": 2, 
              "difficulty": 1, 
              "id": 16, 
              "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
          }
      ], 
      "success": true, 
      "total_questions": 20
  }

  ```

### POST /questions/search

- General: This endpoint handles all searches for questions using search term in JSON request parameters. Returns JSON object with paginated matching questions.

 - Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "which"}'`

```
  {
      "questions": [
          {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
          }, 
          {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
          }, 
          {
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
          }, 
          {
              "answer": "Agra", 
              "category": 3, 
              "difficulty": 2, 
              "id": 15, 
              "question": "The Taj Mahal is located in which Indian city?"
          }, 
          {
              "answer": "Escher", 
              "category": 2, 
              "difficulty": 1, 
              "id": 16, 
              "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
          }, 
          {
              "answer": "Jackson Pollock", 
              "category": 2, 
              "difficulty": 2, 
              "id": 19, 
              "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
          }, 
          {
              "answer": "Scarab", 
              "category": 4, 
              "difficulty": 4, 
              "id": 23, 
              "question": "Which dung beetle was worshipped by the ancient Egyptians?"
          }, 
          {
              "answer": "Michigan", 
              "category": 3, 
              "difficulty": 3, 
              "id": 173, 
              "question": "Which US state contains an area known as the Upper Penninsula?"
          }
      ], 
      "success": true, 
      "total_questions": 18
  }
```

### GET /categories/<int:id>/questions

- General: This endpoint retreieves questions based on category ID selected.Returns JSON object with paginated matching questions.

- Sample: `curl http://127.0.0.1:5000/categories/1/questions`
```

  {
      "current_category": "Science", 
      "questions": [
          {
              "answer": "The Liver", 
              "category": 1, 
              "difficulty": 4, 
              "id": 20, 
              "question": "What is the heaviest organ in the human body?"
          }, 
          {
              "answer": "Alexander Fleming", 
              "category": 1, 
              "difficulty": 3, 
              "id": 21, 
              "question": "Who discovered penicillin?"
          }, 
          {
              "answer": "Blood", 
              "category": 1, 
              "difficulty": 4, 
              "id": 22, 
              "question": "Hematology is a branch of medicine involving the study of what?"
          }
      ], 
      "success": true, 
      "total_questions": 18
  }
```

### POST /quizzes

 - General: This endpoint allows users to play the quiz game. It uses JSON request parameters of category and previous questions. Returns JSON object with random question not among previous questions.

 - Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "1"}}'`

```
  {
      "question": {
          "answer": "Blood", 
          "category": 1, 
          "difficulty": 4, 
          "id": 22, 
          "question": "Hematology is a branch of medicine involving the study of what?"
      }, 
      "success": true
  }
```

## Deployment 

Not applicable to this project. Project is deployed on local machine. 

## Authors
Mafusi Mokati authored the API (__init__.py), test suite (test_flaskr.py), and this README.

The rest of the project files were created by the brilliant team at Udacity as the starter code for project 2 of the Udacity Full Stack Web Developer Nanodegree program.  

## Acknowledgements 
Special thanks to Caryn for being such an amazing instructor and the awesome Udacity Mentors who are always willing to help out and assist us students with debugging our code and answering all our questions.  




