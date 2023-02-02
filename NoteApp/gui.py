import tkinter as tk
from tkinter import messagebox
from NoteApp.database import Database

db = Database()

class NoteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Notes")
        self.master.geometry("400x400")
        
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.write_notes_button = tk.Button(self.frame, text="Write Notes", command=self.write_notes)
        self.write_notes_button.pack()

        self.quit_button = tk.Button(self.frame, text="Exit", command=self.master.quit)
        self.quit_button.pack()

    def write_notes(self):
        self.write_notes_window = tk.Toplevel(self.master)
        self.write_notes_window.title("Write Notes")
        self.write_notes_frame = tk.Frame(self.write_notes_window)
        self.write_notes_frame.pack()
        tk.Label(self.write_notes_frame, text="Title:").pack()
        self.title_entry = tk.Entry(self.write_notes_frame)
        self.title_entry.pack()
        tk.Label(self.write_notes_frame, text="Contents:").pack()
        self.contents_entry = tk.Entry(self.write_notes_frame)
        self.contents_entry.pack()
        tk.Button(self.write_notes_frame, text="Submit", command=self.submit_note).pack()

    def submit_note(self):
        title = self.title_entry.get()
        contents = self.contents_entry.get()
        note_id = db.add_note(title, contents)
        self.write_notes_window.destroy()
        messagebox.showinfo("Success", "Note added with ID: {}".format(note_id))

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
