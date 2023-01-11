from collections import Counter


class TrackOrders:
    def __init__(self):
        self.__orders = []

    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, customer, order, day):
        new_order = {"customer": customer, "order": order, "day": day}
        self.__orders.append(new_order)

    def get_most_ordered_dish_per_customer(self, customer):
        return Counter(
            [
                order.get("order")
                for order in self.__orders
                if order.get("customer") == customer
            ]
        ).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        client_orders = [
            order
            for order in self.__orders
            if order.get("customer") == customer
        ]

        all_dishes = {order.get("order") for order in self.__orders}
        client_dishes = {order.get("order") for order in client_orders}

        return all_dishes - client_dishes

    def get_days_never_visited_per_customer(self, customer):
        client_orders = [
            order
            for order in self.__orders
            if order.get("customer") == customer
        ]

        all_days = {order.get("day") for order in self.__orders}
        client_days = {order.get("day") for order in client_orders}

        return all_days - client_days

    def get_busiest_day(self):
        return Counter(
            [
                order.get("day")
                for order in self.__orders
            ]
        ).most_common(1)[0][0]

    def get_least_busy_day(self):
        return Counter(
            [
                order.get("day")
                for order in self.__orders
            ]
        ).most_common()[-1][0]
