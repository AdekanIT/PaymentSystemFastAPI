from database.models import UserCard, Transaction
from database import get_db
from datetime import datetime


def validate_card(card_number, db):
    card = db.query(UserCard).filter_by(card_number=card_number).first()
    return card


def create_transaction_db(card_from_number, card_to_number, amount):
    db = next(get_db())
    checker_card_from = validate_card(card_from_number, db)
    checker_card_to = validate_card(card_to_number, db)
    if checker_card_from and checker_card_to:
        if checker_card_from.balance >= amount:
            checker_card_from.balance -= amount
            checker_card_to.balance += amount
            new_transaction = Transaction(card_from_number=checker_card_from.card_number,
                                          card_to_number=checker_card_to.card_number,
                                          amount=amount,
                                          tr_date=datetime.now())
            db.add(new_transaction)
            db.commit()
            return 'Transaction successfully done!'
        else:
            return 'Not enough money!'
    else:
        return 'One of the card not exist'


def get_history_transaction_db(card_from_number):
    db = next(get_db())
    card_transaction = db.query(Transaction).filter_by(card_from_number=card_from_number).all()
    if card_transaction:
        return card_transaction
    else:
        return 'History empty'




























































