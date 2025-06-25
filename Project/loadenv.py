import dotenv
import os

def load_env():
    PATH_ENV = os.path.abspath(os.path.join(__file__, '..', '..', '.env'))
    PATH_MIGRATIONS = os.path.abspath(os.path.join(__file__, '..', 'migrations'))
    if os.path.exists(path= PATH_ENV):
        dotenv.load_dotenv(dotenv_path= PATH_ENV)
        
        if not os.path.exists(path= PATH_MIGRATIONS):
            os.system(command= os.environ['DB_INIT'])
        os.system(command= os.environ['DB_MIGRATE'])
        os.system(command= os.environ['DB_UPGRADE'])
