from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='almaz@sky.pro',
            name='almaz',
            telegram_chat_id='123456',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password('admin')
        user.save()