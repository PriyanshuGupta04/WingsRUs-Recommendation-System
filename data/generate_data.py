import pandas as pd
import random
from datetime import datetime, timedelta

# Menu items
wings_flavors = ["Classic Wings", "BBQ Wings", "Spicy Wings", "Honey Mustard Wings", "Garlic Parmesan Wings"]
sides = ["Fries", "Onion Rings", "Celery Sticks", "Garlic Bread"]
drinks = ["Cola", "Beer", "Iced Tea", "Lemonade"]
dips = ["Ranch Dip", "Cheese Dip", "Blue Cheese Dip"]

def generate_order(num_orders=1000):
    orders = []
    for order_id in range(1, num_orders + 1):
        customer_id = random.randint(100, 999)
        
        # Random items (1-3 wings + 1-2 sides/drinks/dips)
        items = random.sample(wings_flavors, k=random.randint(1, 3))
        items += random.sample(sides + drinks + dips, k=random.randint(1, 2))
        
        # Random timestamp in the past year
        timestamp = datetime.now() - timedelta(days=random.randint(1, 365))
        
        orders.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "items": ", ".join(items),
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M")
        })
    return pd.DataFrame(orders)

# Generate and save
df = generate_order(1000)
df.to_csv("data/raw_data.csv", index=False)
print("Generated 1000 synthetic orders in data/raw_data.csv")