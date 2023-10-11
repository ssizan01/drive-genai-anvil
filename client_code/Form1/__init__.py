from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.google.auth
import anvil.google.drive

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.timer_1.interval = None
    if anvil.google.auth.get_user_access_token():
      self.user_email = anvil.google.auth.get_user_email()
      print( f'{self.user_email} is logged in')
    else:
        print('No login information found')


  def text_box_1_pressed_enter(self, **event_args):
      """This method is called when the user presses Enter in this text box"""
      
    # Get the search query from the text box
      query = self.text_box_1.text  
      
      # Call the server function to search for files
      results = anvil.server.call('search_files', query)
      
      # Clear the current items in the dropdown
      self.dropdown_files.items = []
      
      # Populate the dropdown with the file names as display values and file IDs as data values
      self.dropdown_files.items = [(file_name, file_id) for file_name, file_id in results]




  def extract_file_content_click(self, **event_args):
    print("extract_file_content_click triggered!")
  
      #self.llm_output.text = anvil.server.call('get_file_content', selected_file_id, user_query)
    self.timer_1.interval = 5
    selected_file_id = self.dropdown_files.selected_value
    print(f"Selected File ID: {selected_file_id}")

    user_query= self.user_query.text
    print(f"User Query: {user_query}")
    anvil.server.call('get_file_content', selected_file_id, user_query)

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    print(f'tick event triggered for {self.user_email} and {self.user_query.text}')
    # Fetch the relevant sentences from the backend using the server function
    sentences = anvil.server.call('fetch_sentences_from_storage', self.user_email, self.dropdown_files.selected_value, self.user_query.text)
    self.repeating_panel_1.items = sentences
    # If you want to stop the timer after fetching the data, uncomment the next line
    self.timer_1.interval = None

      

       
















