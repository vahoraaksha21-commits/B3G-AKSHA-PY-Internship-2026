inventory={
    "Pen":100,
    "NoteBook":50
}

inventory["Pen"] = inventory["Pen"] + 10
product="NoteBook"

if "NoteBook" in inventory:
    inventory["NoteBook"]=inventory["NoteBook"]-1
    print("NoteBook Sold")
else:
    print("NoteBook Not Found")
    product="Bag"

if "Bag" in inventory:
    inventory["Bag"]=inventory["Bag"]-1
else:
    print("Bag Not Found")
    print("Updated Inventory:")
    print(inventory)