#Zomato(Python)
from dictionaries import rest_list
def ownerUpdates(rest_s):#owner updates the information/menu
    rest_sel=int(rest_s)
    choice=True
    while choice==True:
        rest_act=int(raw_input("Actions:\n1- Update an Item\n2- Add an Item\n3- Delete an Item\n4- To Move Ahead\n--> "))
        if rest_act==1:
            rest_item_name=raw_input("Enter the name of the Item: ")
            rest_item_rate=raw_input("Enter the Updated Price: ")
            if rest_sel==1:
                rest_list['Dominos Pizza']['Menu'][rest_item_name]['Price']=rest_item_rate
            elif rest_sel==2:
                rest_list['Shree Ratnam']['Menu'][rest_item_name]['Price']=rest_item_rate
            choice=True
        elif rest_act==2:
            rest_item_name = raw_input("Enter the name of the Item: ")
            rest_new_rate = raw_input("Enter the rate of new item: ")
            if rest_sel==1:
                rest_list['Dominos Pizza']['Menu'].update({rest_item_name: {'Price': rest_new_rate}})
            elif rest_sel==2:
                rest_list['Shree Ratnam']['Menu'].update({rest_item_name: {'Price': rest_new_rate}})
            choice = True
        elif rest_act==3:
            rest_item_name = raw_input("Enter the name of the Item: ")
            if rest_sel==1:
                del rest_list['Dominos Pizza']['Menu'][rest_item_name]
            elif rest_sel==2:
                del rest_list['Shree Ratnam']['Menu'][rest_item_name]
            choice = True
        elif rest_act==4:
            choice=False
    return
def rating(rest_as):#customer rates the restaurant
    rest_rate=int(raw_input("Rate The Restaurant\n1- OK Rate\n2- No\n--> "))
    if rest_rate==1:
        rate=raw_input("Rate out of 5 Star; ")
        if rest_as == 1:
            rest_list['Dominos Pizza']['Rating'] = rate
            return False
        elif rest_as == 2:
            rest_list['Shree Ratnam']['Rating'] = rate
            return False
    elif rest_rate==2:
        return

def selectMethod():#customer choose delievery method
    rest_del_method = int(raw_input("Delievery Method:\n1- Walk-In\n2- Delievery\n-->"))
    if rest_del_method == 1:
        print "Choosen Method is Walk-In"
        return
    elif rest_del_method==2:
        print "Choosen Method is Delievery"
        return

def confirmOrder():#confirmation asked by user
    order_add = int(raw_input("Press 1 to add more\nPress 0 to confirm\n--> "))
    if order_add == 1:
        return True
    elif order_add == 0:
        return False

def order(rest_a):#customer choose restaurant and then starts ordering the food
    if rest_a == 1:
        print rest_list['Dominos Pizza']
        rest_order_ask = int(raw_input("Choose:\n1- Order the food\n2- Select Another Restaurant\n--> "))
        choice = True
        cost = 0
        if rest_order_ask == 1:
            while choice == True:
                rest_add = int(raw_input("Select:\n1- 5Pepper\n2- Farmhouse\n3- Country Special\n4- Peppy Paneer\n--> "))
                if rest_add == 1:
                    cost = cost + int(rest_list['Dominos Pizza']['Menu']['5Pepper']['Price'])
                elif rest_add == 2:
                    cost = cost + int(rest_list['Dominos Pizza']['Menu']['Farmhouse']['Price'])
                elif rest_add == 3:
                    cost = cost + int(rest_list['Dominos Pizza']['Menu']['Country Special']['Price'])
                elif rest_add == 4:
                    cost = cost + int(rest_list['Dominos Pizza']['Menu']['Peppy Paneer']['Price'])
                else:
                    print "Wrong Choice"
                choice=confirmOrder()
            print "Your order costs Rs." + str(cost+(cost * 0.01)+(cost * 0.06)+(cost * 0.15)) + "(including 10% service charge, 6% service tax & 15% VAT)"
            c=rating(rest_ask)
            return c
        elif rest_order_ask == 2:
            return True
    elif rest_ask == 2:
        print rest_list['Shree Ratnam']
        rest_order_ask = int(raw_input("Choose:\n1- Order the food\n2- Select Another Restaurant\n--> "))
        choice = True
        cost = 0
        if rest_order_ask == 1:
            while choice == True:
                rest_add = int(raw_input("Select:\n1- Kadhai Paneer\n2- Paneer Korma\n3- Dal Makhni\n4- Roti\n--> "))
                if rest_add == 1:   #after customer choose the item, we are calculate the cost of the items
                    cost = cost + int(rest_list['Shree Ratnam']['Menu']['Kadhai Paneer']['Price'])
                elif rest_add == 2:
                    cost = cost + int(rest_list['Shree Ratnam']['Menu']['Paneer Korma']['Price'])
                elif rest_add == 3:
                    cost = cost + int(rest_list['Shree Ratnam']['Menu']['Dal Makhni']['Price'])
                elif rest_add == 4:
                    cost = cost + int(rest_list['Shree Ratnam']['Menu']['Roti']['Price'])
                else:
                    print "Wrong Choice"
                choice=confirmOrder()
                print "Your order costs Rs." + str(cost + (cost * 0.01) + (cost * 0.06) + (cost * 0.15)) + "(including 10% service charge, 6% service tax & 15% VAT)" #print total cost of the bill after including all the taxes
            c=rating(rest_ask)
            return c
        elif rest_order_ask == 2:
            return True
    return

print "ZOMATO"
choice=True
while choice==True:
    rest_person=int(raw_input("1- OWNER\n2- CUSTOMER\n3- QUIT\n--> "))
    choice2=True
    while choice2==True:
        if rest_person==1:
            rest_info_update=int(raw_input("1- To Update Information\n0- To Move Ahead\n--> "))
            if rest_info_update==1:
                rest_sel=int(raw_input("Select Restaurant:\n1- Domino's Pizza\n2- Shree Ratnam\n--> "))
                ownerUpdates(rest_sel)#goto owner's update information menu
            elif rest_info_update==0:
                choice2=False
        elif rest_person==2:
            rest_ask = int(raw_input("Select Restaurant:\n1-> Domino's Pizza\n2-> Shree Ratnam\n--> "))
            selectMethod()#ask customer delievery method
            c=order(rest_ask)
            choice2=c
        elif rest_person==3:
            print "Thank You\nHave A Nice Day"
            choice=False #program end
            break