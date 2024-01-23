
class PizzaManager:
    def __init__(self):
        self.pizzas = []
        self.counter = []
        self.current_id = 0

    def add_pizza(self, toppings, id):
        # will add toppings to pizza and store the pizza with a unique id
        pass

    def get_all_pizzas(self):
        # returns all the pizzas
        pass

    def mark_served_pizza(self, id):
        # marks a pizza served using the id 
        pass

    def remove_served_pizzas(self):
        # removes all served pizzas
        pass

    

current_id = 0

# Function to get the next ID
def get_next_id():
    global current_id
    current_id += 1
    return current_id

# Generate IDs
id1 = get_next_id()
id2 = get_next_id()
id3 = get_next_id()

print(id1, id3)

