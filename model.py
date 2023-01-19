from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

note_tags = Table('note_tags', Base.metadata,
    Column('note_id', Integer, primary_key=True),
    Column('tag_id', Integer, primary_key=True)
)

class Note(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True)
    note_title = Column(String)
    note_contents = Column(String)
    tags = relationship("Tag", secondary=note_tags, back_populates="notes")

class Tag(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, primary_key=True)
    tag_name = Column(String)
    notes = relationship("Note", secondary=note_tags, back_populates="tags")