from db import db, AdmiralShip, AdmiralItem, Item, AdmiralShipItem


def get_itemlist_ordered(admiral):
    query = db.session.query(AdmiralItem, Item).filter(AdmiralItem.item_id == Item.id,
        AdmiralItem.admiral_id == admiral.id).order_by(Item.sortno)
    return query.all()


def get_itemlist_not_equipped(admiral):
    """
    The basic idea here is to make a single huge query to get the data we want
    Data we want = All of Admiral's equipment, except the equipped ones.

    So first we list all Admiral_Ships, then we use that to get all AdmiralShipItems
    belonging to those Ships, making sure we add AdmiralShipItem.admiral_item_id != None.
    We do this because if not, we get a query with empty result (Google empty where clause in subquery).

    Now we have the values of IDs of equipped items by all AdmiralShips. Now we simply list all AdmiralItems
    *excluding* these values. Easy.
    """
    query_admiral_ships = db.session.query(AdmiralShip.id).filter(AdmiralShip.admiral_id == admiral.id)

    query_equipped_items = db.session.query(AdmiralShipItem.admiral_item_id).filter(
        AdmiralShipItem.admiral_ship_id.in_(query_admiral_ships), AdmiralShipItem.admiral_item_id != None)

    query = db.session.query(AdmiralItem, Item).filter(AdmiralItem.item_id == Item.id,
        AdmiralItem.admiral_id == admiral.id, ~AdmiralItem.id.in_(query_equipped_items)).order_by(Item.sortno)
    return query.all()


def get_slottype_list(itemlist=None, admiral=None):
    """
    The idea here is to order items by their type.
    I'm *really* unsure how to do it though, mainly because an item can have up to 4 types,
    but it only shows up once in the list. So how do I decide which type I want to use?

    If we dump everything in a single slottype the filtering won't work, but you can equip
    and everything using the "all" list.

    Really, filtering items is the least of our problems, so I'll just TODO it.
    """
    # TODO
    itemlist = itemlist if itemlist else get_itemlist_not_equipped(admiral)
    data = {}
    data["api_slottype1"] = []
    for admiral_item, item in itemlist:
        data["api_slottype1"].append(admiral_item.id)
    return data
