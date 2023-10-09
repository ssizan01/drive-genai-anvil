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

    if anvil.google.auth.get_user_access_token():
      user_info = anvil.google.auth.get_user_email()
      print( f'{user_info} is logged in')
    else:
        print('No login information found')

    # Any code you write here will run before the form opens.
    

  # def button_1_click(self, **event_args):

  #   # This method is called when the button is clicked
  #   try:
        
  #       # Hide the login button after successful login
  #       self.button_1.visible = False
  #       # Optionally, you can notify the user that they've logged in successfully
  #       # self.label_status.text = "Logged in successfully!"
  #   except Exception as e:
  #       print(f"Error: {e}")

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
  
      selected_file_id = self.dropdown_files.selected_value
      print(f"Selected File ID: {selected_file_id}")
  
      user_query= self.user_query.text
      print(f"User Query: {user_query}")
  
      #anvil.server.call('get_file_content', selected_file_id, user_query)
      anvil.server.call('test_function')
      #print(f"File Content Received: {self.llm_output.text}")
  
      # Set the content of the file to the text box
       

  def user_query_pressed_enter(self, **event_args):
      selected_file_id = self.dropdown_files.selected_value
      user_query= self.user_query.text
      
  
      #file_content = anvil.server.call('get_file_content', selected_file_id, user_query)
      
      #self.llm_output.text = file_content
    

      anvil.server.call('get_file_content', selected_file_id, user_query)
      #self.repeating_panel_1.items = sentences








