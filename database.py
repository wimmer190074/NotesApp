from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Notes, Tags

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///notes_tags.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_note(self, _note_title, _note_contents, _tag_name = None):
        session = self.Session()

        if _tag_name is not None:
            # Check if Tag Name already exists
            existing_tag = session.query(Tags).filter(Tags.tag_name == _tag_name).first()
            if existing_tag:
                new_note = Notes(note_title=_note_title, note_contents=_note_contents)
                new_note.tags.append(existing_tag)
                session.add(new_note)

            else:
                new_note = Notes(note_title=_note_title, note_contents=_note_contents)
                new_tag = Tags(tag_name=_tag_name)
                new_note.tags.append(new_tag)
                session.add(new_note)
        else:
            new_note = Notes(note_title=_note_title, note_contents=_note_contents)
            session.add(new_note)
        
        session.commit()
        last_id = self.get_last_created_note_id()
        session.close()
        return last_id

    def get_notes(self):
        session = self.Session()
        notes = session.query(Notes).all()
        session.close()
        return notes

    def get_note(self, _note_id):
        session = self.Session()
        note = session.query(Notes).filter_by(note_id=_note_id).first()
        session.close()
        return note

    def update_note(self, _note_id, _note_title, _note_contents, _tag_name = None):
        session = self.Session()
        note = session.query(Notes).filter_by(note_id=_note_id).first()
        note.note_title = _note_title
        note.note_contents = _note_contents
    
        
        # check if Tag name already exists
        if _tag_name is not None: 
            existing_tag = session.query(Tags).filter(Tags.tag_name == _tag_name).first()
            if existing_tag:
                note.tags = [existing_tag]
            else:
                new_tag = Tags(tag_name=_tag_name)
                note.tags = [new_tag]
                session.add(new_tag)
        else:
            pass

        session.commit()
        session.close()

    def delete_note(self, _note_id):
        session = self.Session()
        note = session.query(Notes).filter_by(note_id=_note_id).first()
        session.delete(note)
        session.commit()
        session.close()

    def get_last_created_note_id(self):
        session = self.Session()
        last_note = session.query(Notes).order_by(Notes.note_id.desc()).first()
        session.close()
        return last_note.note_id

