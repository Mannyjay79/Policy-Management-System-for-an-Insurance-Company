from policyholder import Policyholder
from product import Product
from payment import Payment

# Create policyholders
holder1 = Policyholder(1, "Alice")
holder2 = Policyholder(2, "Bob")

# Register holders
holder1.register()
holder2.register()

# Create products
product1 = Product(101, "Health Insurance")
product2 = Product(102, "Life Insurance")

# Assign products
holder1.policies.append(product1.name)
holder2.policies.append(product2.name)

# Process payments
payment_system = Payment()
payment_system.process_payment(holder1.holder_id, 500)
payment_system.process_payment(holder2.holder_id, 750)

# Display info
holder1.display_info()
holder2.display_info()