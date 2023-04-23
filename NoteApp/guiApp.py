import tkinter as tk
from tkinter import ttk
from NoteApp.database import Database
from tkinter import messagebox

db = Database()

class NoteApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Note App")
        self.geometry("400x500")
        
        self.db = Database()

        self.note_list = tk.Listbox(self)
        self.note_list.pack(fill="both", expand=True)
        
        self.note_list.bind("<<ListboxSelect>>", self.load_note)


        self.note_title = tk.StringVar()
        self.note_content = tk.StringVar()

        self.note_title_label = tk.Label(self)
        self.note_title_label.pack(fill="both", expand=True)
        
        self.note_contents_label = tk.Label(self)
        self.note_contents_label.pack(fill="both", expand=True)

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.delete_notes_button = tk.Button(self.frame, text="Delete Note", command=self.delete_note)
        self.delete_notes_button.pack()

        self.edit_notes_button = tk.Button(self.frame, text="Edit Note", command=self.edit_note)
        self.edit_notes_button.pack()

        self.write_notes_button = tk.Button(self.frame, text="Write Notes", command=self.write_notes)
        self.write_notes_button.pack()

        self.quit_button = tk.Button(self.frame, text="Exit", command=self.quit)
        self.quit_button.pack()

        
        self.populate_list()

    def load_note(self, event=None):
        selected_index = self.note_list.curselection()
        if selected_index:
            note_id = self.note_list.get(selected_index[0])
            note = self.db.get_note(note_id)
            self.display_note(note)

    def populate_list(self):
        self.note_list.delete(0, tk.END)
        for note in self.db.get_notes():
            self.note_list.insert(tk.END, note.note_id)

        # select first item
        if self.note_list.size() > 0:
            self.note_list.selection_clear(0, tk.END)
            self.note_list.selection_set(0)
            self.load_note()


    def display_note(self, note):
        self.note_title_label.config(text=note.note_title)
        self.note_contents_label.config(text=note.note_contents)

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
        self.populate_list()

    def delete_note(self):
        selected_index = self.note_list.curselection()
        if selected_index:
            note_id = self.note_list.get(selected_index[0])
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete the selected note?")
            if confirm:
                self.db.delete_note(note_id)
            self.populate_list()

    def edit_note(self):
        selected_index = self.note_list.curselection()
        if selected_index:
            note_id = self.note_list.get(selected_index[0])
            note = self.db.get_note(note_id)
            self.edit_notes_window = tk.Toplevel(self.master)
            self.edit_notes_window.title("Edit Notes")
            self.edit_notes_frame = tk.Frame(self.edit_notes_window)
            self.edit_notes_frame.pack()
            tk.Label(self.edit_notes_frame, text="Title:").pack()
            self.edit_title_entry = tk.Entry(self.edit_notes_frame)
            self.edit_title_entry.insert(0, note.note_title)
            self.edit_title_entry.pack()
            tk.Label(self.edit_notes_frame, text="Contents:").pack()
            self.edit_contents_entry = tk.Entry(self.edit_notes_frame)
            self.edit_contents_entry.insert(0, note.note_contents)
            self.edit_contents_entry.pack()
            tk.Button(self.edit_notes_frame, text="Submit", command=lambda: self.submit_edit_note(note_id)).pack()

    def submit_edit_note(self, note_id):
        title = self.edit_title_entry.get()
        contents = self.edit_contents_entry.get()
        self.db.update_note(note_id, title, contents)
        self.edit_notes_window.destroy()
        messagebox.showinfo("Success", "Note updated")
        self.populate_list()



if __name__ == "__main__":
    app = NoteApp()
    app.mainloop()
