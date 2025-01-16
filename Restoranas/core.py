from collections import deque

print("Welcome to Michail's restaurant")
print('Hello from Vika')
print('Hello from Ilja')

# Banko operacijø klasë
class BankTransactions:
    def __init__(self):
        self.queue = deque()  # Naudojame kaip eilæ
        self.stack = deque()  # Naudojame kaip stekà
        self.deque = deque()  # Naudojame kaip deklà
    
    # Eilës funkcijos
    def enqueue_transaction(self, transaction):
        # TODO: ádëti elementà á eilæ
        # self.queue.
        print(f"[Elementas {transaction} ádëtas á eilæ]")
    
    def dequeue_transaction(self):
        if self.queue:
            print("[Gauname elementà ið eilës]")
            # TODO: paimti pirmà elementà ið eilës
            # return self.queue
        return None
    
    # Steko funkcijos
    def push_transaction(self, transaction):
        # TODO: ádëti elementà á stekà
        # self.stack.
        print(f"[Elementas {transaction} ádëtas á stekà]")
    
    def pop_transaction(self):
        if self.stack:
            print("[Gauname elementà ið steko]")
            # TODO: paimti paskutiná elementà ið steko
            # return self.stack.
        return None
    
    # Deklo funkcijos
    def add_front_transaction(self, transaction):
        # TODO: ádëti elementà á prieká
        # self.deque.
        print(f"[Elementas {transaction} ádëtas á deklo galà]")
    
    def add_rear_transaction(self, transaction):
        # TODO: ádëti elementà á prieká
        # self.deque.
        print(f"[Elementas {transaction} ádëtas á deklo prieká]")
    
    def remove_front_transaction(self):
        if self.deque:
            print("[Gauname elementà ið deklo ið priekio]")
            # TODO: paimti pirmà elementà ið deklo
            # return self.deque.
        return None
    
    def remove_rear_transaction(self):
        if self.deque:
            print("[Gauname elementà ið deklo ið galo]")
            # TODO: paimti paskutiná elementà ið deklo
            # return self.deque.
        return None

# Pavyzdys
bt = BankTransactions()

# Eilës operacijos
bt.enqueue_transaction("Client 1")
bt.enqueue_transaction("Client 2")
print("Eilëje aptarnaujamas:", bt.dequeue_transaction())  # Client 1

# Steko operacijos
bt.push_transaction("Client 1")
bt.push_transaction("Client 2")
print("Steke aptarnaujamas:", bt.pop_transaction())  # Client 2

# Deklo operacijos
bt.add_rear_transaction("Client 1")
bt.add_front_transaction("VIP Client")
print("Dekle aptarnaujamas ið priekio:", bt.remove_front_transaction())  # VIP Client
print("Dekle aptarnaujamas ið galo:", bt.remove_rear_transaction())  # Client 1
#Atnaujintas tekstas
