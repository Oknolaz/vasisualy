# Vasisualy utils
import tempfile
import os
from ..skills.skill_loader import _get_skills_names

tmp = tempfile.mkdtemp(prefix="vasisualy")

skills = _get_skills_names()

for skill in skills:
    os.mkdir(f"{tmp}/{skill}")

