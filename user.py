from sqlalchemy import create_engine, Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Joke(DeclarativeBase):
    __tablename__ = 'variation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    variation_text = Column('variation_text', String)

    def as_dict(self):
        return {c.name:getattr(self,c.name) for c in self.__table__.columns}

    # def __repr__(self):
    #     return "".format(self.code)

