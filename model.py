import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy_utils import IPAddressType

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(50), unique=True, nullable=False)
    registered_on = Column(DateTime, nullable=False)

    def __init__(self, ip_address):
        self.ip = ip_address
        self.registered_on = datetime.datetime.now()
