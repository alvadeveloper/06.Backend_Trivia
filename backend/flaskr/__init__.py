import os
from flask import Flask, request, abort, jsonify, request
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

# Get all Questions

  @app.route('/questions', methods=['GET'])
  def get_messages():
    page = request.args.get('page' , 1 , type=int)
    start = (page - 1)* 10
    end = start + 10
    data = Question.query.all()
    formatted_data = [d.format() for d in data]

    return jsonify({
        "questions": formatted_data[start:end],
        "categories": formatted_data[start:end],
        "totalQuestions": len(formatted_data[start:end])
      })

# Get question based on question id

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_message(question_id):
    data = Question.query.filter(Question.id == question_id).one_or_none()

    if data is None:
      abort(404)

    data.delete();

    page = request.args.get('page' , 1 , type=int)
    start = (page - 1)* 10
    end = start + 10
    data = Question.query.all()
    formatted_data = [d.format() for d in data]

    return jsonify({
        'data': formatted_data[start:end]
      })

 #  Create Question
  @app.route('/questions/create', methods=['POST'])
  def create_message():
    

          body = request.get_json()

          new_question = body.get('question')
          new_answer = body.get('answer')
          new_category = body.get('category')
          new_difficulty = body.get('difficulty')

          print(body)

  
          questions = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
          questions.insert()

          page = request.args.get('page' , 1 , type=int)
          start = (page - 1)* 10
          end = start + 10
          data = Question.query.all()
          formatted_data = [d.format() for d in data]

          return jsonify({
            'success': True,
             'created': formatted_data
           })


  #  Get questions based on search 

  @app.route('/questions', methods=['POST'])
  def search():

      body = request.get_json()

      print(body)

      search_term = body.get('searchTerm')
      results = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
      page = request.args.get('page' , 1 , type=int)
      start = (page - 1)* 10
      end = start + 10
      formatted_data = [d.format() for d in results]

      return jsonify ({
        "questions": formatted_data[start:end],
        "categories": formatted_data[start:end]
        })

  # Get questions based on category

  @app.route('/categories/<int:id>/questions', methods=['GET'])
  def search_category(id):

      search_term = id
      results = Question.query.filter(Question.category == search_term).all()
      page = request.args.get('page' , 1 , type=int)
      start = (page - 1)* 10
      end = start + 10
      formatted_data = [d.format() for d in results]

      return jsonify ({
        "questions": formatted_data[start:end],
        "categories": formatted_data[start:end]
        })

  # Random search

  @app.route('/questions/randomsearch', methods=['POST'])
  def random_search():

      body = request.get_json()

      search_term = body.get('category')
      print (type(search_term))
      results = Question.query.filter(Question.category == search_term).all()
      formatted_data = [d.format() for d in results]
      question = random.choice(formatted_data)

      return jsonify ({
          'data': question
        })

  # error handling

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message' : 'resource not found'
    }), 404


  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message' : 'unprocessable'
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message' : 'bad request'
    }), 400

  @app.errorhandler(405)
  def methodnotallowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message' : 'method not allowed'
    }), 405


  return app

    