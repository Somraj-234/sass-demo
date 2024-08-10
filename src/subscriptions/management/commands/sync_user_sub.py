from typing import Any
import helper.billing
from django.core.management.base import BaseCommand, CommandParser
from subscriptions import utils as subs_utils

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--day-start",default=0, type=int)
        parser.add_argument("--day-end",default=0, type=int)
        parser.add_argument("--days-left",default=0, type=int)
        parser.add_argument("--days-ago",default=0, type=int)
        parser.add_argument("--clear-dangling",action="store_true",default=False)

    def handle(self, *args: Any, **options: Any):
       days_left = options.get("days_left")
       days_ago = options.get("days_ago")
       day_start = options.get("day_start")
       day_end = options.get("day_end")
       clear_dangling = options.get("clear_dangling")
       if clear_dangling:
        print("clearing dangling not in use active subs in stripe")
        subs_utils.clear_dangling_subs()
       else:
          print("sync active subs")
          done = subs_utils.refresh_active_users_subscriptions(
            active_only=True,
            days_ago=days_ago,
            days_left=days_left,
            day_start=day_start,
            day_end=day_end,
            verbose=True)
          if done:
            print("Done")
        
