import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_host = os.environ['DB_HOST']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']

engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

# create a session factory
Session = sessionmaker(bind=engine)

# create a declarative base
Base = declarative_base()

# define the user_profile table
class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# create the table
Base.metadata.create_all(engine)

# create a session
session = Session()

# add some example data
user1 = UserProfile(name='John Smith', email='john@example.com')
user2 = UserProfile(name='Jane Doe', email='jane@example.com')
session.add_all([user1, user2])
session.commit()

# close the session
session.close()

print('done______________--------!')