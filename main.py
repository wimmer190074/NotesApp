import sqlalchemy

from model import Base, Note

def main():
    """Run Main function."""
    db_connection = sqlalchemy.create_engine("sqlite:///.db")
    Base.metadata.create_all(db_connection)
    session_factory = sqlalchemy.orm.sessionmaker()
    session_factory.configure(bind=db_connection)

    with session_factory() as session:
        new_note = Note(note_title="Test")
        session.add(new_note)
        session.commit()


if __name__ == "__main__":
    main()