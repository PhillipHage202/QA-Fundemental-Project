import unittest 
from flask import url_for
from flask_testing import TestCase
from application.models import Workout_plan, Session
from application import app, db 


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
			SECRET_KEY='TEST_SECRET_KEY',
			DEBUG=True
			)
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        #Create Test registree
        name = Workout_plan(name='Sob')
        session = Session(pushups='2', comment='i did this in 10seconds')
        
        #Save workout plan & session to the database
        db.session.add(name)
        db.session.add(session)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_addPlan_get(self):
        response = self.client.get(url_for('addPlan'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('index', id=1))
        self.assertEqual(response.status_code, 200)

    def test_addSession_get(self):
        response = self.client.get(url_for('addSession', id=1))
        self.assertEqual(response.status_code, 200)

    def test_Viewpage_get(self):
        response = self.client.get(url_for('Viewpage', id=1))
        self.assertEqual(response.status_code, 200)

#Test Adding a name
class TestAdd(TestBase):
    def test_add_name(self):
        response = self.client.post(
		url_for('addPlan', id=1),
		data = dict(name='bobby')
	)
        self.assertIn(b'bobby', response.data)

#Test Updating a name
class TestUpdate(TestBase):
    def test_update_name(self):
        response = self.client.post(
		url_for('update', id=1),
                data = dict(oldname='booby', newname='bobby'),
		follow_redirects=True
        	)
        self.assertEqual(response.status_code, 200)

#Test Deleting a name
class TestDelete(TestBase):
    def test_delete_name(self):
        response = self.client.post(
		url_for('index', id=1),
		data = dict(name='Size'),
		follow_redirects=True
		)
        self.assertEqual(response.status_code,200)

#Test Adding a session
class TestAddreview(TestBase):
    def test_add_session(self):
        response = self.client.post(
		url_for('addSession', id=1),
		data = dict(pushups='1000', comment='i did not do this')
		)
        self.assertIn(b'1000', response.data)
        self.assertIn(b'i did not do this', response.data)

#Test Viewpage
class TestViewpage(TestBase):
    def test_Viewpage(self):
        response = self.client.post(
                url_for('Viewpage', id=1),
                data = dict(name='bobby'),
                follow_redirects=True
                )
        self.assertEqual(response.status_code,200)