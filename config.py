from dotenv import load_dotenv
load_dotenv()

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQL_ENGINE_URL = 'mysql://%s:%s@localhost/tele_test' % (os.environ['DB_USERNAME'], os.environ['DB_PASSWORD'])
SQL_ENGINE = create_engine(SQL_ENGINE_URL, echo=True)

Session = sessionmaker(bind=SQL_ENGINE)
SQL_SESSION = Session()
