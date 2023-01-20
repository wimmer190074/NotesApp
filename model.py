from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Notes(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True)
    note_title = Column(String)
    note_contents = Column(String)
    tags = relationship("Tags", secondary="notes_tags", back_populates="notes")

class Tags(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, primary_key=True)
    tag_name = Column(String)
    notes = relationship("Notes", secondary="notes_tags", back_populates="tags")

class NotesTags(Base):
    __tablename__ = 'notes_tags'
    note_id = Column(Integer, ForeignKey('notes.note_id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.tag_id'), primary_key=True)