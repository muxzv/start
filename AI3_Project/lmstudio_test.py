import lmstudio as lms

SERVER_API_HOST = "solnechnaya102.asuscomm.com:1234"

lms.configure_default_client(SERVER_API_HOST)

model = lms.llm("openai/gpt-oss-20b")

print(model.respond("What is the meaning of life?"))


image_path = "C:\tmp\76.jpg"
image_handle = lms.prepare_image(image_path)


chat = lms.Chat()
chat.add_user_message("Describe this image please", images=[image_handle])
prediction = model.respond(chat)
