# Work Log
## 2023-01-19

- Started this Work-Log
- Finished ER-Diagramm ([ER-Diagramm](ER-Diagramm_NotesApp.png))
- started coding the datamodel, still struggling with the many to many connection

## 2023-01-20

- Had a weird error message when I tried to create my session
- After a lot of browsing the internet for solutions to my problems, I redid the whole thing with an actual crosstable and it finally worked.

## 2023-01-26

- Finished the CRUD Module of the Database class (get_notes, get_note, update_note and delete_note). 
- Tag names were added as doubles, when the name already existed while adding new notes.
- I fixed the problem with the doubled tags.
- Same problem occured in the update database. Fixed that too.
- Started writing the main Console Application (as a minimum viable product). Finished View, Edit and Deleting of Notes.

## 2023-01-27
- Coded the Write Note, added loops and breakpoints
- Added new function in the database.py that returns the id of the last created note and modified the add_note function so that it returns the note_id of the newly created note.
- Version 1.0.0 finished
- Added Venv, Module and setup config and fixed a small bug in main.py that lead to the exit clause not working.
- Added Testing Setup
- Started Writing Tests (Last three are missing)