import json
import sys
import os
import subprocess
import re

def get_structure_json(*args):
  app_parent_dir=os.environ['DEV0_TREES']
  app_suite_dir=None
  app_suite_name="demo"
  # get the json via wget or filename
  if len(args) >0:
    file_or_wget=args[0]
    file_path=args[1]

  else:

    if len(sys.argv) == 3:
      file_or_wget=sys.argv[1]
      file_path=sys.argv[2]

    if len(sys.argv) == 2:
      file_or_wget="file"
      file_path=sys.argv[1]

  print(file_path)  
  if file_or_wget== "wget":
    #subprocess.call(["wget", file_path])
    p = re.compile(r'[a-zA-Z0-9_]*[.]+[a-zA-Z0-9_]+')
    m = p.findall(file_path)
    print(file_path)
    file_path = m[1]
  
  if not os.path.isfile(file_path):
    print("Error: File ", file_path, " not found")
    exit()
    


#data = get_structure_json("file", "basic.json")
#print(data)