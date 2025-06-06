from sqlalchemy import Column, Integer, String
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    def __repr__(self):
        return {"id" : self.id, "title":self.title}
    