from ._anvil_designer import crimlaw_and_procedureTemplate
from anvil import *

class crimlaw_and_procedure(crimlaw_and_procedureTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
