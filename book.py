class Book:
    def __init__(self, title):
        self.title = title
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes

    def remove_note(self, note_title):
        new_notes = []
        for note in self.notes:
            if note.title != note_title:
                new_notes.append(note)
        self.notes = new_notes
