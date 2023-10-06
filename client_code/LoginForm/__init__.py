from ._anvil_designer import LoginFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class LoginForm(LoginFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.source = "_/theme/SRTT%20Logo%20Merchology.png"

    # Any code you write here will run before the form opens.

  def google_sign_in_button_click(self, **event_args):
    """This method is called when the button is clicked"""

    try:
        anvil.google.auth.login()
        # Redirect to the main form after successful login
        open_form('Form1')
    except Exception as e:
        # Optionally, display an error message to the user
        Notification(f"Error: {e}", timeout=5).show()




