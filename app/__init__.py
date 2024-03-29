from typing import Any, Dict  # noqa: F821
from typing import cast
from pathlib    import Path
from flask      import Flask
from app.routes import api
from app.db     import Base, engine
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)


app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = str(Path(__file__).resolve().parent.parent / 'templates')

app.register_blueprint(api, url_prefix='/')

def create_tables() -> None:
    Base.metadata.create_all(bind=engine)     # type: ignore

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)