# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

# ---------- PART 2: the OUTER while loop — one customer per repeat ----------
while billing:
    name = input("Enter customer name: ")
    item_count = int(input(f"Hello {name}! How many items are you buying? "))

# ---------- PART 3: continue on a bad item count ----------
    if item_count <= 0:
        print("Invalid item count. Please enter a positive number.\n")
        continue
# ---------- PART 4: the INNER while loop — one item per repeat ----------
customer_total = 0
item_number = 1
while item_number <= item_count:
        item_name = input("Item Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        # ---------- PART 5: item total and price band ----------
        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity. Please enter again.\n")
            continue

        item_total = price * quantity
        print(f"{item_name}: {quantity} x {price} = {item_total}")
        customer_total += item_total

        if quantity < 50:
            low_price_items += quantity
            print("Low")
        elif quantity <= 100:
            medium_price_items += quantity
            print("Medium")
        else:
            high_price_items += quantity
            print("High")

        item_number += 1


# ---------- PART 6: finish the customer, ask about the next ----------
customers_served += 1
total_sales += customer_total

print(f"\nTotal bill for {name}: {customer_total}")
print("Billing complete!\n")

again = input("Next customer? (yes/no): ")

if again != "yes":
     billing = False

# ---------- PART 7: the NESTED for report ----------
print("\n=== Grocery Category Report ===")

for slot in range(1, 4):
     if slot == 1:
          label, total = "Low price items", low_price_items
     elif slot == 2:
          label, total = "Medium price items", medium_price_items
     else:
          label, total = label, total = "High price items", high_price_items

     if total > 0:
          print(f"  {label}: {total} ", end="")

          for item in range(total):
               print("*", end="")

          print()