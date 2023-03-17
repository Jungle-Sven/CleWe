from sqlalchemy import Column, ForeignKey, Table

from app.db.base_class import Base


users_quests = Table(
    'users_quests',
    Base.metadata,
    Column('user', ForeignKey('user.id'), primary_key=True),
    Column('quest', ForeignKey('quest.id'), primary_key=True),
)
