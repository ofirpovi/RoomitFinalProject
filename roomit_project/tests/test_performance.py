import random

from locust import HttpUser, between, task
from datetime import date
# Your personal details have been saved and your profile has been created. You can see your profile and edit it at any time by clicking on the 'profile' tab on the top right of the screen.


class test_performance(HttpUser):
    wait_time = between(5, 15)
    usernames = []

    def on_start(self):
        username = f"username{self.environment.runner.user_count}{random.randrange(500)}"

        # Register a new user with a unique identifier
        while username in self.usernames:
            username = f"username{self.environment.runner.user_count}{random.randrange(500)}"

        password = "mypes12345"
        email = f"{username}@gmail.com"
        response = self.client.get('user/register/')
        csrftoken = response.cookies['csrftoken']

        response = self.client.post("user/register/", {"username": username, "password1": password, "password2": password, "email": email}, headers={'X-CSRFToken': csrftoken})

        # Check that the register was successful
        response = self.client.get('user/register/')
        csrftoken = response.cookies['csrftoken']
        response = self.client.post(
            f"user/fill_info/{username}/",
            {"first_name": username, "last_name": "levi", "birthdate": date(1990, 1, 1), "phone_number": "+12125552368", "gender": random.choice(['F', 'M', 'N'])}, headers={'X-CSRFToken': csrftoken}
        )

        response = self.client.get(
            f"user/set-status/",
            {"status": random.choice(['StatusInsert', 'StatusEnter'])},
        )

    @task
    def view_homepage(self):
        self.client.get("")

    @task(2)
    def view_profile(self):
        self.client.get(f'user/profile/{random.choice(self.usernames)}/')

