from system.core.model import Model
import re

class User(Model):
  def __init__(self):
    super(User, self).__init__()

  def validate(self):
    EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
    NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
    PASSWORD_REGEX = re.compile(r'^.*\d+.*[A-Z]+.*$')
    BIRTHDAY_REGEX = re.compile(r'^\d{2}[\-]\d{2}[\-]\d{4}$')



