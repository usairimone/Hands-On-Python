title = "Bill"
print(f"{title:-^60}")
# initialize float values
item1 = float(45)
item2 = float(15)
item3 = float(8.75)

# add all 3 items
subtotal = item1 + item2 + item3
# calculate gst at 18%
gst = 18 * (subtotal/100)
# calculate total
total = subtotal + gst

# print all items and subtotal,gst and total
print(f"Item 1 (Notebook): Rs {item1}")
print(f"Item 2 (Pen): Rs {item2}")
print(f"Item 3 (Eraser): Rs {item3}\n")
print(f"Subtotal: Rs {subtotal}")
print(f"GST (18%) : Rs {gst}")
print(f"Total: Rs {total}")