# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 20:28:41 2019

@author: USER
"""



from datetime import datetime


class InventoryProduct:  #this is our inventory class
        
    def __init__(self, name , price, stock_amount):
        self.name = name
        self.price = price
        self.stock_amount = stock_amount



class Basket:  #this basket class is each user's basket
    
    def __init__(self, contents, total_value):
        self.contents = contents
        self.total_value = total_value
        self.current_user = None
        
        
    def set_total(self):  # when we call this method, it calculates the total_value of the basket
        self.total_value = 0
        for i in self.contents:
            self.total_value += bounmarket.inventory[i].price * self.contents[i][1]
        
        
    def display_contents(self):  # this shows the contents of the basket when needed
        self.set_total()
        if len(self.contents) == 0:
            print('Your basket is empty. Total value = $0')
        else:
            print('Your basket contains: ')
            for item in self.contents:
                print(str(list(self.contents.keys()).index(item)+1) + '.' + item + 
                      ' price= $' + str(self.contents[item][0].price) +
                      ' amount= ' + str(self.contents[item][1]) +
                      ' total= $' + str(self.contents[item][1] * self.contents[item][0].price))
            
            print('Total $' + str(self.total_value))
    
    
    def set_current_user(self, user): # to call user in main menu
        self.current_user=user
            
    def show_basket_submenu(self): 
        while True:
            choice = input('''Please choose an option:  
        1.Update amount 
        2.Remove an item 
        3.Check out 
        4.Go back to main menu 
 
Your selection: ''')
            if choice == '1':
                return self.update_item()
            elif choice == '2':
                return self.remove_item()
            elif choice == '3':
                return bounmarket.check_out(self.current_user)
            elif choice == '4':
                return bounmarket.show_market_menu(self.current_user)
            else:
                print('Please provide a valid selection!')
     
        
    def add_item(self, product, amount):  # to add item into the user's basket
        if product in self.contents.keys():
            self.contents[product][1] += amount
            bounmarket.update_stock_amount(product, amount)
            self.set_total()
            self.display_contents()
            print('Remaining ' + product + ' amount ' + str(bounmarket.inventory[product].stock_amount))
            return self.show_basket_submenu()
        else:
            self.contents[product] = [bounmarket.inventory[product], amount]
            bounmarket.update_stock_amount(product, amount)
            self.set_total()
            self.display_contents()
            print('Remaining ' + product + ' amount ' + str(bounmarket.inventory[product].stock_amount))
            return self.show_basket_submenu()
        
        
        
    def remove_item(self):  # to remove selected item from the basket
        self.display_contents()
        while True:
            number = input('Please enter which item you want to remove from your basket (Enter 0 for main menu): ')
            b = True
            for i in number:
                if i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    pass
                else:
                    b = False
            if b == False:
                print('Please provide a valid number!')
            else:
                number = int(number)
                if number == '0':
                    return self.show_basket_submenu()
                else:
                    if int(number) > len(self.contents):
                        print('Please provide a valid item number!')
                    else:
                        bounmarket.update_stock_amount(list(self.contents.keys())[number - 1], self.contents[list(self.contents.keys())[number - 1]][1] * (-1))
                        del self.contents[list(self.contents.keys())[number - 1]]
                        self.set_total()
                        self.display_contents()
                        return self.show_basket_submenu()
            
        
    def update_item(self):  # to update the amount of an item in the basket
        items = list(self.contents.keys())
        if len(self.contents) == 0:
            print('Your basket is empty. Total value = $0')
            return self.show_basket_submenu()
        else:
            self.display_contents()
            while True:
                item_no = input('Please enter which item you want to update: ')
                b = True
                for i in item_no:
                    if i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                        pass
                    else:
                        b = False
                if b == False:
                    print('Please provide a valid number!')
                else:
                    item_no = int(item_no)
                    if item_no not in range(0, len(self.contents) + 1, 1):
                        print('Please enter a valid choice!')
                    else:
                        howmany = int(input('Please enter the new amount: '))
                        if howmany > bounmarket.inventory[items[item_no - 1]].stock_amount + self.contents[items[item_no - 1]][1]:
                            print('The amount you enter exceeds the stock amount!')
                        else:
                            bounmarket.update_stock_amount(items[item_no - 1], howmany - self.contents[items[item_no - 1]][1])
                            self.contents[items[item_no - 1]][1] = howmany
                            self.check_amount(items[item_no - 1])
                            self.set_total()
                            self.display_contents()
                            return self.show_basket_submenu()
                    
                    
    def check_amount(self, product): # after update_item method, we call this to remove an item if the amount is 0
        if self.contents[product][1] == 0:
            del self.contents[product]

                

class Market:
    
    def __init__(self, inventory = {}, users = {}):
        self.inventory = inventory
        self.users = users
        inventory_dict = {'asparagus':[10,5],
                          'broccoli':[15,6],
                          'carrots':[18,7], 
                          'apples':[20,5],
                          'banana':[10,8],
                          'berries':[30,3],
                          'eggs':[50,2],
                          'mixed fruit juice':[0,8],
                          'fish sticks':[25,12],
                          'ice cream':[32,6], 
                          'apple juice':[40,7],
                          'orange juice':[30,8],
                          'grape juice':[10,9]}
        for item in inventory_dict:
            self.inventory[item] = InventoryProduct(item, inventory_dict[item][1], inventory_dict[item][0])
        
        
    
    
    def show_market_menu(self, user):  # this is main menu after login
        while True:
            ch = input('''Please choose one of the following services:
    
    1.Search for a product   
    2.See Basket   
    3.Check Out   
    4.Logout   
    5.Exit 
    
Your Choice: ''')
                
            if ch not in ('1','2','3','4','5'):
                print('Please provide a valid menu number!')
                
            else:
                if ch == '1':
                    return self.search(user)
                elif ch == '2':
                    self.users[user].basket.display_contents()
                    return self.users[user].basket.show_basket_submenu()
                elif ch == '3':
                    return self.check_out(user)
                elif ch == '4':
                    return self.login()
                elif ch == '5':
                    print('''We are looking forward to seeing you again!

Have a nice day!''')
                    break
                
        
    def search(self, user): # this helps user to make a search in inventory and add that item in their basket after required controls 
        items_to_show = []
        
        while True:
            keyword = input('What are you searching for? ').lower()
            
            for item in self.inventory.keys():
                if keyword in item and self.inventory[item].stock_amount > 0:
                    items_to_show.append(item)
            
            if len(items_to_show) == 0:
                print('No items found!')
            else:
                break
            
        print('found ' + str(len(items_to_show)) + ' similar items')
        for i in range(len(items_to_show)):
            print(str(i+1)+'.'+items_to_show[i]+'- $'+str(self.inventory[items_to_show[i]].price))
        
        while True:
            a = True
            option = input('Please select which item you want to add to your basket (Enter 0 for main menu):')
            for i in option:
                if i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    pass
                else:
                    a = False
            if a == False:
                print('Please provide a valid number!')
            else:
                if int(option) not in range(0, len(items_to_show)+1, 1):
                    print('Please enter a valid choice!')
                else:
                    if option == '0':
                        return self.show_market_menu(user)
                    else:
                        while True:
                            nmbr = input('How many of the item do you want to add to your basket (Enter 0 for main menu): ')
                            b = True
                            for i in nmbr:
                                if i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                                    pass
                                else:
                                    b = False
                            if b == False:
                                print('Please provide a valid number!')
                            else:
                                nmbr = int(nmbr)
                                if nmbr == 0:
                                    return self.show_market_menu(user)
                                elif nmbr > self.inventory[items_to_show[int(option) -1]].stock_amount:
                                    print('Sorry! The amount exceeds the limit, Please try again with smaller amount (Enter 0 for main menu):')
                                else:
                                    print(self.users[user].username)
                                    return self.users[user].basket.add_item(items_to_show[int(option)-1], nmbr)
                        
                
    def update_stock_amount(self, product_name, sold_amount): # to update stock amount after add_item, update_item, remove_item
        self.inventory[product_name].stock_amount -= sold_amount
        
        
    def check_out(self, user): # check out and print receipt
        self.users[user].basket.set_total()
        now = datetime.now()
        print('''Processing your receipt...
              
******* BOUN Online Market ********

************************************  
        4444034 
        boun.edu.tr 
------------------------------------''')
        for key in self.users[user].basket.contents.keys():
            print(key + ' $' + str(self.inventory[key].price) + ' amount=' + 
                  str(self.users[user].basket.contents[key][1]) + ' total= ' + 
                  str(self.users[user].basket.contents[key][1] * self.inventory[key].price))
        print('------------------------------------')
        print('Total  $' + str(self.users[user].basket.total_value))
        print('------------------------------------')
        print(now.strftime('%d/%m/%Y     %H:%M:%S'))
        print('Thank you for using our market!')
        self.users[user].basket.contents = {}
        self.users[user].basket.set_total()
        return self.show_market_menu(user)
        
        
    def login(self): # our program starts with this method of our market class
        while True:
            un = input('''
****Welcome to BOUN Online Market**** 

Please log in by providing your user credentials:

User Name (You can enter "exit" to quit): ''')
            if un.lower() == 'exit':
                print('''We are looking forward to seeing you again!

Have a nice day!''')
                break
            else:
                pw = input('Password (You can enter "exit" to quit): ')
                if pw.lower() == 'exit':
                    print('''We are looking forward to seeing you again!
    
Have a nice day!''')
                    break
                else:
                    if un in self.users.keys():
                        if pw == self.users[un].password:
                            print('''Successfully logged in!
        
Welcome, ''' + un + '''! 

Please choose one of the following options by entering the corresponding menu number.''')
                            self.users[un].basket.set_current_user(un)
                            print(self.users[un].basket.contents.keys())
                            return self.show_market_menu(un)
                        else:
                            print('Your user name and/or password is not correct. Please try again!')
                    else:
                        print('Your user name and/or password is not correct. Please try again!')
            


class User: # we define each user as an object of this class
    
    def __init__(self, username, password, basket):
        self.username = username
        self.password = password
        self.basket = basket




myusers = {'ahmet' : User('ahmet', '1234', Basket({}, 0)),
           'meryem' : User('meryem', '4444', Basket({}, 0))}

bounmarket = Market(users=myusers)

bounmarket.login()
        

