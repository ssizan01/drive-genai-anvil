from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.google.auth
import anvil.google.drive
import re

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    if anvil.google.auth.get_user_access_token():
      user_info = anvil.google.auth.get_user_email()
      print( f'{user_info} is logged in')
    else:
        print('No login information found')


  # def text_box_1_pressed_enter(self, **event_args):
  #     """This method is called when the user presses Enter in this text box"""
  
  #     # Get the search query from the text box
  #     urls = self.text_box_1.text
  #     print(urls)
  #     pattern = r'https://docs\.google\.com/document/d/([a-zA-Z0-9_-]+)/edit'
  #     self.file_ids = re.findall(pattern, urls)
  #     print(f'file IDs are {self.file_ids}')

  def extract_file_content_click(self, **event_args):
      print("extract_file_content_click triggered!")
      urls = self.text_box_1.text
      print(urls)
      pattern = r'https://docs\.google\.com/document/d/([a-zA-Z0-9_-]+)/edit'
      self.file_ids = re.findall(pattern, urls)
      print(f'file IDs are {self.file_ids}')
    
      self.indexing_output.text = anvil.server.call('get_doc_embeddings', self.file_ids)


  def user_query_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""


    user_query= self.user_query.text
    print(f"User Query: {user_query}")
    print(f"max results being used is {self.max_results.text}")

    try:
      self.llm_output.text = anvil.server.call('answer_with_llm', self.file_ids, user_query,int(self.max_results.text))


    except Exception as e:  # This will catch any other exceptions
      self.llm_output.text =  f"Please index your document first"
      print(f"An error occurred: {e}")
       












