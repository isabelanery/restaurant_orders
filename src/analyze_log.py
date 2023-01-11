import csv
from collections import Counter


def convert_log_to_dict(path_to_file, field_names):
    if path_to_file[-4:] != ".csv":
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as file:
            reader = csv.DictReader(file, fieldnames=field_names)
            return list(reader)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'") from e


def filter_orders_by_customer(orders_log: list, customer: str):
    return [order for order in orders_log if order.get("customer") == customer]


def get_most_requested_dish(orders_log: list):
    counter = Counter([order.get("dish") for order in orders_log])
    return counter.most_common(1)[0][0]


def count_dish_requests(orders_log: list, dish: str):
    return len([order for order in orders_log if order.get("dish") == dish])


def count_client_never_requested_dishes(orders_log: list, customer: str):
    client_orders = filter_orders_by_customer(orders_log, customer)
    client_dishes = {order.get("dish") for order in client_orders}
    all_dishes = {order.get("dish") for order in orders_log}

    return all_dishes - client_dishes


def get_client_never_attended_days(orders_log: list, customer: str):
    client_orders = filter_orders_by_customer(orders_log, customer)
    client_days = {order.get("day") for order in client_orders}
    all_days = {order.get("day") for order in orders_log}

    return all_days - client_days


def analyze_log(path_to_file):
    orders_log = convert_log_to_dict(path_to_file, ["customer", "dish", "day"])

    maria_orders = filter_orders_by_customer(orders_log, "maria")
    maria_favorites = get_most_requested_dish(maria_orders)

    arnaldo_orders = filter_orders_by_customer(orders_log, "arnaldo")
    arnaldo_asked_hb = count_dish_requests(arnaldo_orders, "hamburguer")

    joao_never_asked = count_client_never_requested_dishes(orders_log, "joao")
    joao_never_attended = get_client_never_attended_days(orders_log, "joao")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{maria_favorites}\n"
            f"{arnaldo_asked_hb}\n"
            f"{joao_never_asked}\n"
            f"{joao_never_attended}\n"
        )