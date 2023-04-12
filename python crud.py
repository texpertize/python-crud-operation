# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:14:21 2023

@author: aryan
"""

items = []

def create_item():
    item_id = int(input('Enter item ID: '))
    name = input('Enter name: ')
    description = input('Enter description: ')
    item = {'id': item_id, 'name': name, 'description': description}
    items.append(item)
    print('Item created successfully\n')

def read_all_items():
    print('All items:')
    for item in items:
        print(f"{item['id']}: {item['name']} ({item['description']})")
    print()

def read_item():
    item_id = int(input('Enter item ID: '))
    item = None
    for i in items:
        if i['id'] == item_id:
            item = i
            break
    if item:
        print(f"{item['id']}: {item['name']} ({item['description']})\n")
    else:
        print('Item not found\n')

def update_item():
    item_id = int(input('Enter item ID: '))
    for item in items:
        if item['id'] == item_id:
            name = input('Enter new name (leave blank to keep existing name): ')
            if name:
                item['name'] = name
            description = input('Enter new description (leave blank to keep existing description): ')
            if description:
                item['description'] = description
            print('Item updated successfully\n')
            return
    print('Item not found\n')

def delete_item():
    item_id = int(input('Enter item ID: '))
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            print('Item deleted successfully\n')
            return
    print('Item not found\n')

# Main loop
while True:
    print('1. Create item')
    print('2. Read all items')
    print('3. Read item')
    print('4. Update item')
    print('5. Delete item')
    print('6. Quit')
    choice = input('Enter your choice: ')
    print()
    
    if choice == '1':
        create_item()
    elif choice == '2':
        read_all_items()
    elif choice == '3':
        read_item()
    elif choice == '4':
        update_item()
    elif choice == '5':
        delete_item()
    elif choice == '6':
        print('Goodbye!')
        break
    else:
        print('Invalid choice\n')
