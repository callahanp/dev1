def log_labeled (label, value, label_length=0, space_before=0, space_after=0, ):
  global verbose
  if label_length == 0:
    label_length=len(label)
  if verbose:
    spaces="                                       "
    for i in range(0,space_before):
      print("")
      
    if isinstance(value,str):
      print(label+":", spaces[0:label_length-len(label)], value)
    if isinstance(value,list):
      showLabel=True
      for item in value:
        if showLabel:
          print(label+":", spaces[0:label_length-len(label)], value)
          showLabel=False
        else:
          print( spaces[0:label_length -1])
          
    for i in range(0,space_after):
      print("")

def log (log_text, space_before=0, space_after=0):
  
  global verbose
  if verbose:
    for i in range(0,space_before):
      print("")
      
    print(log_text)
   
    for i in range(0,space_after):
      print("")
