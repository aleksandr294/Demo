from django.core.management.base import BaseCommand
import json
from users.models import Statistic

class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        listObjects = []
        with open('users_statistic.json') as file:
            usersStatistic = json.load(file)
        for userStat in usersStatistic:
            statistic = Statistic(
                user_id = userStat['user_id'],
                date = userStat['date'],
                page_views = userStat['page_views'],
                clicks = userStat['clicks']
            )
            listObjects.append(statistic)
        Statistic.objects.bulk_create(listObjects)
            
