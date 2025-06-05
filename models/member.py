from sqlalchemy import Column, Integer, String, Date
from database.base import Base
import datetime

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    join_date = Column(Date, default=datetime.date.today)