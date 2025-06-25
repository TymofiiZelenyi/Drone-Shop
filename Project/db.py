import flask_sqlalchemy, flask_migrate, os
from .settings import project
import sqlalchemy

project.app_context().push()

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

DATABASE = flask_sqlalchemy.SQLAlchemy(app= project)
MIGRATE = flask_migrate.Migrate(
    app= project,
    db= DATABASE,
    directory= os.path.abspath(os.path.join(__file__, '..', 'migrations'))
)