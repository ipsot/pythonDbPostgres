import json

import user
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from user import Joke
from user import DeclarativeBase

engine = create_engine('postgresql+psycopg2://sellingnftuser:1234@151.248.113.116/nftrecordsdb')

DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# newJoke=Joke(variation_text="Не шутка")
# session.add(newJoke)
# session.commit()

for currentJoke in session.query(Joke):
    print(json.dumps(currentJoke.__dict__))


# DATABASE = {'drivername': 'postgres', 'host': '151.248.113.116', 'port': '5432', 'username': 'sellingnftuser',
#             'password': '1234', 'database': 'nftrecordsdb'}
#
# engine = create_engine(URL(**DATABASE))
#
# connection = psycopg2.connect(database="nftrecordsdb", user="sellingnftuser", password="1234", host="151.248.113.116",
#                               port=5432)
#
# with connection:
#     with connection.cursor() as cur:
#         try:
#             cur.execute("Delete from jokes")
#         except:
#             connection.rollback()
#
# cursor = connection.cursor()
#
# # cursor.execute("INSERT INTO jokes (textJoke) values (%s)", ("What"))
# # connection.commit()
#
# cursor.execute("Select * from jokes")
#
# for currentJokes in cursor:
#     print(currentJokes[0], ':', currentJokes[1])
#
# cursor.close()
