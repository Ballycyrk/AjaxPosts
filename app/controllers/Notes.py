from system.core.controller import *

class Notes(Controller):
  def __init__(self, action):
    super(Notes, self).__init__(action)
    self.load_model('Note')

  def index(self):
    notes = self.models['Note'].all()
    return self.load_view('/notes/index.html', notes = notes)

  def create(self):
    new_note = request.form['note']
    self.models['Note'].create(new_note)
    notes = self.models['Note'].all()
    return self.load_view('/partials/_note.html', notes = notes)
