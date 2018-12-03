
from db import db
class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content
        self.done = False


    def json(self):
        return {'Content': self.content}
    #def __repr__(self):
     #   return '<Content %s>' % self.content
    
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
