from ._anvil_designer import Practice_testsTemplate
from anvil import *

class Practice_tests(Practice_testsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
