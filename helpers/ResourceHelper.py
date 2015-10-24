from db import Resource


def update_resource(target, source=None, resources=None, **kwargs):
    """
    :return: the updated object.
    :params: either an object resource, a dict with named resources, named resources
    """
    if source is None:
        data = resources if resources else kwargs
        for key, value in data.items():
            setattr(target, key, getattr(target, key) + value)
    else:
        # Uhh...
        target.ammo = target.ammo + source.ammo if source.ammo is not None else target.ammo
        target.fuel = target.fuel + source.fuel if source.fuel is not None else target.fuel
        target.steel = target.steel + source.steel if source.steel is not None else target.steel
        target.baux = target.baux + source.baux if source.baux is not None else target.baux

        target.flame = target.flame + source.flame if source.flame is not None else target.flame
        target.bucket = target.bucket + source.bucket if source.bucket is not None else target.bucket
        target.material = target.material + source.material if source.material is not None else target.material
    return target


def get_resource_from_list(data):
    resource = Resource(fuel=data[0], ammo=data[1], steel=data[2], baux=data[3])
    return resource
