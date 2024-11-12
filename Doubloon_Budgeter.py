import tkinter as tk
from tkinter import messagebox

# shop items with their corresponding prices in doubloons 
shop_items = [
    {"name": "Pile of Stickers", "price": 17},
    {"name": "DigitalOcean Credits", "price": 28},
    {"name": "OpenAI Credits", "price": 28},
    {"name": "Hetzner Credits", "price": 28},
    {"name": "Anthropic Credits", "price": 28},
    {"name": "Hack Club MicroSD card", "price": 32},
    {"name": "Logic Analyzer", "price": 34},
    {"name": "Bite Size Linux", "price": 40},
    {"name": "Bite Size Bash", "price": 40},
    {"name": "How DNS Works", "price": 40},
    {"name": "Domain (1 year)", "price": 40},
    {"name": "Signed photo of Malted", "price": 42},
    {"name": "Raspberry Pi Kit", "price": 48},
    {"name": "Digital Calipers", "price": 50},
    {"name": "PCB manufacturing credit", "price": 55},
    {"name": "Adafruit ItsyBitsy M4 Express", "price": 55},
    {"name": "Hot Glue Gun", "price": 57},
    {"name": "DigiKey/LCSC Credit", "price": 63},
    {"name": "GitHub Invertocat Pin", "price": 76},
    {"name": "Signed photo of Graham Darcey", "price": 80},
    {"name": "Pinecil", "price": 82},
    {"name": "GitHub Notebook", "price": 140},
    {"name": "Blahåj", "price": 123},
    {"name": "Baofeng UV-5R", "price": 126},
    {"name": "Lockpick set", "price": 154},
    {"name": "GitHub Keycaps", "price": 154},
    {"name": "Hack Club socks", "price": 156},
    {"name": "GitHub Universe Badge", "price": 172},
    {"name": "1 lb fudge", "price": 240},
    {"name": "YubiKey", "price": 264},
    {"name": "Dremel 4300 kit", "price": 265},
    {"name": "Raspberry Pi 5", "price": 275},
    {"name": "System76 Launch Keyboard", "price": 520},
    {"name": "GitHub MiiR® Backpack", "price": 725},
    {"name": "Flipper Zero", "price": 850},
    {"name": "Bambu Lab A1 Mini", "price": 1000},
    {"name": "Thermal Imaging Camera", "price": 1015},
    {"name": "Hot-air rework station", "price": 1120},
    {"name": "100MHz Oscilloscope", "price": 1210},
    {"name": "iPad (10th gen)", "price": 2090},
    {"name": "Framework Laptop 13\"", "price": 3075},
    {"name": "MacBook Air M2", "price": 4000},
    {"name": "Framework Laptop 16\"", "price": 4980},
    {"name": "DEF CON ticket", "price": 6675}
]

budget = 0 
remaining_budget = 0
cart = []

# sets the budget
def set_budget(): 
    global budget, remaining_budget
    try: 
        budget = int(budget_entry.get())
        remaining_budget = budget
        budget_label.config(text=f"Your Budget: {budget} doubloons")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for your budget")

def add_to_cart(item): 
    global remaining_budget
    if remaining_budget >= item['price']:
        cart.append(item)
        remaining_budget -= item['price']
        remaining_label.config(text=f"Remaining Budget: {remaining_budget} Doubloons")
        messagebox.showinfo("Added to Cart", f"Added {item['name']} to cart.")
    else:
        messagebox.showwarning("Not enough Doubloons", "You don't have enough doubloons for that item!")

def show_cart():
    if cart: 
        cart_items = "\n".join([f"- {item['name']} ({item['price']} doubloons)" for item in cart])
        total_spent = sum([item['price'] for item in cart])
        messagebox.showinfo("Your Cart", f"Items in your cart:\n{cart_items}\n\nTotal Spent: {total_spent} doubloons")
    else:
        messagebox.showinfo("Your Cart", "Your cart is empty.")

# Setting up the main window
root = tk.Tk()
root.title("Shop Budgeter")

# Budget input
budget_frame = tk.Frame(root)
budget_frame.pack(pady=10)

tk.Label(budget_frame, text="Enter your total budget in doubloons:").pack(side=tk.LEFT)
budget_entry = tk.Entry(budget_frame)
budget_entry.pack(side=tk.LEFT)
set_budget_btn = tk.Button(budget_frame, text="Set Budget", command=set_budget)
set_budget_btn.pack(side=tk.LEFT)

budget_label = tk.Label(root, text="Your Budget: 0 doubloons")
budget_label.pack()
remaining_label = tk.Label(root, text="Remaining Budget: 0 doubloons")
remaining_label.pack()

# Items display
items_frame = tk.Frame(root)
items_frame.pack(pady=10)

items_canvas = tk.Canvas(items_frame, width=400)  # Set a fixed width for the canvas
items_canvas.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(items_frame, orient="vertical", command=items_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')

items_canvas.configure(yscrollcommand=scrollbar.set)
items_canvas.bind('<Configure>', lambda e: items_canvas.configure(scrollregion=items_canvas.bbox('all')))

items_inner_frame = tk.Frame(items_canvas, width=380)  # Set a fixed width for the inner frame
items_canvas.create_window((0,0), window=items_inner_frame, anchor='nw')

tk.Label(items_inner_frame, text="Shop Items:", font=('Arial', 14, 'bold')).pack()

# Display each item with an "Add to Cart" button
for item in shop_items:
    frame = tk.Frame(items_inner_frame, relief=tk.RIDGE, borderwidth=1, width=380)  # Set width for each item frame
    frame.pack(fill='x', padx=5, pady=5)

    # Layout with "Add to Cart" button included
    item_label = tk.Label(frame, text=f"{item['name']} - {item['price']} doubloons", anchor='w')
    item_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)

    add_button = tk.Button(frame, text="Add to Cart", command=lambda i=item: add_to_cart(i))
    add_button.grid(row=0, column=1, padx=10, pady=5)

# Cart button
cart_button = tk.Button(root, text="View Cart", command=show_cart)
cart_button.pack(pady=10)

root.mainloop()
