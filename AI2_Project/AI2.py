def SplitText(s):
  return ["1", "2"]

def FindComponentBySyn(s):
  return 123 if s == "1" else 888 if s == "3" else None

def FindComponentByInci(s):
  pass

def AskLLM(s):
  return "3"

def MainParsingTask(st):
  ResList = []
  
  Lst = SplitText(st)
  
  for s in Lst:
    IdComponent = FindComponentBySyn(s)
    if IdComponent == None:
      inci = AskLLM(s)
      if inci != None:
        IdComponent = FindComponentByInci(inci)
        if IdComponent == None:
          IdComponent = FindComponentBySyn(inci)
    ResList.append(IdComponent)
    
  return ResList
    
print(MainParsingTask("1,2"))
