import os
from datetime import datetime

#db_host = os.environ['DB_HOST']
#db_name = os.environ['DB_NAME']
#db_user = os.environ['DB_USER']
#db_pass = os.environ['DB_PASS']
#db_uri = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(64), unique=True, nullable=False)
    experience = db.Column(db.Integer, nullable=False, default=0)
    level = db.Column(db.Integer, nullable=False, default=1)
    nickname = db.Column(db.String(64), nullable=False)
    avatar_url = db.Column(db.String(256), nullable=False)
    skill_general_xp = db.Column(db.Integer, nullable=False, default=0)
    skill_dex_xp = db.Column(db.Integer, nullable=False, default=0)
    skill_nft_xp = db.Column(db.Integer, nullable=False, default=0)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    topic = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(256), nullable=False)
    experience_reward = db.Column(db.Integer, nullable=False, default=0)
    skill_reward = db.Column(db.Integer, nullable=False, default=0) 

'''
we need some data about users like logins, content interaction, etc

it is a form of:
web analytics / user tracking / event sourcing / logging

possible user's actions are:
-login
-page_view
-quest completion
-a series of logins
-a series of completed quests
'''
class ActionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    action = db.Column(db.String(64), nullable=False)
    xp_reward = db.Column(db.Integer, nullable=False, default=0)

