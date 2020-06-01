# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET '/questions'
GET '/categories/<int:id>/questions'
POST '/questions/create'
POST '/questions'
POST '/questions/randomsearch'
POST '/quizzes'
DELETE '/questions/<int:id>'

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Fetches all lists of questions in which the keys are question, answer, difficulty, category and id
- Request Arguments: None
- Returns: An array of objects, in which including question: string , answer: string, difficulty: string, category: string, id : string pairs.
{
"answer": "Muhammad Ali",
"category": 4,
"difficulty": 1,
"id": 9,
 "question": "What boxer's original name is Cassius Clay?"
},

GET '/categories/<int:id>/questions'
- Fetch lists of question that in the same category in which the keys are question, answer, difficulty, category and id
- Request Arguments: id : Integer
- Returns An array of objects, in which including the question:string, answer:string, difficulty: string, category:string, id:string in same id of category
{
"answer": "The Liver",
"category": 1,
"difficulty": 4,
"id": 20,
"question": "What is the heaviest organ in the human body?"
},

POST '/questions/create'
- SEND an object including keys with questions: string, answer:string, category: string, difficulty: string to the server
- Request Arguments: NOne
- Return : After success create the data in the databse, a JSON with key success: True , and the all questions will be returned
{
"answer": "Muhammad Ali",
"category": 4,
"difficulty": 1,
"id": 9,
 "question": "What boxer's original name is Cassius Clay?"
}

POST '/questions'
- SEND an string in search_term to compare the value in all keys of questions
- Request Arugmnets: None
- Return : After success post the data , it returns the finding similar to the search_term words, as below search for "who"
{
"answer": "George Washington Carver",
"category": 4,
"difficulty": 2,
"id": 12,
"question": "Who invented Peanut Butter?"
},
{
"answer": "Alexander Fleming",
"category": 1,
"difficulty": 3,
"id": 21,
"question": "Who discovered penicillin?"
}

POST '/questions/randomsearch'
- SEND a string to get a question from all the return results in the specific category
- Request Argument: None
- Return: After success send the data, it returns a question that in the specific catagory in which including the question:string, answer:string, difficulty: string, category:string, id:string
{
"answer": "Jackson Pollock",
"category": 2,
"difficulty": 2,
"id": 19,
"question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
}

POST 'quizzes'
- SEND a string from 1 - 6 as the category number and array of previous question to get back a question in that category that did not repeat more than once
- Request Argument: None
- Return: After success send the data, it returns a question that in the specific catagory in which including the question:string, answer:string, difficulty: string, category:string, id:string , and the question just return once.
{
"answer": "Jackson Pollock",
"category": 2,
"difficulty": 2,
"id": 19,
"question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
}

ERROR HANDLING
The API will return four error types when request failed:
404: resource not found
422: unprocessable
400: bad request
405: method not allowed

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```