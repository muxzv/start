import json
import requests
import pymssql

PROMPT = "The input text lists the components of cosmetic product separated by commas. For each, find the most suitable match in INCI (International Nomenclature of Cosmetic Ingredients) and display semicolon-separated list like: source component 1 -> INCI ingredient code 1; source component 2 -> INCI ingredient code 2. Some composite components may contain multiple INCI-components (sample: шаромикс 705 -> Benzoic Acid, Sorbic Acid, Dehydroacetic Acid, Benzyl alcohol)"

def SplitText(s):
  s1 = s.split(',')
  return s1

def SqlServerConnect():
  return pymssql.connect(server,user,password,database='InciParserDb',as_dict=True)

def FindComponentByInci(s):
  sql = "select [IdComponent] from [tbComponent] where [Inci]='" + s + "'"
  conn = SqlServerConnect()
  cursor = conn.cursor()
  cursor.execute(sql)
  row = cursor.fetchone()
  id = row[0]
  conn.close()
  return id

def FindComponentBySyn(s):
  sql = "select [IdComponent] from [tbComponentSyn] where [Title]='" + s + "'"
  conn = SqlServerConnect()
  cursor = conn.cursor()
  cursor.execute(sql)
  row = cursor.fetchone()
  id = row[0]
  conn.close()
  return id

def AskLLM(s):
  url = "https://localhost:17555/llmstudio?prompt=" + PROMPT + "&request=" + s
  response = requests.get(url)
  s = json.loads(response)["response"]
  return s.split(" -> ")[1]

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
