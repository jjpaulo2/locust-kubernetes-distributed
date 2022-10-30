from faker import Faker


def new_author() -> dict:
    fake = Faker()
    return {
        "name": fake.name(),
        "birth_date": fake.date()
    }

def new_author_name() -> dict:
    fake = Faker()
    return {
        "name": fake.name()
    }
