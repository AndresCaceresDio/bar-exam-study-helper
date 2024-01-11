from ._anvil_designer import evidenceTemplate
from anvil import *

class evidence(evidenceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
