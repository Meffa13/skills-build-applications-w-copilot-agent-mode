from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T')
        u = User.objects.create(name='U', email='u@example.com', team=team)
        self.assertEqual(str(u), 'U')
    def test_activity_create(self):
        team = Team.objects.create(name='T')
        u = User.objects.create(name='U', email='u@example.com', team=team)
        a = Activity.objects.create(user=u, type='Run', duration=10, date='2026-01-12')
        self.assertEqual(str(a), 'U - Run')
    def test_workout_create(self):
        t = Team.objects.create(name='T')
        w = Workout.objects.create(name='W')
        w.suggested_for.set([t])
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='T')
        u = User.objects.create(name='U', email='u@example.com', team=t)
        l = Leaderboard.objects.create(user=u, score=1, rank=1)
        self.assertIn('U', str(l))
