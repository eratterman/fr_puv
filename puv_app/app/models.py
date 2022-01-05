from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from app import db


class Clients(db.Model):
    """
    this model holds the clients we do business with
    for time sake, I'm assuming only one client and already logged in
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    company = db.Column(db.String(64), index=True)
    client_email = db.Column(db.String(120), index=True, unique=True)
    contact_name = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Client {self.username}>'


class WorkCenters(db.Model):
    """
    this model holds the various work centers available
    """
    id = db.Column(db.Integer, primary_key=True)
    work_center = db.Column(db.String(64), index=True)


class Materials(db.Model):
    """
    this model holds the various materials,
    the cost, and turn around time in days
    """
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(120), index=True)
    description = db.Column(db.String(600))
    price = db.Column(db.Float)
    turn_around_days = db.Column(db.Integer)


class Orders(db.Model):
    """
    assuming total assembly time is 10 days
    set_due_date() will add 10 days
    """
    order_number = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    clientid = db.Column(db.Integer, db.ForeignKey('clients.id'))
    vehicleid = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    def set_due_date(self):
        self.due_date = self.order_date + timedelta(days=10)


class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle = db.Column(db.String(64), index=True)
