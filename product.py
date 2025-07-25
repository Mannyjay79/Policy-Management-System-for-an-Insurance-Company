class Product:
    def __init__(self, product_id, name, status='active'):
        self.product_id = product_id
        self.name = name
        self.status = status

    def create(self):
        self.status = 'active'

    def update(self, name):
        self.name = name

    def remove(self):
        self.status = 'removed'

    def suspend(self):
        self.status = 'suspended'