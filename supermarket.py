
def add_items(selected_list,items_list):
    selected_keys = input("Enter the keys you want to add to your new list (separated by spaces): ").split()
    list_added_to_cart = [items_list[int(key)] for key in selected_keys if int(key) in items_list]
    print("List of items added to the cart:", list_added_to_cart)
    billing(list_added_to_cart)
def billing(items):
    price={'rice':30 ,'sugar':28,'salt':20,'pepper':15,'water_bottle':20,'noodles':15,'orange_juice':30,'Pen': 5,'Pencil': 3,'Small Size note book': 10,'King size notebook': 15,'Eraser': 2,'Geometry': 10,'Pouch': 8,'chocobar': 10,'mangobar': 12,'Fundae': 8,'ball': 5,'cone': 7,'family pack': 20,'popsicle': 5,'lays': 10,'Bingo': 12,'Brownie': 15,'Kurkure': 8,'potato chips': 10}
    total_price = sum(price[item] for item in items if item in price)
    print("Total Price:", total_price)
    user=input("Do you want to purchase more (yes/no)? : ")
    if user == 'yes':
        main()
    else:
        exit()
def exit():
    print("--------------- THANK YOU FOR VISITING OUR STORE --------------------")
def main():
    print("--------------------- Welcome to Super Market ------------------")
    order={1:'groceries list',2:'Stationary list',3:'Desert list',4:'Snacks list',5:'Exit'}
    groceries_list={1:'rice',2:'sugar',3:'salt',4:'pepper',5:'water bottle',6:'noodles',7:'orange juice'}
    stationary_list={1:'Pen',2:'Pencil',3:'Small Size note book',4:'King size notebook',5:'Eraser',6:'Geometry',7:'Pouch'}
    dessert_list={1:'chocobar',2:'mangobar',3:'Fundae',4:'ball',5:'cone',6:'family pack',7:'popsicle'}
    snack_list={1:'lays',2:'Bingo',3:'Brownie',4:'Kurkure',5:'potato chips'}
    print("**************************** MENU ******************************")
    for key,values in order.items():
        print(key,":",values)
    choice=int(input("Enter your choice : "))
    if choice == 1:
        print("Groceries List:")
        for key,values in groceries_list.items():
            print(key,":",values)
        user_input=input("Do you want to add the items to the cart (yes/no)? : ")
        if user_input == 'yes':
            add_items(groceries_list,groceries_list)
        else:
            exit()
    elif choice == 2:
        print("Stationary List:")
        for key,values in stationary_list.items():
            print(key,":",values)
        user_input=input("Do you want to add the items to the cart (yes/no)? : ")
        if user_input == 'yes':
            add_items(stationary_list,stationary_list)
        else:
            exit()
    elif choice == 3:
        print("Dessert List:")
        for key,values in dessert_list.items():                                                     
            print(key,":",values)
        user_input=input("Do you want to add the items to the cart (yes/no)? : ")
        if user_input == 'yes':
            add_items(dessert_list,dessert_list)
        else:
            exit()
    elif choice == 4:
        print("Snacks List:")
        for key,values in snack_list.items():
            print(key,":",values)
        user_input=input("Do you want to add the items to the cart (yes/no)? : ")
        if user_input == 'yes':
            add_items(snack_list,snack_list)
        else:
            exit()
    else :
        exit()
if __name__ == "__main__":
    main()





