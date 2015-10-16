from kancolle import *

def questlist(page=1):
    import math
    
    data = {}
    admiral = get_token_admiral_or_error()
    data['api_count'] = admiral.quests.count()
    data['api_page_count'] = int(math.ceil(data['api_count'] / 5))
    data["api_disp_page"] = page_number
    data["api_list"] = [quest.getAPIData() for quest in admiral.quests]