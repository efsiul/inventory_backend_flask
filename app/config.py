import os
from pathlib    import Path
from dotenv     import load_dotenv


class Config:
    # dotenv_path = os.path.join(os.path.dirname(__file__), 'dev', '.env')

    load_dotenv()

    MYSQL_USER                      = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD                  = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST                      = os.getenv('MYSQL_HOST')
    MYSQL_DATABASE                  = os.getenv('MYSQL_DATABASE')

    DATABASE_URI                    = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"

    SQLALCHEMY_DATABASE_URI         = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

config = Config()
