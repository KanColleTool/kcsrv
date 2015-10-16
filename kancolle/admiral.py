from kancolle.orm import *
from kancolle.operation import Quest

class Admiral(AdmiralMap):
    def addQuest(self,code=None,id=None,no=None):
        pass

class AdmiralShip(AdmiralShipMap):
    pass

class AdmiralQuest(AdmiralQuestMap):
    def getAPIData(self):
        quest = Quest().byId(self.quest_id)
        return {
            "api_no": quest.no,
            "api_category": quest.category,
            "api_type": quest.frequency,
            "api_title": quest.title,
            "api_detail": quest.detail,
            "api_get_material": eval(quest.get_material),
            "api_bonus_flag": quest.bonus_flag,
            "api_invalid_flag": quest.invalid_flag,
            "api_progress_flag": self.progress,
            "api_state": self.state
        }

class AdmiralSortie(AdmiralSortieMap):
    pass