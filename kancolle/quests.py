"""
Ok, there are 2 ways to do this.
I can create a lot of functions and call them from a string or I can chain elifs.
I hate elifs chains and I don't know how expensive calls from strings are in Python, so I'll just use that.
We might have to refactor if efficiency becomes a problem.
"""
from db import AdmiralQuest,Quest,AdmiralShip
from . import *
import json

def get_quest_progress(admiral,admiral_quest=None,id_admiralquest=None,code=None):
    admiral_quest = admiral_quest if admiral_quest else AdmiralQuest.query.get(id_admiralquest)
    code = code if code else Quest.query.get(admiral_quest.quest_id).code
    
    data = json.loads(admiral_quest.data) if admiral_quest.data else None
    return globals()[code](admiral,data)

    
#If we don't have a function with the code of the Quest, we catbomb
def A0(admiral,data=None):
    """
    Never complete, idk
    """
    return 0

def A1(admiral,data=None):
    """
    2 any ships
    """
    print(AdmiralShip.query.filter_by(admiral_id=admiral.id).count())
    return QUEST_PROGRESS_COMPLETE if AdmiralShip.query.filter_by(admiral_id=admiral.id).count() > 1 else QUEST_PROGRESS_0