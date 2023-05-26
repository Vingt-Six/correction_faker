from django_seed import Seed
from .models import Employee
import random

departement = ["Marketing", "Communication", "Comptabilité", "Designer", "Web-Dev"]

def run():
    seeder = Seed.seeder()
    seeder.add_entity(Employee, 30, {
        "name": lambda x: seeder.faker.last_name(),
        "firstname": lambda x: seeder.faker.first_name(),
        "email": lambda x: seeder.faker.email(),
        "date_embauche": lambda x: seeder.faker.date_between(start_date="-13y", end_date='now'),
        "salaire": lambda x: random.randint(20000, 50000),
        "departement": lambda x: random.choice(departement),
    })
    print(seeder.execute())