import os
from app import create_app, db, mail
from app.models import Fan, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, mail=mail, Fan=Fan, Role=Role)