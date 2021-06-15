from vasisualy.skills.vas_skill.vas_skill import Skill  # Импорт родительского класса навыков


class HelloWorld(Skill):
    def main(self, user_message):
        if super(HelloWorld, self)._is_triggered(user_message, super(HelloWorld, self)._get_triggers()):
            toSpeak = "Hello, World!"
            return toSpeak
        else:
            return ''

def main(user_message):
    skill = HelloWorld("hello_world", user_message)  # Вывод сообщения, переданного навыком, пользователю.
    return skill.main(user_message)
