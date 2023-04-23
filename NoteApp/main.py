from NoteApp.database import Database

def main():
    db = Database()
    i = ""
    running = True
    while(running):
        if i == "":
            print("Welcome to Notes!")
            print("(1) View Notes")
            print("(2) Write Notes")
            print("(3) Exit")
            print("What do you want to do? ")
            i = input()
        else:
            # View Notes
            if i == "1":
                notes = db.get_notes()
                lenght = notes.__len__
                print("You have " + str(notes.__len__()) + " Notes.")
                for note in notes:
                    print("----------")
                    print("ID: ", note.note_id, "Title: ", note.note_title)
                print("----------")
                print("Do you want to view one of these Notes (enter ID) or just go back (exit)?")
                _i = input()
                i = ""

                if _i == "exit":
                    pass
                else:
                    singleNote = db.get_note(_i)
                    print("Title: ", singleNote.note_title)
                    print("Contents: ", singleNote.note_contents)
                    print("----------")
                    print("Do you want to edit (1), delete (2) or just go back (exit): ")
                    o = input()

                    #edit
                    if o == "1":
                        print("What do you want to change? Title (1), Contents (2), both (3)? or just go back (exit)?")
                        _o = input()
                        
                        if _o == "1": 
                            print("Enter new Title: ")
                            db.update_note(singleNote.note_id, input(), singleNote.note_contents)
                            singleNote = db.get_note(_i)
                            print("Title: ", singleNote.note_title)
                            print("Contents: ", singleNote.note_contents)
                            print("----------")

                        if _o == "2": 
                            print("Enter new Content: ")
                            db.update_note(singleNote.note_id, singleNote.note_title, input())
                            singleNote = db.get_note(_i)
                            print("Title: ", singleNote.note_title)
                            print("Contents: ", singleNote.note_contents)
                            print("----------")
                    
                        if _o == "3": 
                            print("Enter new Title: ")
                            new_title = input()
                            print("Enter new Content: ")
                            new_content = input()
                            db.update_note(singleNote.note_id, new_title, new_content)
                            singleNote = db.get_note(_i)
                            print("Title: ", singleNote.note_title)
                            print("Contents: ", singleNote.note_contents)
                            print("----------")

                        if _o == "exit":
                            pass

                    #delete
                    if o == "2":
                        print("Do you really want to delete this note? There is no undo! (y/n)")
                        p = input()
                        
                        if p == "y":
                            db.delete_note(_i)
                        if p == "n":
                            pass

                    #return
                    if o == "exit":
                        pass

            # Write Notes
            if i == "2":
                print("What should the title of your note be?")
                title = input()
                print("What should the contents of the note be?")
                contents = input()
                id = db.add_note(title, contents)
                
                notes = db.get_notes()
                singleNote = db.get_note(id)
                print("Title: ", singleNote.note_title)
                print("Contents: ", singleNote.note_contents)
                print("----------")
                
                print("Do you want to view all of your notes (1) or just exit (exit)?")
                i = input()

                if i == "exit":
                    i = ""
                    break

            if i == "3":
                running = False

if __name__ == "__main__":
    main()  