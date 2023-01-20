from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Notes, Tags

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///notes_tags.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_note(self, note_title, note_contents, tag_name):
        session = self.Session()

        new_note = Notes(note_title=note_title, note_contents=note_contents)
        new_tag = Tags(tag_name=tag_name)
        new_note.tags.append(new_tag)

        session.add(new_note)
        session.commit()
        session.close()

db = Database()
db.add_note('My Note','This is my note','Important')