from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Session, Workout_plan
from application.forms import SessionForm, Workout_planForm


@app.route('/', methods = ['POST', 'GET'])
def index():
    all_workout_plan = Workout_plan.query.all()
    return render_template('index.html', all_workout_plan=all_workout_plan)

@app.route('/add', methods = ['GET', 'POST'])
def addPlan():
    form = Workout_planForm()
    if request.method == 'POST' or form.validate_on_submit():
        new_wo_plan = Workout_plan(name=form.name.data)
        db.session.add(new_wo_plan)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addPlan.html', form=form)


@app.route('/addSession/<int:id>', methods=['GET', 'Post'])
def addSession(id):
    form = SessionForm()
    if form.validate_on_submit():
        new_session = Session(
            pushups=form.pushups.data,
			comment=form.comment.data,
			workout_plan_id=id)
        db.session.add(new_session)
        db.session.commit()
        return redirect(url_for('Viewpage', id=id))
    return render_template('addSession.html', form=form, workout_plan_id = Workout_plan.query.get(id))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = Workout_planForm()
    name_update = Workout_plan.query.get(id)
    if form.validate_on_submit():
        name_update.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    delete_name = Workout_plan.query.get(id)
    delete_session = Session.query.filter_by(workout_plan_id=id).all()
    for delete_session in delete_session:
        db.session.delete(delete_session)
    db.session.delete(delete_name)
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/Viewpage/<int:id>', methods=['GET','POST'])
def Viewpage(id):
    view_page = Session.query.filter_by(workout_plan_id=id).all()
    return render_template('Viewpage.html', view_page=view_page)
 
