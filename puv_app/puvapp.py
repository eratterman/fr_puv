from app import app, db
from app.models import Clients, WorkCenters, Materials, Orders, Vehicles


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Clients': Clients,
        'WorkCenters': WorkCenters,
        'Materials': Materials,
        'Orders': Orders,
        'Vehicles': Vehicles
    }
