from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.base import Base
import datetime

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    rent_date = Column(Date, default=datetime.date.today)
    return_date = Column(Date, nullable=True)

    book = relationship("Book")
    member = relationship("Member")