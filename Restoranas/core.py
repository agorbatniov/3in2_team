from collections import deque

print("Welcome to Michail's restaurant")
print('Hello from Vika')
print('Hello from Ilja')

# Banko operacij� klas�
class BankTransactions:
    def __init__(self):
        self.queue = deque()  # Naudojame kaip eil�
        self.stack = deque()  # Naudojame kaip stek�
        self.deque = deque()  # Naudojame kaip dekl�
    
    # Eil�s funkcijos
    def enqueue_transaction(self, transaction):
        # TODO: �d�ti element� � eil�
        # self.queue.
        print(f"[Elementas {transaction} �d�tas � eil�]")
    
    def dequeue_transaction(self):
        if self.queue:
            print("[Gauname element� i� eil�s]")
            # TODO: paimti pirm� element� i� eil�s
            # return self.queue
        return None
    
    # Steko funkcijos
    def push_transaction(self, transaction):
        # TODO: �d�ti element� � stek�
        # self.stack.
        print(f"[Elementas {transaction} �d�tas � stek�]")
    
    def pop_transaction(self):
        if self.stack:
            print("[Gauname element� i� steko]")
            # TODO: paimti paskutin� element� i� steko
            # return self.stack.
        return None
    
    # Deklo funkcijos
    def add_front_transaction(self, transaction):
        # TODO: �d�ti element� � priek�
        # self.deque.
        print(f"[Elementas {transaction} �d�tas � deklo gal�]")
    
    def add_rear_transaction(self, transaction):
        # TODO: �d�ti element� � priek�
        # self.deque.
        print(f"[Elementas {transaction} �d�tas � deklo priek�]")
    
    def remove_front_transaction(self):
        if self.deque:
            print("[Gauname element� i� deklo i� priekio]")
            # TODO: paimti pirm� element� i� deklo
            # return self.deque.
        return None
    
    def remove_rear_transaction(self):
        if self.deque:
            print("[Gauname element� i� deklo i� galo]")
            # TODO: paimti paskutin� element� i� deklo
            # return self.deque.
        return None

# Pavyzdys
bt = BankTransactions()

# Eil�s operacijos
bt.enqueue_transaction("Client 1")
bt.enqueue_transaction("Client 2")
print("Eil�je aptarnaujamas:", bt.dequeue_transaction())  # Client 1

# Steko operacijos
bt.push_transaction("Client 1")
bt.push_transaction("Client 2")
print("Steke aptarnaujamas:", bt.pop_transaction())  # Client 2

# Deklo operacijos
bt.add_rear_transaction("Client 1")
bt.add_front_transaction("VIP Client")
print("Dekle aptarnaujamas i� priekio:", bt.remove_front_transaction())  # VIP Client
print("Dekle aptarnaujamas i� galo:", bt.remove_rear_transaction())  # Client 1
#Atnaujintas tekstas
