from ._anvil_designer import Real_propertyTemplate
from anvil import *

class Real_property(Real_propertyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
