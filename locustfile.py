from locust import HttpUser, task, between
import json
import random


# Creating an API User class inheriting from Locust's HttpUser class
class APIUser(HttpUser):
    # Setting the host name and wait_time
    host = 'http://127.0.0.1:8000/api'
    wait_time = between(3, 5)

    # 개인화 추천 테스트
    @task(1)
    def person_test(self):
        authorization = 'Token da66d43802bbc7cfe49df8cb62582036aa3ce1f3'

        with open('user_item.json', 'rb') as f:
            data = json.load(f)
        data = random.choice(list(data.keys()))

        url = '/person/?user_id='+data
        self.client.get(url=url,
                        auth=None,
                        headers={'Authorization': authorization})
