from application import db




class Workout_plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    sessions = db.relationship ('Session', backref='plan')



class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    workout_plan_id = db.Column(db.Integer, db.ForeignKey('workout_plan.id'), nullable=True)

  