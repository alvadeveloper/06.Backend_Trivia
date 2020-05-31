import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    new_question = {
                "success" :True,
                "questions": "who is larry",
                "answer": "larry",
                "category": "1",
                "difficulty": "1"
                }

    quizquestion = {
               'previous_questions': [1, 2],
                'quiz_category': {
                'type': 'Science',
                'id': 1
                }
                }

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(len(data['categories']))


    def test_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

    def test_categories_withid(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

    # please change id to test delete function

    def test_delete_book(self):
        res = self.client().delete('/questions/1')
        data = json.loads(res.data)
        
        question = Question.query.filter(Question.id == 1).one_or_none()

        print (data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(question, None)

    def test_create_new_question(self):
        res = self.client().post('/questions/create', json=self.new_question)
        data = json.loads(res.data)
            
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

    def test_return_searchresult(self):
        res = self.client().post('/questions', json={"question" : "who"})
        data = json.loads(res.data)
            
        self.assertEqual(res.status_code, 200)


    def test_questions_randomsearch(self):
        res = self.client().post('/questions/randomsearch', json={"category" : "1"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['data']))


    def test_quizzes(self):
        res = self.client().post('/quizzes', json=self.quizquestion)
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['question']) 
        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()