import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random

from models import  setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

# function to enable pagination in the "Get" endpoint
def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  formatted_questions = [question.format() for question in selection]
  current_questions = formatted_questions[start:end]

  return current_questions


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors= CORS(app, resources={r"/endpoint/*": {"origins":"*"}})
 # CORS(app)

 # '''
  #@TODO: Set up CORS. Allow '*' for origins.[done] Delete the sample route after completing the TODOs
  #'''


  #'''
  #@TODO: Use the after_request decorator to set Access-Control-Allow [done]
  #'''
  @app.after_request
  def after_request(response):
          response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
          response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
          return response



#  '''
 # @TODO:
  #Create an endpoint to handle GET requests
  #for all available categories.
  #'''
  @app.route('/categories')
  def view_categories():
      categories = Category.query.all()
      formatted_categories = {category.id:category.type for category in categories}

      if len(formatted_categories) == 0:
          abort(404)
          return jsonify({
          'success':False

       })

      return jsonify({
      'success':True,
      'categories': formatted_categories,
      'total_categories': len(Category.query.all())

       })





#  '''
 # @TODO: done
  #Create an endpoint to handle GET requests for questions,
  #including pagination (every 10 questions).
  #This endpoint should return a list of questions,
  #number of total questions, current category, categories.

  #TEST: At this point, when you start the application
  #you should see questions and categories generated,
  #ten questions per page and pagination at the bottom of the screen for three pages.
  #Clicking on the page numbers should update the questions.
  #'''

  @app.route('/questions')
  def view_questions():
    selection = Question.query.all()
    current_questions = paginate_questions(request, selection)

    if len(current_questions) == 0:
      abort(404)
      return jsonify({
        'success':False
      })

    #Provide list of categories
    categories = Category.query.all()
    formatted_categories = {category.id:category.type for category in categories}

    return jsonify ({
      'success':True,
      'questions': current_questions,
      'total_questions': len(Question.query.all()),
      'categories': formatted_categories,
      'currentCategory': None
    })

  #'''
  #@TODO:
  #Create an endpoint to DELETE question using a question ID.

  @app.route('/questions/<int:question_id', methods=['DELETE'])
  def delete_question(question_id):
      try:
          question = Question.query.filter(Question.id == question_id).one_or_none()



      if question is None:
          abort(404)

        question.delete()
        selection= Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

    return jsonify({
    'success': True,
    'deleted': question_id,
    'questions': current_questions,
    'total_questions': len(Question.query.all())

    })

except:
    abort(422)




  #TEST: When you click the trash icon next to a question, the question will be removed.
  #This removal will persist in the database and when you refresh the page.
  #'''

  #'''
  #@TODO:
  #Create an endpoint to POST a new question,
  #which will require the question and answer text,
  #category, and difficulty score.
  @app.route('/questions', methods=['POST'])
  def create_question():
      body = request.get_json()

      new_questions = body.get('question', None)
      new_answer = body.get('answer', None)
      new_category = body.get('category', None)
      new_difficulty = body.get('difficulty', None)

      try:
          question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
          question.insert()

          selection = Question.query.order_by(question.id).all()
          current_questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'created': question.id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      })

    except:
      abort(422)



  #TEST: When you submit a question on the "Add" tab,
  #the form will clear and the question will appear at the end of the last page
  #of the questions list in the "List" tab.
  #'''

  #'''
  #@TODO:
  #Create a POST endpoint to get questions based on a search term.
  #It should return any questions for whom the search term
  #is a substring of the question.
 @app.route('/questions', methods=['POST'])
  def add_question():
    body = request.get_json()
    try:
      new_search = body.get('searchTerm',None)
      #If no search term a new question is being added
      if new_search is None:

        new_question = body.get('question',None)
        new_answer = body.get('answer',None)
        new_category = body.get('category',None)
        new_difficulty = body.get('difficulty',None)
        #Build new question from model
        question = Question(question=new_question,answer=new_answer,category=new_category,difficulty=new_difficulty)
        #Insert question into the DB
        question.insert()

        return jsonify({
          'success':True
        })

    #Search is being performed
      else:
        question_results = Question.query.filter(Question.question.ilike('%'+new_search+'%'))
        current_results = paginate_questions(request,question_results)

        return jsonify({
          'success':True,
          'questions':current_results,
          'total_questions':len(question_results.all()),
          'current_category':{}
        })
    except:
      abort(422)

  #TEST: Search by any phrase. The questions list will update to include
  #only question that include that string within their question.
  #Try using the word "title" to start.
  #'''

  #'''
  #@TODO:
  #Create a GET endpoint to get questions based on category.

  @app.route('/categories/<int:category_id>/questions')
  def view_questions_by_category(category_id):
      questions = Question.query.filter(Question.category == str(category_id)).all()
      current_questions = paginate_questions(request, questions)

      if len(current_questions) == 0:
        abort(404)

      return jsonify({
        'success':True,
        'questions':current_questions,
        'total_questions':len(questions),
        'current_category':category_id
      })







  #TEST: In the "List" tab / main screen, clicking on one of the
  #categories in the left column will cause only questions of that
  #category to be shown.
  #'''


  #'''
  #@TODO:
  #Create a POST endpoint to get questions to play the quiz.
  #This endpoint should take category and previous question parameters
  #and return a random questions within the given category,
  #if provided, and that is not one of the previous questions.
@app.route('/quizzes', methods=['POST'])
def play_quiz():
    #Init previous_questions to handle first question
    previous_questions = []
    body = request.get_json()
    try:
      #Get category id
      cat_id = body['quiz_category']['id']
      #A different way to get something from JSON
      previous_questions = body.get('previous_questions', None)
      #If ALL categories is selected
      if cat_id == 0:
        quiz_questions = Question.query.all()
      #Else filter questions by cat_id
      else:
        quiz_questions = Question.query.filter(Question.category == cat_id).all()

      #Decide if the quiz is finished
      if len(previous_questions) == len(quiz_questions):
        return jsonify({
          'success':True,
          'question':False
        })
      #Randomly select a question that hasn't been asked
      else:
        current_question = random.choice([question for question in quiz_questions if question.id not in previous_questions])
        previous_questions.append(current_question.id)
        return jsonify({
          'success':True,
          'question':{
            'question':current_question.question,
            'answer':current_question.answer,
            'id':current_question.id,
            'category':current_question.category,
            'difficulty':current_question.difficulty
            }
        })
    except:
      abort(422)



  #TEST: In the "Play" tab, after a user selects "All" or a category,
  #one question at a time is displayed, the user is allowed to answer
  #and shown whether they were correct or not.
  #'''

  #'''
  #@TODO:
  #Create error handlers for all expected errors
  #including 404 and 422.
  #'''

    #Error handler creation
@app.errorhandler(404)
def not_found(error):

        return jsonify({
            'success':False,
            'error':404,
            'message':'Resource not found!'
        }),404

  @app.errorhandler(422)
   def unproccesable(error):
      return jsonify({
            'success':False,
            'error':422,
            'message':'Unprocessable'
        }),422


  return app
