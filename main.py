class FreshmanBot:
    def __init__(self):
        self.questions = {"расписание": "Расписание можно найти на сайте университета или в личном кабинете студента.",
                          "баллы": "Информацию о своих баллах можно узнать в личном кабинете студента.",
                          "стипендия": "Информацию о стипендии можно узнать в деканате вашего факультета.",
                          "профориентация": "Для профориентации можно обратиться в центр карьеры вашего университета.",
                          "спорт": "Ваш университет предлагает множество спортивных секций и клубов. Информацию можно найти на сайте университета."}

    def greet(self):
        return "Привет, я бот-первокурсник. Я здесь, чтобы помочь вам адаптироваться в университете. Если у вас есть какие-либо вопросы, пожалуйста, задайте их мне."

    def check_question(self, message):
        for question in self.questions:
            if question.lower() in message.lower():
                return self.questions[question]
        return None

    def respond(self, message):
        answer = self.check_question(message)
        if answer:
            return answer
        else:
            return "Извините, я не понимаю ваш вопрос. Пожалуйста, задайте другой вопрос."


bot = FreshmanBot()
print(bot.greet())
message = "расписание"
response = bot.check_question(message)
if response:
    print(response)
else:
    print("Извините, такого вопроса нет.")