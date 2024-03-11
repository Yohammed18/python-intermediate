from tkinter import *


operator = ''

def click_button(character):
    global operator
    operator = operator+character
    calculator_display.delete(0,END)
    calculator_display.insert(END, operator)


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
                       onvalue=1, offvalue=0, variable=food_variables[counter])

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
                        variable=drink_variables[counter])

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
                          variable=dessert_variables[counter])
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

    button.grid(row=0,
                column= colum)
    colum += 1

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
                      '1', '2', '3', 'x',
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
    if calculator_buttons[index] == 'CE' or calculator_buttons[index] == 'Delete':
        index+=1
    else:
        cal_val = calculator_buttons[index]
        stored_buttons[index].config(command=lambda char=cal_val: click_button(char))
        







































































# prevent window from closing
application.mainloop()


# To learn more about TKinter visit https://docs.python.org/3/library/tk.html