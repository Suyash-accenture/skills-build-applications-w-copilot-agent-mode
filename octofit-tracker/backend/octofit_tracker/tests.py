
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
	def test_user_list(self):
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class TeamTests(APITestCase):
	def test_team_list(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class ActivityTests(APITestCase):
	def test_activity_list(self):
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class WorkoutTests(APITestCase):
	def test_workout_list(self):
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class LeaderboardTests(APITestCase):
	def test_leaderboard_list(self):
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
