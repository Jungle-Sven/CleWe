"""
create_test_data() - наполняет таблицы тестовыми данными.
delete_test_data() - удаляет тестовые данные.
"""
import random
from faker import Faker

fake = Faker()

def migrate():
    from alembic.config import Config
    from alembic import command

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


def create_test_data():
    from datetime import date
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from app.core.config import settings
    from app import models

    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

    Session = sessionmaker(
        engine,
        autocommit=False,
        autoflush=False,
    )

    users = [
        models.User(
            nickname=fake.name(),
            wallet_address=fake.word(),
            level=random.randint(1, 5),
            level_total_exp=random.randint(1, 5),
            exp_to_next_level=random.randint(1, 5),
        ) for _ in range(10)
    ]

    trophies = [
        models.Trophy(
            user_id=users[i].id,
            tx_hash=f'fake hash: {i}',
            img_url=fake.url(),
            description=fake.word(),
        ) for i in range(len(users))
    ]

    skills = [
        models.Skill(
            user_id=users[i].id,
            topic=fake.word(),
            title=fake.word(),
            level=random.randint(1, 5),
            experience=random.randint(1, 5),
        ) for i in range(len(users))
    ]

    quests = [
        models.Quest(
            name=fake.word(),
            slug=f'slug: {i}',
            topic=fake.word(),
            skill_reward=random.randint(1, 5),
            description=fake.word(),
            difficulty=random.randint(1, 5),
            exp_reward=random.randint(1, 5),
        ) for i in range(len(users))
    ]

    with Session() as session:
        try:
            session.bulk_save_objects(objects=users)
            session.bulk_save_objects(objects=trophies)
            session.bulk_save_objects(objects=skills)
            session.bulk_save_objects(objects=quests)


            for i in range(len(users)):
                users[i].completed_quests.append(quests[i])
            session.commit()
            print(f"All tables are filled")
        except Exception as exc:
            print(f"Error: {exc}")
            return False


def delete_test_data():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from app.core.config import settings
    from app import models

    engine = create_engine(settings.DATABASE_URL)
    Session = sessionmaker(
        engine,
        autocommit=False,
        autoflush=False,
    )

    with Session() as session:
        try:
            session.query(models.User).delete()
            session.query(models.Quest).delete()
            session.query(models.Trophy).delete()
            session.query(models.Skill).delete()
            print("All tables cleared")
        except Exception as exc:
            print(f"Error: {exc}")
            return False
