from database import get_db
from database.models import User
from datetime import datetime


def add_user_db(fname, lname, tellNo, email, country, password):
    db = next(get_db())
    user = User(fname=fname, lname=lname, tellNo=tellNo, email=email, country=country,
                reg_date=datetime.now(), password=password)
    db.add(user)
    db.commit()
    return user


def get_user_info_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        return user
    else:
        return f'User by {user_id} ID not found'


def get_all_users_db():
    db = next(get_db())
    users = db.query(User).all()
    return users


def check_user_email_db(email):
    db = next(get_db())
    user = db.query(User).filter_by(email=email)
    if user:
        return user
    else:
        return f'User by {email} email not found'


def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        if edit_info == 'email':
            user.email = new_info
        elif edit_info == 'country':
            user.country = new_info
        elif edit_info == 'fname':
            user.fname = new_info
        elif edit_info == 'lname':
            user.lname = new_info
        else:
            return f'Argument {edit_info} not found'
        db.commit()
    else:
        return f'User by {user_id} email not found'


def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        return f'User by {user_id} email not found'
    else:
        db.delete(user)
        db.commit()
        return 'User deleted'






























































































