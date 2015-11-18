from system.core.model import Model
import re

class Note(Model):
  def __init__(self):
    super(Note, self).__init__()

  def all(self):
    get = "SELECT * FROM notes"
    return self.db.query_db(get)

  def create(self, note):
    create  = "INSERT INTO notes(note) VALUES (%s)"
    data    = [note]
    return self.db.query_db(create, data)
