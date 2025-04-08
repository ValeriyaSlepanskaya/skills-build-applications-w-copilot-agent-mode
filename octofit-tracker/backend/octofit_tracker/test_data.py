from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

# Create test data for the application

test_users = [
    {"email": "thundergod@mhigh.edu", "name": "Thor", "age": 30},
    {"email": "metalgeek@mhigh.edu", "name": "Tony Stark", "age": 45},
    {"email": "zerocool@mhigh.edu", "name": "Steve Rogers", "age": 100},
    {"email": "crashoverride@hmhigh.edu", "name": "Bruce Banner", "age": 40},
    {"email": "sleeptoken@mhigh.edu", "name": "Natasha Romanoff", "age": 35},
]

test_teams = [
    {"name": "Blue Team", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu"]},
    {"name": "Gold Team", "members": ["zerocool@mhigh.edu", "crashoverride@hmhigh.edu", "sleeptoken@mhigh.edu"]},
]

test_activities = [
    {"user_email": "thundergod@mhigh.edu", "type": "Cycling", "duration": timedelta(hours=1)},
    {"user_email": "metalgeek@mhigh.edu", "type": "Crossfit", "duration": timedelta(hours=2)},
    {"user_email": "zerocool@mhigh.edu", "type": "Running", "duration": timedelta(hours=1, minutes=30)},
    {"user_email": "crashoverride@hmhigh.edu", "type": "Strength", "duration": timedelta(minutes=30)},
    {"user_email": "sleeptoken@mhigh.edu", "type": "Swimming", "duration": timedelta(hours=1, minutes=15)},
]

test_leaderboard = [
    {"user_email": "thundergod@mhigh.edu", "score": 100},
    {"user_email": "metalgeek@mhigh.edu", "score": 90},
    {"user_email": "zerocool@mhigh.edu", "score": 95},
    {"user_email": "crashoverride@hmhigh.edu", "score": 85},
    {"user_email": "sleeptoken@mhigh.edu", "score": 80},
]

test_workouts = [
    {"user_email": "thundergod@mhigh.edu", "description": "Cycling Training", "date": "2025-04-08"},
    {"user_email": "metalgeek@mhigh.edu", "description": "Crossfit Training", "date": "2025-04-08"},
    {"user_email": "zerocool@mhigh.edu", "description": "Running Training", "date": "2025-04-08"},
    {"user_email": "crashoverride@hmhigh.edu", "description": "Strength Training", "date": "2025-04-08"},
    {"user_email": "sleeptoken@mhigh.edu", "description": "Swimming Training", "date": "2025-04-08"},
]

def create_test_data():
    # Create Users
    user1 = User.objects.create(username="john_doe", email="john@example.com", password="password123")
    user2 = User.objects.create(username="jane_doe", email="jane@example.com", password="password456")

    # Create Teams
    team1 = Team.objects.create(name="Team Alpha")
    team1.members.add(user1, user2)

    # Create Activities
    Activity.objects.create(user=user1, activity_type="Running", duration="00:30:00")
    Activity.objects.create(user=user2, activity_type="Cycling", duration="01:00:00")

    # Create Leaderboard entries
    Leaderboard.objects.create(user=user1, score=100)
    Leaderboard.objects.create(user=user2, score=150)

    # Create Workouts
    Workout.objects.create(name="Morning Yoga", description="A relaxing morning yoga session.")
    Workout.objects.create(name="HIIT", description="High-Intensity Interval Training.")

if __name__ == "__main__":
    create_test_data()