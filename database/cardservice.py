from database.models import UserCard
from database import get_db
from datetime import datetime


def add_card_db(user_id, card_name, card_number, exp_date, cvv):
    db = next(get_db())
    card = UserCard(user_id=user_id, card_name=card_name, card_number=card_number, cvv=cvv,
                    exp_date=exp_date)
    if card:
        db.add(card)
        db.commit()
        return 'Card created'
    else:
        return 'WTF?!'


def add_balance_card_db(card_id, balance):
    db = next(get_db())
    card = db.query(UserCard).filter_by(card_id=card_id).first()
    if card:
        card.balance += balance
        db.commit()
    else:
        return f'Card by {card_id} ID not found'


def get_user_card_db(user_id):
    db = next(get_db())
    user_card = db.query(UserCard).filter_by(user_id=user_id).first()
    if user_card:
        return user_card
    else:
        return f'User cards by {user_id} not found'


def get_exact_user_card_db(user_id, card_id):
    db = next(get_db())
    exact = db.query(UserCard).filter_by(user_id=user_id, card_id=card_id)
    if exact:
        return exact
    else:
        return 'Card not found!'


def check_card_db(card_number):
    db = next(get_db())
    checker = db.query(UserCard).filter_by(card_number=card_number).first()
    if checker:
        return checker
    else:
        return 'Card not found'


def delete_card_db(card_id):
    db = next(get_db())
    card = db.query(UserCard).filter_by(card_id=card_id).first()
    if card:
        db.delete(card)
        db.commit()
        return 'Card deleted!'
    else:
        return f'Card by {card_id} ID not found'


def edit_card_db(card_id, edit_info, new_info):
    db = next(get_db())
    card = db.query(UserCard).filter_by(card_id=card_id).first()
    if card:
        if edit_info == 'curd_name':
            card.card_name = new_info
        else:
            return 'Wrong argument'
        db.commit()
    else:
        return f'Card by {card_id} ID not found'



















































































