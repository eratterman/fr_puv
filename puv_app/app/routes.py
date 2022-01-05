from app import app, db
from flask import render_template, flash, redirect
import app.puv_utils as puv_utils
from app.forms import PlaceOrderForm
from app.models import Vehicles, Clients, Orders
from flask_login import current_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/place_order', methods=['GET', 'POST'])
def place_order():
    client = current_user.username
    clientid = current_user.id
    form = PlaceOrderForm()
    form.vehicle = [(v.id, v.vehicle) for v in Vehicles.query.all()]
    if form.validate_on_submit():
        o = Orders(
            clientid=clientid,
            vehicleid=form.vehicle.data
        )
        o.set_due_date()
        db.session.add(o)
        db.session.commit()
        flash('Successfully submitted order!', 'success')
        # here is where we build the BOM and submit a celery task for orders of parts
        #
        return render_template('place_order.html')

    return render_template('place_order.html')
