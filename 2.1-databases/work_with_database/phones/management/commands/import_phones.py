import slugify
from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # Преобразование данных перед сохранением
            Phone.objects.create(
                name=phone['name'],
                price=float(phone['price']),
                image=phone['image'],
                release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                lte_exists=bool(phone['lte_exists']),
                slug=slugify(phone['name'])
            )

        self.stdout.write(self.style.SUCCESS('Phones imported successfully'))