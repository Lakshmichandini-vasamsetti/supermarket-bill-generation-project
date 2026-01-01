# On# ==============================
# SUPER MARKET BILLING PROJECT
# ==============================

# Store items
store = {
    "rice": 60,
    "sugar": 45,
    "oil": 120
}

# GST rates
gst_rates = {
    "rice": 5,
    "sugar": 5,
    "oil": 12
}

cart = []


# ---------- BILL PRINT FUNCTION ----------
def print_bill():
    if not cart:
        print("\n❌ No items purchased. Bill not generated.")
        return

    print("\n----------------------------------------")
    print("           SUPER MARKET BILL")
    print("----------------------------------------")
    print(f"{'Item':15}{'Qty':5}{'Rate':8}{'Amount':10}")
    print("----------------------------------------")

    subtotal = 0
    total_gst = 0

    for item in cart:
        amount = item["qty"] * item["price"]
        gst_amount = amount * item["gst"] / 100

        subtotal += amount
        total_gst += gst_amount

        print(f"{item['name']:15}{item['qty']:<5}{item['price']:<8}{amount:<10.2f}")
        print(f"  SGST ({item['gst']/2}%)           {gst_amount/2:.2f}")
        print(f"  CGST ({item['gst']/2}%)           {gst_amount/2:.2f}")
        print("----------------------------------------")

    grand_total = subtotal + total_gst

    print(f"{'Subtotal:':25}{subtotal:.2f}")
    print(f"{'Total GST:':25}{total_gst:.2f}")
    print("----------------------------------------")
    print(f"{'Grand Total:':25}{grand_total:.2f}")
    print("----------------------------------------")
    print("        THANK YOU FOR VISIT 😊")
    print("----------------------------------------")


# ---------- MAIN MENU ----------
while True:
    print("\n========== MENU ==========")
    print("1. Purchase Items")
    print("2. Add New Item to Store")
    print("3. Exit & Print Bill")

    option = input("Enter your choice (1/2/3): ")

    # Purchase items
    if option == "1":
        while True:
            item = input("Enter item name (or 'done'): ").lower()
            if item == "done":
                break

            if item not in store:
                print("❌ Item not available")
                continue

            qty = int(input("Enter quantity: "))

            cart.append({
                "name": item.capitalize(),
                "qty": qty,
                "price": store[item],
                "gst": gst_rates[item]
            })

    # Add new item
    elif option == "2":
        name = input("Enter new item name: ").lower()
        price = float(input("Enter price: "))
        gst = float(input("Enter GST %: "))

        store[name] = price
        gst_rates[name] = gst

        print("✅ Item added successfully!")

    # Exit and print bill
    elif option == "3":
        print_bill()
        break

    else:
        print("❌ Invalid choice! Please enter 1, 2 or 3")
