from app import db

class Thing(db.Model):
	id = db.Column(db.Integer(), primary_key=True)

	def __repr__(self):
		return "<Thing {}>".format(self.id)

db.create_all()