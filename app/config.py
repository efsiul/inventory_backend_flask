import os
from pathlib    import Path
from dotenv     import load_dotenv


class Config:
    dotenv_path = os.path.join(os.path.dirname(__file__), 'dev', '.env')
    # Carga las variables de entorno desde el archivo .env
    load_dotenv(dotenv_path="dev/.env")

    # Configuración de la base de datos MySQL
    MYSQL_USER                      = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD                  = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST                      = os.getenv('MYSQL_HOST')
    MYSQL_DATABASE                  = os.getenv('MYSQL_DATABASE')

    # URL de conexión a la base de datos MySQL
    DATABASE_URI                    = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"

    # Configuración adicional de SQLAlchemy
    SQLALCHEMY_DATABASE_URI         = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

config = Config()
