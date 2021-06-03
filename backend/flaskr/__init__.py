import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random
from models import setup_db, Question, Category


"""
----------------------------------------------------------------
Paginate_questions helper method.
-------------------------------------------------------------------
"""
QUESTIONS_PER_PAGE = 10
# function to enable pagination in the "Get" endpoint


def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formatted_questions = [question.format() for question in selection]
    current_questions = formatted_questions[start:end]
    return current_questions


"""
--------------------------------------------
App configuration
--------------------------------------------
"""


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/endpoint/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    # ---------------------------------------------------------------------
    # View_Categories Endpoint: uses GET method to retrieve
    # and display all categories from the database.

    # ---------------------------------------------------------------------

    @app.route("/categories")
    def view_categories():
        categories = Category.query.all()
        formatted_categories = {
            category.id: category.type for category in categories}
        if len(formatted_categories) == 0:
            abort(404)
            return jsonify({"success": False})
        return jsonify(
            {
                "success": True,
                "categories": formatted_categories,
                "total_categories": len(Category.query.all()),
            }
        )

    # ----------------------------------------------------------------------------
    # View_Questions Endpoint: uses GET method to retrieve questions from the
    # database. Function includes pagination and displays results as
    # 10 questions per page.
    # ----------------------------------------------------------------------------

    @app.route("/questions")
    def view_questions():
        selection = Question.query.all()
        current_questions = paginate_questions(request, selection)
        if len(current_questions) == 0:
            abort(404)
            return jsonify({"success": False})
        # Provide list of categories
        categories = Category.query.all()
        formatted_categories = {
            category.id: category.type for category in categories}
        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(Question.query.all()),
                "categories": formatted_categories,
                "currentCategory": None,
            }
        )

    # ---------------------------------------------------------------------------------------------------
    # Delete_Question Endpoint: uses DELETE method to delete a question from
    # the database based on the question ID.
    # ---------------------------------------------------------------------------------------------------

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()
            if question is None:
                abort(404)
            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify(
                {
                    "success": True,
                    "deleted": question.id,
                    "questions": current_questions,
                    "total_questions": len(Question.query.all()),
                }
            )
        except Exception:
            abort(422)

    # ----------------------------------------------------------------------------
    # Create_Question Endpoint: uses POST method to add a new question in the
    # database using JSON object.
    # Requires answer, question, category and difficulty score
    #  from question form.
    # ----------------------------------------------------------------------------

    @app.route("/questions/add", methods=["POST"])
    def create_question():
        body = request.get_json()

        try:
            new_question = body.get("question", None)
            new_answer = body.get("answer", None)
            new_category = body.get("category", None)
            new_difficulty = body.get("difficulty", None)

            if (
                (new_question is None)
                or (new_answer is None)
                or (new_difficulty is None)
                or (new_category is None)
            ):
                abort(422)

            question = Question(
                question=new_question,
                answer=new_answer,
                category=new_category,
                difficulty=new_difficulty,
            )

            question.insert()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "created": question.id,
                    "questions": current_questions,
                    "total_questions": len(Question.query.all()),
                }
            )
        except Exception:
            abort(422)

    # ---------------------------------------------------------------------------
    # Search_Question Endpoint: uses POST method to  get questions based on
    #  a search term.
    # ----------------------------------------------------------------------------

    @app.route("/questions/search", methods=["POST"])
    def search_question():
        body = request.get_json()
        search_term = body.get("searchTerm", None)
        print(search_term)

        try:
            if search_term:
                selection = Question.query.filter(
                    Question.question.ilike(f"% {search_term} %")
                ).all()

                current_questions = paginate_questions(request, selection)

            if len(selection) == 0:
                abort(404)

            if search_term is None:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "total_questions": len(selection),
                    "current_category": None,
                }
            )

        except Exception:
            abort(404)

    # ---------------------------------------------------------------------------
    # View_Question_By_Category Endpoint: uses GET method to delete a question
    # from the database based on the question ID.
    # ----------------------------------------------------------------------------

    @app.route("/categories/<int:category_id>/questions")
    def view_questions_by_category(category_id):
        body = request.get_json()

        try:

            questions = Question.query.filter(Question.category ==
                                              str(category_id))

            current_questions = paginate_questions(request, questions)

            if len(current_questions) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "total_questions": len(current_questions),
                    "current_category": category_id,
                }
            )

        except Exception:
            abort(404)

    # ----------------------------------------------------------------------------
    # Play_Quiz Endpoint: uses POST method to get questions to play the quiz.
    # Takes category and previous question parameters and returns
    # random questions within the given category, if given, that is not one of
    # the previous questions.
    # ----------------------------------------------------------------------------

    @app.route("/quizzes", methods=["POST"])
    def play_quiz():
        body = request.get_json()

        previous_questions = body.get("previous_questions", [])
        quiz_category = body.get("quiz_category", None)

        try:

            if quiz_category:

                if quiz_category["id"] == 0:
                    quiz = Question.query.all()

                else:
                    quiz = Question.query.filter_by(
                        category=quiz_category["id"]).all()

                if not quiz:
                    return abort(422)
                print(quiz)

            selected = []

            for question in quiz:
                if question.id not in previous_questions:
                    selected.append(question.format())

            if len(selected) != 0:
                result = random.choice(selected)
                return jsonify({"success": True, "question": result})

            else:
                return jsonify({"question": False})

        except Exception:
            abort(422)
    # ---------------------------------------------------------------------------------------------------
    # Error Handlers : put in place to handle all expected errors.
    # 404: Used when the resource can be found.
    # 422: Used when the request is unprocessable
    # ---------------------------------------------------------------------------------------------------

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({
                "success": False,
                "error": 404,
                "message": "Resource not found!"}),
            404,
        )

    @app.errorhandler(422)
    def unproccesable(error):
        return (
            jsonify({
                "success": False,
                "error": 422,
                "message": "Unprocessable"}),
            422,
        )

    # ---------------------------------------------
    # Return app: used to run the Flask app.
    # ----------------------------------------------
    return app
