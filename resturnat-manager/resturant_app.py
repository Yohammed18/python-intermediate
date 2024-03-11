from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operator = ''
food_prices = [2.50, 2.25, 2.99, 2.75, 1.99, 2.50, 2.25, 2.75]
drink_prices = [1.50, 0.99, 1.75, 1.50, 1.75, 1.25, 2.50, 1.25]
dessert_prices = [1.50, 1.60, 1.70, 1.80, 2.90, 2.55, 1.95, 1.75]


def click_button(character):
    global operator
    operator = operator+character
    calculator_display.delete(0,END)
    calculator_display.insert(END, operator)

def delete_all():
    global operator
    operator = ''
    calculator_display.delete(0, END)

def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0,END)
    calculator_display.insert(0, result)
    operator = ''

def review_check():
    x = 0
    # food
    for _ in food_box:
        if food_variables[x].get() == 1:
            food_box[x].config(state=NORMAL)
            if food_box[x].get() == '0':
                food_box[x].delete(0, END)
            food_box[x].focus()
        else:
            food_box[x].config(state=DISABLED)
            food_text[x].set('0') 
        x+=1
    # drinks
    x = 0
    for _ in drink_box:
        if drink_variables[x].get() == 1:
            drink_box[x].config(state=NORMAL)
            if drink_box[x].get() == '0':
                drink_box[x].delete(0, END)
            drink_box[x].focus()
        else:
            drink_box[x].config(state=DISABLED)
            drink_text[x].set('0') 
        x+=1
    # dessert
    x = 0
    for _ in dessert_box:
        if dessert_variables[x].get() == 1:
            dessert_box[x].config(state=NORMAL)
            if dessert_box[x].get() == '0':
                dessert_box[x].delete(0, END)
            dessert_box[x].focus()
        else:
            dessert_box[x].config(state=DISABLED)
            dessert_text[x].set('0') 
        x+=1

def total_calculation():
    food_subtotal = 0
    drink_subtotal = 0
    dessert_subtotal = 0
    
    p = 0
    # food
    for unit in food_text:
        food_subtotal = food_subtotal + (food_prices[p] * float(unit.get()))
        p+=1
    
    # drink
    # reset counter for every loop
    p = 0
    for unit in drink_text:
        drink_subtotal = drink_subtotal + (drink_prices[p] * float(unit.get()))
        p+=1

    # dessert
    # reset counter for every loop
    p = 0
    for unit in dessert_text:
        dessert_subtotal = dessert_subtotal + (dessert_prices[p] * float(unit.get()))
        p+=1   

    total_subtotal = food_subtotal+drink_subtotal+dessert_subtotal
    taxes = total_subtotal * 0.11
    total = total_subtotal + taxes


    # display all value tot he cost panel
    food_cost_var.set(f'$ {round(food_subtotal, 2)}')
    drink_cost_var.set(f'$ {round(drink_subtotal, 2)}')
    dessert_cost_var.set(f'$ {round(dessert_subtotal, 2)}')
    subtotal_var.set(f'$ {round(total_subtotal, 2)}')
    taxes_var.set(f'$ {round(taxes, 2)}')
    total_var.set(f'$ {round(total, 2)}')

def create_invoice():
    
    invoice_text.delete(1.0, END)

    invoice_number = f'N# - {random.randint(1000,9999)}'
    current_date = datetime.datetime.now()

    invoice_date = f'{current_date.month}/{current_date.day}/{current_date.year} - {current_date.hour:{current_date.minute}}'

    invoice_text.insert(END, f'Information: \t{invoice_number}\t\t{invoice_date}\n')
    invoice_text.insert(END, f'*'*66+'\n')
    invoice_text.insert(END, f'Items\t\tQuantity\tItems Cost\n')
    invoice_text.insert(END, f'-'*77+'\n')

    x = 0
    for f in food_text:
        if f.get() != '0':
            invoice_text.insert(END, f'{food_list[x]}\t\t{f.get()}\t$ {int(f.get()) * food_prices[x]}\n')
        x+=1

    x = 0
    for d in drink_text:
        if f.get() != '0':
            invoice_text.insert(END, f'{drink_list[d]}\t\t{f.get()}\t$ {int(f.get()) * drink_prices[d]}\n')
        x+=1

    x = 0
    for e in dessert_text:
        if f.get() != '0':
            invoice_text.insert(END, f'{dessert_list[e]}\t\t{f.get()}\t$ {int(f.get()) * dessert_prices[e]}\n')
        x+=1

    invoice_text.insert(END, f'-'*66+'\n')
    invoice_text.insert(END, f'Food Subtotal: \t\t\t{food_cost_var.get()}\n')
    invoice_text.insert(END, f'Drink Subtotal: \t\t\t{drink_cost_var.get()}\n')
    invoice_text.insert(END, f'Dessert Subtotal: \t\t\t{dessert_cost_var.get()}\n')
    invoice_text.insert(END, f'*'*77+'\n')
    invoice_text.insert(END, f'Subtotal: \t\t\t{subtotal_var.get()}\n')
    invoice_text.insert(END, f'Taxes: \t\t\t{taxes_var.get()}\n')
    invoice_text.insert(END, f'Total: \t\t\t{total_var.get()}\n')
    invoice_text.insert(END, f'-'*66+'\n')
    invoice_text.insert(END, f'See you next time.')

def save_invoice():
    invoice_info = invoice_text.get(1.0, END)
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(invoice_info)
    file.close()
    messagebox.showinfo('Notification', 'Your invoice has been saved')

def total_reset():
    invoice_text.delete(0.1, END)

    for text in food_text:
        text.set('0')

    for text in drink_text:
        text.set('0')

    for text in dessert_text:
        text.set('0')


    for box in food_box:
        box.config(state=DISABLED)
     
    for box in drink_box:
        box.config(state=DISABLED)

    for box in dessert_box:
        box.config(state=DISABLED)

    for var in food_variables:
        var.set(0)
    for var in drink_variables:
        var.set(0)
    for var in dessert_variables:
        var.set(0)

    food_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')
    taxes_var.set('')
    subtotal_var.set('')
    total_var.set('')



# initiliaze TKinter
application = Tk()

# Window size
application.geometry('1160x630+-1800+0')

# Prevent from Mazimizing
application.resizable(False, False)

# Window title
application.title('Vegan Resturant - Invoice System')

# background color
application.config(bg='burlywood')

# TOP PANEL
top_panel = Frame(application, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# add panel title
title_tag = Label(top_panel, text='Invoice System', fg='azure4',
                  font=('book antiqua', 50), bg='burlywood', width=27)

# create crid for the top panel
title_tag.grid(row=0, column=0)

# LEFT PANEL
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# COST PANEL
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=50)
cost_panel.pack(side=BOTTOM)

# FOOD PANEL
food_panel = LabelFrame(left_panel, text='Food', font=('book antiqua', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
food_panel.pack(side=LEFT)

# Drink PANEL
drink_panel = LabelFrame(left_panel, text='Drink', font=('book antiqua', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
drink_panel.pack(side=LEFT)

# Dessert PANEL
dessert_panel = LabelFrame(left_panel, text='Dessert', font=('book antiqua', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
dessert_panel.pack(side=LEFT)

# RIGHT PANEL
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# CALCULATOR PANEL
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
calculator_panel.pack()

# INVOICE  PANEL
invoice_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
invoice_panel.pack()

# BUTTON PAENLL
button_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
button_panel.pack()


# PRODUCT LISTS
food_list = ["Chicken", 'Lamb',"Beef", "Pork", "Fish", "Pizza", 'Hakes', 'Kebabs']
drink_list = ['Lemonade', 'Soda', 'Juice', 'Cola','Wine1', 'Wine2','Beer1', 'Beer2']
dessert_list = ['Ice cream', 'Fruit', 'Brownies', 'Pudding', 'Cheesecake', 'Cake1', 'Cake2', 'Yogurt']

# Create food items
food_variables = []
food_box = []
food_text = []
counter = 0

for food in food_list:
    # Create checkbuttons

    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel, 
                       text=food.title(), 
                       font=('book antiqua', 19, 'bold'), 
                       onvalue=1, 
                       offvalue=0, 
                       variable=food_variables[counter],
                       command=review_check
                       )

    food.grid(row=counter, 
              column=0, 
              sticky=W)

    # create input boxes
    food_box.append('')
    food_text.append('')

    # set the input text to zero
    food_text[counter] = StringVar()
    food_text[counter].set('0')

    food_box[counter] = Entry(food_panel,
                              font=('Book Antiqua', 18, 'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=food_text[counter]
                              )
    
    food_box[counter].grid(row=counter,
                           column=1)

    counter+=1

drink_variables = []
drink_box = []
drink_text = []
counter = 0
for drink in drink_list:
    # check box
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel, 
                        text=drink.title(), 
                        font=('book antiqua', 19, 'bold'), onvalue=1, 
                        offvalue=0, 
                        variable=drink_variables[counter],
                        command=review_check)

    drink.grid(row=counter, 
               column=1, 
               sticky=W)
    
    # input boxes
    drink_box.append('')
    drink_text.append('')

    # set the input text to zero
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')

    drink_box[counter] = Entry(drink_panel, 
                               font=('Book Antiqua', 18, 'bold'),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=drink_text[counter])
    # place the box into the proper column and row
    drink_box[counter].grid(row=counter, 
                            column=2)

    counter+=1

dessert_variables = []
dessert_box = []
dessert_text = []
counter = 0
for dessert in dessert_list:
    # Check boxes
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel, 
                          text=dessert.title(), 
                          font=('book antiqua', 19, 'bold'), onvalue=1, 
                          offvalue=0, 
                          variable=dessert_variables[counter],
                          command=review_check)
    # place properly in the colum and row
    dessert.grid(row=counter, 
                 column=2, 
                 sticky=W)
    
        # input boxes
    dessert_box.append('')
    dessert_text.append('')

    # set the input text to zero
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')

    dessert_box[counter] = Entry(dessert_panel, 
                               font=('Book Antiqua', 18, 'bold'),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=dessert_text[counter])
    # place the box into the proper column and row
    dessert_box[counter].grid(row=counter, 
                            column=3)

    counter+=1

# variable that will be use to store the value in the bottom boxes
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()

subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

# COST LABELS AND INPUT FIELDS
# Food cost
food_cost_label = Label(cost_panel,
                        text='Food Cost',
                        font=('Book Antiqua', 12, 'bold'),
                        bg='azure4',
                        fg='white')
food_cost_label.grid(row=0, column=0)
food_cost_text = Entry(cost_panel,
                       font=('Book Antiqua', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=food_cost_var)
# place the text into the right position on the grid
food_cost_text.grid(row=0, column=1,padx=41)

# Drink cost
drink_cost_label = Label(cost_panel,
                        text='Drink Cost',
                        font=('Book Antiqua', 12, 'bold'),
                        bg='azure4',
                        fg='white')
drink_cost_label.grid(row=1, column=0)
drink_cost_text = Entry(cost_panel,
                       font=('Book Antiqua', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=drink_cost_var)
drink_cost_text.grid(row=1, column=1)

# Dessert cost
dessert_cost_label = Label(cost_panel,
                        text='Dessert Cost',
                        font=('Book Antiqua', 12, 'bold'),
                        bg='azure4',
                        fg='white')
dessert_cost_label.grid(row=2, column=0)
dessert_cost_text = Entry(cost_panel,
                       font=('Book Antiqua', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2, column=1)

# subtotal
subtotal_label = Label(cost_panel,
                        text='Sub Total Cost',
                        font=('Book Antiqua', 12, 'bold'),
                        bg='azure4',
                        fg='white')
subtotal_label.grid(row=0, column=2)
subtotal_text = Entry(cost_panel,
                       font=('Book Antiqua', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=subtotal_var)
subtotal_text.grid(row=0, column=3)

# Taxes
taxes_label = Label(cost_panel,
                        text='Taxes',
                        font=('Book Antiqua', 12, 'bold'),
                        bg='azure4',
                        fg='white')
taxes_label.grid(row=1, column=2)
taxes_text = Entry(cost_panel,
                       font=('Book Antiqua', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=taxes_var)
taxes_text.grid(row=1, column=3)

# Total
total_label = Label(cost_panel,
                        text='Total',
                        font=('Book Antiqua', 12, 'bold'),
                        bg='azure4',
                        fg='white')
total_label.grid(row=2, column=2)
total_text = Entry(cost_panel,
                       font=('Book Antiqua', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=total_var)
total_text.grid(row=2, column=3)

# Add Calculator, Check, and Buttons

# Buttons
buttons = ['total', 'invoice', 'save', 'reset']
created_buttons = []
colum = 0
for button in buttons:
    button = Button(
        button_panel,
        text=button.title(),
        font=('Book Antique', 14, 'bold'),
        fg='white',
        bg='azure4',
        bd=1,
        width=9
    )
    created_buttons.append(button)
    button.grid(row=0,
                column= colum)
    colum += 1


created_buttons[0].config(command=total_calculation)
created_buttons[1].config(command=create_invoice)
created_buttons[2].config(command=save_invoice)
created_buttons[3].config(command=total_reset)


# Invoice
invoice_text = Text(invoice_panel,
                    font=('Book Antique', 14, 'bold'),
                    bd=1,
                    width=42,
                    height=10)

invoice_text.grid(row=0,
                  column=0)

# Calculator
calculator_display = Entry(calculator_panel,
                           font=('Book Antique', 16, 'bold'),
                           width=40,
                           bd=1)


calculator_display.grid(row=0,
                        column=0,
                        columnspan=4)

# createa loop that will place each element in the calculator display
calculator_buttons = ['7', '8', '9', '+',
                      '4', '5', '6', '-',
                      '1', '2', '3', '*',
                      'CE', 'Delete', '0', '/',
                      ]

stored_buttons = []

my_row = 1
my_column = 0

for button in calculator_buttons:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=('Book Antique', 16, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=8)
    
    stored_buttons.append(button)

    button.grid(row=my_row,
                column=my_column)
    
    if my_column == 3:
        my_row+=1

    my_column+=1

    if my_column == 4:
        my_column = 0


for index in range(0,16):
    if calculator_buttons[index] == 'Delete':
        stored_buttons[index].config(command=delete_all)
    elif calculator_buttons[index] == 'CE':
        stored_buttons[index].config(command=get_result)
    else:
        cal_val = calculator_buttons[index]
        stored_buttons[index].config(command=lambda char=cal_val: click_button(char))
        






































































# prevent window from closing
application.mainloop()


# To learn more about TKinter visit https://docs.python.org/3/library/tk.html