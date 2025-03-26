import json
import requests
import pymssql

LLM_PROMPT = "The input text lists the components of cosmetic product separated by commas. For each component match the component name in INCI (International Nomenclature of Cosmetic Ingredients) and get out semicolon-separated list in strict format: source 1 -> INCI ingredient code 1; source 2 -> INCI ingredient code 2. Each source (before '->') must be out exactly the same as in the input text. In case of ambiguity, choose the most suitable component. (Example: input: \"Декстрин, Сорбитол, Д-пантенолout\" output: \"Декстрин -> Dextrin; Сорбитол -> Sorbitol; Д-пантенолout -> Panthenol\")"
LLM_MODEL = "MaziyarPanahi/Mistral-7B-Instruct-v0.3-GGUF"
LLM_HOST = "http://localhost:1234"

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
  url = LLM_HOST + "/v1/chat/completions" # LLM Studio
  request_text = LLM_PROMPT + " Input text: " + s
  payload = {"model":LLM_MODEL,"messages":[{"role":"system","content":"You are a parser of cosmetic compositions"},{"role": "user","content":request_text}],"temperature":0}
  headers = {'Content-Type': 'application/json'}
  response = requests.post(url, data=json.dumps(payload), headers=headers)
  return json.loads(response.text)["choices"][0]["message"]["content"]

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
