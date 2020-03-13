from sqlalchemy import Integer,String

from application import db
class OpsUser(db):
    __tablename__ = 'ops_user'

    id = db.Column(Integer, primary_key=True)
    user_name = db.Column(String(32))
    user_pwd = db.Column(String(255))
