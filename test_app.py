import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db
DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5433')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'admin')
DB_NAME = os.getenv('DB_NAME', 'trivia_test')

class CapstonTestCase(unittest.TestCase):

  def setUp(self):
    """Define test variables and initialize app."""
    self.app = create_app()
    self.client = self.app.test_client
    self.database_name = "trivia_test"
    self.database_path = "postgresql+psycopg2://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
    self.new_movie = {"question":"a is ?","answer":"b","category":1,"difficulty":2}
    

    # binds the app to the current context
    with self.app.app_context():
        self.db = SQLAlchemy()
        self.db.init_app(self.app)
        setup_db(self.app, self.database_path)
          
  
  def tearDown(self):
    """Executed after reach test"""
    pass
  
  def test_404_sent_requesting_beyond_valid_page(self):
    res = self.client().get("/movies/1")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "resource not found")
  
  def test_get_movies(self):
    res = self.client().get("/movies")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["movies"])
  
  def test_delete_movies(self):
    res = self.client().delete("movies/5")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    
  def test_create_movies(self):
    res = self.client().post("movies", json=self.new_movie)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)

  def test_update_movies(self):
    res = self.client().patch("movies", json=self.new_movie)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)

  
  def test_get_actors(self):
    res = self.client().get("/actors")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["actors"])
  
  def test_delete_actors(self):
    res = self.client().delete("actors/5")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    
  def test_create_actors(self):
    res = self.client().post("actors", json=self.new_actor)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)

  def test_update_actors(self):
    res = self.client().patch("actors", json=self.new_actor)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()