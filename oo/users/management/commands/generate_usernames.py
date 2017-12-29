import hashlib

from django.core.management import BaseCommand

from oo.users.models import User


class Command(BaseCommand):
    help = "Update users with User's Name."

    def handle(self, *args, **options):

        for user in User.objects.all():
            user.save()

        print('Done.')
