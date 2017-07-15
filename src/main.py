import flask
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import datetime
import json


Base = declarative_base()


class Engine:
    def __init__(self):
        self.engine = sqlalchemy.create_engine("sqlite:///comment.sqlite", echo=True)
        self.Session = sqlalchemy.orm.sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add(self, obj):
        self.session.add(obj)

    def commit(self):
        self.session.commit()

class Comment(Base):
    __tablename__ = "comment"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    article_id = sqlalchemy.Column(sqlalchemy.Integer)
    text = sqlalchemy.Column(sqlalchemy.String)
    datetime = sqlalchemy.Column(sqlalchemy.DateTime)
    moderated = sqlalchemy.Column(sqlalchemy.Boolean)
    # parent_id = sqlalchemy.Column(sqlalchemy.Integer)

    def json_of_comment(self):
        d = {
            "id": self.id,
            "article_id": self.article_id,
            "text": self.text,
            "datetime": self.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "moderated": self.moderated
        }
        return d

app = flask.Flask(__name__)

e = Engine()
# t = datetime.datetime.now()
# test = Comment(article_id=0, text="hello", datetime=t, moderated=False)
# e.add(test)
# e.commit()

@app.route("/comment")
def get_all_comments():
    # print e.query(Comment).all()
    all_comments = e.session.query(Comment).all()
    return json.dumps([comment.json_of_comment() for comment in all_comments])

@app.route("/comment/<int:article_id>")
def get_comment_by_id(article_id):
    all_comments = e.session.query(Comment).filter_by(article_id=article_id).all()
    return json.dumps([comment.json_of_comment() for comment in all_comments])
