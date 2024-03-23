from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    tellNo = Column(Integer, unique=True)
    email = Column(String, unique=True)
    country = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)


class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    card_number = Column(Integer, nullable=False, unique=True)
    card_name = Column(String, ForeignKey('user.fname'))
    balance = Column(Float, default=0)
    exp_date = Column(Integer)
    cvv = Column(Integer)

    user_fk = relationship(User, lazy='subquery')


class Transaction(Base):
    __tablename__ = 'transaction'
    tr_id = Column(Integer, autoincrement=True, primary_key=True)
    card_from_number = Column(Integer, ForeignKey('cards.card_number'))
    card_to_number = Column(Integer, ForeignKey('cards.card_number'))
    amount = Column(Float)
    status = Column(Boolean, default=True)
    tr_date = Column(DateTime)

    card_from_fk = relationship(UserCard, lazy='subquery')
    card_to_fk = relationship(UserCard, lazy='subquery')