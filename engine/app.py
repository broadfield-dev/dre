from pathlib import Path
import sys
def mod_dep(file_path=".",orig_str="",mod_str=""):
  file_path =file_path
  
  try:
      file_content = index_path.read_text()
      original_block = orig_str
      replacement_block = mod_str
      if original_block in file_content:
          modified_content = file_content.replace(original_block, replacement_block)
          
          index_path.write_text(modified_content)
          print("Script modified successfully.")
      else:
          print("Warning: Error")
  
  except Exception as e:
      print(f"An error occurred while modifying the script: {e}")
      sys.exit(1)
      
