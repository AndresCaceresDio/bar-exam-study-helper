from ._anvil_designer import real_propertyTemplate
from anvil import *

class real_property(real_propertyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
