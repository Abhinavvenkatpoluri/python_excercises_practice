"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    a, b, locomotive, *rest = each_wagons_id

    return [
        locomotive,
        *missing_wagons,
        *rest,
        a,
        b
    ]


def add_missing_stops(route,**kwargs):
    new_dict = route.copy()
    new_dict["stops"]=list(kwargs.values())
    return new_dict

def extend_route_information(route, more_route_information):
    new_dict={}
    new_dict={**route,**more_route_information}
    return new_dict

def fix_wagon_depot(depot):
    return [list(row) for row in zip(*depot)]
    
    
