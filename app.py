
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import setup_db,Movie,Actor
from flask_cors import CORS
import sys
from auth.auth import AuthError, requires_auth
import babel
import dateutil.parser


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

  def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format="EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format="EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')

    app.jinja_env.filters['datetime'] = format_datetime
  '''
      GET /Movies
  '''
  # Get All movies
  @app.route("/movies", methods=["GET"])
  @requires_auth("get:movies")
  def get_movies(payload):

      movies = Movie.query.all()
      formatted_movies = [movie.format() for movie in movies]
      return jsonify(
          {
              "success": True,
              "movies": formatted_movies
          }
      )


  '''

      POST /movies

  '''
    # Create new movies 
  @app.route("/movies", methods=["POST"])
  @requires_auth("post:movies")
  def create_movie(payload):
      
      body = request.get_json()
      try:
          title = body.get("title", None)
          releaseDate = body.get("release_date", None)
          movie_new = Movie(title=title,release_date=releaseDate)
          movie_new.insert()

          movies = Movie.query.all()
          formatted_movies = [movie.format() for movie in movies]
          return jsonify(
              {
                  "success": True,
                  "movies": formatted_movies
              }
          )
      except:
          print(sys.exc_info())
          abort(422)

  '''
 
      PATCH /movies/<id>
  '''
  # Get movies 
  @app.route("/movies/<int:movie_id>", methods=["PATCH"])
  @requires_auth("patch:movies")
  # @cross_origin
  def update_movies(payload, movie_id):
      try:
          movie = Movie.query.get(movie_id)
          if movie is None:
              abort(404)
          
          body = request.get_json()
          title = body.get("title", None)
          releaseDate = body.get("release_date", None)
          movie.title = title
          movie.recipe = releaseDate
          movie.update()
          movies = Movie.query.all()
          formatted_movies = [movie.format() for movie in movies]
          return jsonify(
              {
                  "success": True,
                  "movies": formatted_movies
              }
          )
      except:
          print(sys.exc_info())
          abort(422)

  '''

      DELETE /movies/<id>

  '''
  # Delete drinks
  @app.route("/movies/<int:movie_id>", methods=["DELETE"])
  @requires_auth("delete:movies")
  # @cross_origin
  def delete_movies(payload,movie_id):
      try:
          movie = Movie.query.get(movie_id)
          if movie is None:
              abort(404)
          movie.delete()
          return jsonify(
              {
                  "success": True,
                  "movie":movie_id
              }
          )
      except:
          print(sys.exc_info())
          abort(422)


  '''
      GET /Actors
  '''
  # Get All movies
  @app.route("/actors", methods=["GET"])
  @requires_auth("get:actors")
  def get_actors(payload):

      actors = Actor.query.all()
      formatted_actors = [actor.format() for actor in actors]
      return jsonify(
          {
              "success": True,
              "actors": formatted_actors
          }
      )


  '''

      POST /actors

  '''
    # Create new actors 
  @app.route("/actors", methods=["POST"])
  @requires_auth("post:actors")
  def create_actor(payload):
      print('1')
      body = request.get_json()
      try:
          name = body.get("name", None)
          age = body.get("age", None)
          gender = body.get("age", None)
          actor_new = Actor(name=name,age=age,gender=gender)
          actor_new.insert()
        
          actors = Actor.query.all()
          formatted_actors = [actor.format() for actor in actors]
          return jsonify(
              {
                  "success": True,
                  "actors": formatted_actors
              }
          )
      except:
          print(sys.exc_info())
          abort(422)

  '''
  @TODO implement endpoint
      PATCH /actors/<id>
  '''
  # Get movies 
  @app.route("/actors/<int:actor_id>", methods=["PATCH"])
  @requires_auth("patch:actors")
  # @cross_origin
  def update_actors(payload, actor_id):
      try:
          actor = Actor.query.get(actor_id)
          if actor is None:
              abort(404)
          
          body = request.get_json()
          name = body.get("name", None)
          age = body.get("age", None)
          gender = body.get("age", None)
          actor.name = name
          actor.age = age
          actor.gender = gender
          actor.update()
          actors = Actor.query.all()
          formatted_actors = [actor.format() for actor in actors]
          return jsonify(
              {
                  "success": True,
                  "actors": formatted_actors
              }
          )
      except:
          print(sys.exc_info())
          abort(422)

  '''
  @TODO implement endpoint
      DELETE /actors/<id>

  '''
  # Delete drinks
  @app.route("/actors/<int:actor_id>", methods=["DELETE"])
  @requires_auth("delete:actors")
  # @cross_origin
  def delete_actors(payload,actor_id):
      try:
          actor = Actor.query.get(actor_id)
          if actor is None:
              abort(404)
          actor.delete()
          return jsonify(
              {
                  "success": True,
                  "Actor":actor_id
              }
          )
      except:
          print(sys.exc_info())
          abort(422)

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
      }), 422

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404
 
  @app.errorhandler(AuthError)
  def invalid_claims(ex):
      return jsonify({
                      "success": False,
                      "error": ex.status_code,
                      "message": ex.error
                      })
  return app
app = create_app()

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))