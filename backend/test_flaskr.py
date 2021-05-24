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
        self.database_name = "trivia_test"
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'Precious12!','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'Who was the first black women to go to space?',
            'answer':  'Mae Jemison',
            'category': "history",
            'difficulty': 5
        }


            
            
    

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        


    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_view_categories(self):
        "Test to verify that all categories are returned"
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))
        


    #def test_404_sent_requesting_invalid_url(self):
     #   res = self.client().get('/cateygories')
      #  data = json.loads(res.data)
#
       # self.assertEqual(res.status_code, 404)
        #self.assertEqual(data['success'], False)
        #self.assertEqual(data['message'], 'resource not found')

    def test_get_paginated_questions(self):
        "Test to verify all questions are returned"
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
   


    def test_404_sent_request_beyond_valid_page(self):
        "Test to fail the GET request on questions"
        res = self.client().get('/questions?page=400')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Resource not found!' )

    

    def test_create_new_question(self):
        "Test to verify that new question is added"
        res = self.client().post('/questions/add', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['questions']))
    




    def test_fail_422_create_new_question(self):
        "Test to fail adding a question"
        res = self.client().post('/questions/add', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
