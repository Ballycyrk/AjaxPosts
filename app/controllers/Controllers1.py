from system.core.controller import *

class Controllers1(Controller):
  def __init__(self, action):
    super(Controllers1, self).__init__(action)
    self.load_model('Controller1')

  def index(self):
    return self.load_view('index.html')

