from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://winn:123456@127.0.0.1:3306/weibo?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True                                                                            

db = SQLAlchemy(app)

class WeiboMysql(db.Model):
    __tablename__ = 'kunming'
    messageid = db.Column(db.String(16), primary_key=True)
    username = db.Column(db.String(30), unique=False)
    content = db.Column(db.String(500))
    geoinfo = db.Column(db.String(50))
    tweetnum = db.Column(db.Integer)
    time = db.Column(db.String(20), unique=False)
    def __init__(self, messageid, username):
        self.messageid = messageid
        self.username = username
    
    def __repr__(self):
        return '<User %r>' % self.username

if __name__=='__main__':
    #db.create_all()
    #user_test = User(id='123', username='john')
    #user_test2 = User(id='1234', username='johnd')
    #db.session.add(user_test)
    #db.session.add(user_test2)
    #db.session.commit()
    print(WeiboMysql.query.filter_by(messageid='3608720938280712').count())

