
from prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visul Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
for language in languages:
    if language.is_dynamic():
        print(language.name)

