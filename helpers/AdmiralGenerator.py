import db


def new_admiral():
    """
    Sets up an admiral.
    This is for both APIv1 and APIv2.
    :param first_ship_id: The ID of the very first ship.
    :param admiral: The admiral object to setup.
    :return: The setup admiral.
    """
    admiral = db.Admiral()

    # Give the admiral starting resources
    admiral.resources = "500,500,500,500,1,1,3,0"
    # Give the admiral some docks.
    docks = [db.Dock() for _ in range(8)]
    admiral.docks = docks
    # Return the admiral
    admiral.setup = False
    return admiral
