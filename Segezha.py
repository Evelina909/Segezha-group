import random
from datetime import datetime, timedelta

class Order:
    def __init__(self, destination, weight, priority):
        self.destination = destination
        self.weight = weight
        self.priority = priority
        self.delivery_time = None

class Vehicle:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity
        self.orders = []

    def add_order(self, order):
        if self.get_total_weight() + order.weight <= self.capacity:
            self.orders.append(order)
            return True
        return False

    def get_total_weight(self):
        return sum(order.weight for order in self.orders)

def generate_batch_orders(batch_size):
    destinations = ['Москва', 'Санкт-Петербург', 'Казань', 'Новосибирск', 'Екатеринбург']
    orders = [Order(random.choice(destinations), random.randint(100, 1000), random.randint(1, 10)) for _ in range(batch_size)]
    return sorted(orders, key=lambda x: x.priority, reverse=True)

def simulate_delivery(vehicles, orders):
    waiting_list = []
    for order in orders:
        added_to_vehicle = False
        for vehicle in vehicles:
            if vehicle.add_order(order):
                added_to_vehicle = True
                break
        if not added_to_vehicle:
            waiting_list.append(order)

    while waiting_list:
        order = waiting_list.pop(0)
        for vehicle in vehicles:
            if vehicle.add_order(order):
                break
            else:
                waiting_list.append(order)
                break

    for vehicle in vehicles:
        for order in vehicle.orders:
            distance = random.randint(100, 1000)
            delivery_time = distance / vehicle.speed
            order.delivery_time = timedelta(hours=delivery_time)

vehicles = [Vehicle(60, 5000) for _ in range(400)]

def main_simulation(vehicles, num_batches):
    for _ in range(num_batches):
        batch_size = random.randint(200, 500)
        orders = generate_batch_orders(batch_size)
        simulate_delivery(vehicles, orders)

    for order in orders[:5]:
        print(
         f'Заказ до {order.destination} с весом {order.weight} кг и приоритетом {order.priority} доставлен за {order.delivery_time}')
        # print(f"Обработана пачка из {batch_size} заказов.")

num_batches = 5
main_simulation(vehicles, num_batches)
