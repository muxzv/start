import lmstudio as lms

SERVER_API_HOST = ""

lms.configure_default_client(SERVER_API_HOST)

model = lms.llm("openai/gpt-oss-20b")

print(model.respond("What is the meaning of life?"))


image_path = "C:\\tmp\\76.jpg"
image_handle = lms.prepare_image(image_path)

user_text = "Текст объявления"
PROMPT = "Я пришлю тебе объявление, а ты должен классифицировать его и в ответе присылать мне подходящие хэштеги и ничего больше." \
          "Если содержит какой-либо контакт - добавь #spam. Если объявление содержит что-нибудь запрещенное законами РФ, то добавь хэштег #ban." \
          "Следующим сообщением я пришлю объявление. Дополнительных вопросов не задавай. Объявление:"
      
text = PROMPT + user_text

chat = lms.Chat()
chat.add_user_message(text, images=[image_handle])
prediction = model.respond(chat)
