from NoteApp import Database

def test_add_note():
    db = Database()
    db.__init__()
    id = db.add_note("Test Title", "Test Contents")
    note = db.get_note(id)
    assert note.note_title == "Test Title"
    assert note.note_contents == "Test Contents"
    db.delete_note(id)

def test_get_note():
    db = Database()
    db.__init__()
    id = db.add_note("Test Title", "Test Contents")
    note = db.get_note(id)
    assert note.note_title == "Test Title"
    assert note.note_contents == "Test Contents"
    db.delete_note(id)

def test_get_notes():
    db = Database()
    db.__init__()
    id1 = db.add_note("Test Title 1", "Test Contents 1")
    id2 = db.add_note("Test Title 2", "Test Contents 2")
    notes = db.get_notes()
    assert len(notes) == 2
    db.delete_note(id1)
    db.delete_note(id2)

def test_update_note():
    db = Database()
    db.__init__()
    id = db.add_note("Test Title", "Test Contents")
    db.update_note(id, "Updated Title", "Updated Contents")
    note = db.get_note(id)
    assert note.note_title == "Updated Title"
    assert note.note_contents == "Updated Contents"
    db.delete_note(id)

def test_delete_note():
    db = Database()
    db.__init__()
    id = db.add_note("Test Title", "Test Contents")
    db.delete_note(id)
    notes = db.get_notes()
    assert len(notes) == 0