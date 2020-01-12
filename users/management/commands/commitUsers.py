from django.core.management.base import BaseCommand
import json
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        listObjects = []
        with open('users.json') as file:
            users = json.load(file)
        for user in users:
            userObject = User(
                user_id = user['id'],
                first_name = user['first_name'],
                last_name = user['last_name'],
                email = user['email'],
                gender = user['gender'],
                ip_address = user['ip_address']
                )
            listObjects.append(userObject)
        User.objects.bulk_create(listObjects)
