import os
import sys
from glob import glob
import importlib
from ..core import speak
from ..utils.tmpdir import tmp


def _get_skill_dirs():
    skill_pathnames = glob(os.path.abspath('vasisualy/skills/*/'))  # Определение всех директорий навыков
    skill_dirs = []

    for skill_dir in skill_pathnames:
        if os.path.isdir(skill_dir) and ("__init__.py" in os.listdir(skill_dir)):
            skill_dirs.append(skill_dir.rstrip('/'))  # Запись всех путей в список

    return skill_dirs


def _get_skills_names():
    # Получает названия всех директорий навыков
    skills_names = []

    for file in os.listdir(__file__.replace("skill_loader.py", "")):
        if os.path.isdir(str(os.path.abspath(__file__)).replace("skill_loader.py", '') + f"/{file}"):
            skills_names.append(file)

    return skills_names


def _relation():
    # Соотносит названия навыков и их пути в словаре
    skills = {}
    for directory in _get_skill_dirs():
        for name in _get_skills_names():
            if (name in directory) and (name != "vas_skill"):
                skills[name] = directory

    return skills


def load():
    # Импортирует все навыки как модули Python
    skills = _relation()

    for skill in skills:
        main_file_path = f"{skills[skill]}/__init__.py"
        spec = importlib.util.spec_from_file_location(skill, main_file_path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[skill] = mod
        spec.loader.exec_module(mod)


def run_skills(user_message, widget):
    # Активирует навыки
    result = ''
    for skill in _relation():
        result = sys.modules[skill].main(user_message)

        if result:
            speak.speak(result, widget)
            break

    return result


def run_looped(user_message, widget):
    with open(f"{tmp}/.skill_lock", 'r') as f:
        # Получение первой строки файла блокировки в качестве имени навыка
        skill_name = f.read()
    result = sys.modules[skill_name].loop(user_message)

    speak.speak(result, widget)
