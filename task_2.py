class Data_type_not_valid(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]

class Invalid_parameter_value(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]

def total_cost_of_apartments(
    number_of_floors: int,
    cost_increasing_floor: int,
    first_appartment_cost: int
) -> int:

    if type(number_of_floors) != int:
        raise Data_type_not_valid(
            f'Incorrect number_of_floors type: {type(number_of_floors)}')
    if type(cost_increasing_floor) != int:
        raise Data_type_not_valid(
            f'Incorrect cost_increasing_floor type: {type(cost_increasing_floor)}')
    if type(first_appartment_cost) != int:
        raise Data_type_not_valid(
            f'Incorrect first_appartment_cost type: {type(first_appartment_cost)}')

    if number_of_floors == 0:
        raise Invalid_parameter_value(
            "Incorrect number_of_floors value: can't be zero value")

    COST_INCREASE = 1000
    total_sum = 0
    appartment_cost = first_appartment_cost
    price_change_indicator = cost_increasing_floor

    for i in range(1, number_of_floors + 1):
        total_sum += appartment_cost
        
        if i == price_change_indicator:
            appartment_cost += COST_INCREASE
            price_change_indicator += cost_increasing_floor

    return total_sum
