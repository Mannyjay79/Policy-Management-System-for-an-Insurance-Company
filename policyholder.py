class Policyholder:
    def __init__(self, holder_id, name, is_active=True):
        self.holder_id = holder_id
        self.name = name
        self.is_active = is_active
        self.policies = []

    def register(self):
        self.is_active = True
        print(f"{self.name} has been registered.")

    def suspend(self):
        self.is_active = False
        print(f"{self.name} has been suspended.")

    def reactivate(self):
        self.is_active = True
        print(f"{self.name} has been reactivated.")

    def display_info(self):
        print(f"ID: {self.holder_id}, Name: {self.name}, Active: {self.is_active}")
        for policy in self.policies:
            print(f"Policy: {policy}")