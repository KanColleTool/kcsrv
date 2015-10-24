"""
Oh god kill it with fire

Turn back here it uses globals accesses

If you are a young pythonista, just stop right now
"""
import json

from constants import *
from db import AdmiralQuest, Quest, Kanmusu


def get_quest_progress(admiral, admiral_quest=None, id_admiralquest=None, code=None):
    admiral_quest = admiral_quest if admiral_quest else AdmiralQuest.query.get(id_admiralquest)
    code = code if code else Quest.query.get(admiral_quest.quest_id).code

    data = json.loads(admiral_quest.data) if admiral_quest.data else None
    return globals()[code](admiral, data)


# If we don't have a function with the code of the Quest, we catbomb
def A0(admiral, data=None):
    """
    Never complete, idk
    """
    return 0


def A1(admiral, data=None):
    """
    2 any ships
    """
    print(Kanmusu.query.filter_by(admiral_id=admiral.id).count())
    return QUEST_PROGRESS_100 if Kanmusu.query.filter_by(admiral_id=admiral.id).count() > 1 else QUEST_PROGRESS_0
