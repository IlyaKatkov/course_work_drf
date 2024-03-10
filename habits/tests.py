from rest_framework.test import APITestCase
from rest_framework import status
from habits.models import Habit
from users.models import User


class HabitAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            name="testuser",
            email="testuser@test.com",
            telegram_chat_id="@testtelegram",
            password='12345'
        )
        self.habit = Habit.objects.create(
            id=100,
            user=self.user,
            place="home",
            time="12:00",
            action="not drink alcohol",
            reward="15 DKK",
            periodicity=1,
            is_public=False,
            duration_time="00:00:30",
        )

    def test_get_list_habits(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/habit/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_habit(self):
        data = {
            "user": self.user.pk,
            "place": "home",
            "time": "12:00",
            "action": "drink water",
            "reward": "10 DKK",
            "periodicity": 1,
            "is_public": False,
            "duration_time": "00:01",
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/habit/create/',
            data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_habit(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            '/habit/delete/100/')
        print(response)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_get_list_public_habits(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/habit/public/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
