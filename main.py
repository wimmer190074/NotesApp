import sqlalchemy

from model import Base, Note, Tag

def main():
    """Run Main function."""
    db_connection = sqlalchemy.create_engine("sqlite:///database.db")
    Base.metadata.create_all(db_connection)
    session_factory = sqlalchemy.orm.sessionmaker()
    session_factory.configure(bind=db_connection)

    with session_factory() as session:
        new_note = Note(note_title="Test", note_contents="TestTest", tag_id=0)
        session.add(new_note)
        session.commit()

if __name__ == "__main__":
    main()