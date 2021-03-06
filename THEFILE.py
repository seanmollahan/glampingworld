from tkinter import * # Import tkinter
    
class OrderApplication:
    def __init__(self):
        self.window = Tk() # Create a window
        self.window.title("GW Order Processing Application") # Set title of a window
        photo = PhotoImage(file="P:\GWlogo.gif") # specify the path to your file
        label = Label(self.window, image=photo)  #put the image in a label to disdaply it in the window
        label.grid(sticky = W, column = 1, row = 0)  # show the label on the screen
        
        


        #set up labels the left column of the window (Aligned left)
        lbl = Label(self.window, text ="Customer Name:", font = "Times 12 bold")
        lbl.grid(sticky = W, column = 0, row = 2,)
        lbl = Label(self.window, text ="Product Name:", font = "Times 12 bold")
        lbl.grid(sticky = W, column = 0, row = 3)
        lbl = Label(self.window, text ="Product ID:", font = "Times 12 bold")
        lbl.grid(sticky = W, column = 0, row = 4)
        lbl = Label(self.window, text ="Product Quantity:", font = "Times 12 bold")
        lbl.grid(sticky = W, column = 0, row = 5)
        lbl = Label(self.window, text = "Product Price (USD):", font = "Times 12 bold")
        lbl.grid(sticky = W, column = 0, row = 6)
        lbl = Label(self.window, text ="Subtotal:", font = "Times 12 bold")
        lbl.grid(sticky = W, column = 0, row = 8)
        lbl = Label(self.window, text = "Order Total (USD):", font = "Times 12 bold")
        lbl.grid(sticky = W, column = 0, row = 10)
        w = Checkbutton(self.window, text = "2% discount", onvalue = 0.02, font = "Times 12 bold", command = self.checkbuttonvalue1).grid(sticky = W, row = 7, column = 1)
        x = Checkbutton(self.window, text = "No discount", onvalue = 0.02, font = "Times 12 bold", command = self.checkbuttonvalue2).grid(sticky = E, row = 7, column = 1)

        # set up the input area and assigning variables
        self.CustomerNameVar = StringVar()
        Entry(self.window, width = 51, textvariable = self.CustomerNameVar).grid(sticky = W, row = 2, column = 1)
        self.ProductNameVar = StringVar()
        Entry(self.window, width = 51, textvariable = self.ProductNameVar).grid(sticky = W, row = 3, column = 1)
        self.ProductIDVar = StringVar()
        Entry(self.window, width = 51, textvariable = self.ProductIDVar).grid(sticky = W, row = 4, column = 1)
        self.ProductQuantityVar = StringVar()
        Entry(self.window, width = 51, textvariable = self.ProductQuantityVar).grid(sticky = W, row = 5, column = 1)
        self.ProductPriceVar = StringVar()
        Entry(self.window, width = 51, textvariable = self.ProductPriceVar).grid(sticky = W, row = 6, column = 1)
        
        #set up the output area using two labels and two buttons
        self.subTotalVar = StringVar()
        Label(self.window, textvariable = self.subTotalVar, font = "Times 12 bold").grid(sticky = W, column = 1, row = 8)
        self.orderTotalVar = StringVar()
        Label(self.window, textvariable = self.orderTotalVar, font = "Times 12 bold").grid(sticky = W, column = 1, row = 10)
        R1 = Radiobutton(self.window, text = "English", font = "Times 12 bold"). grid(row = 0, column = 0, sticky = W)
        Button(self.window, text = "Calculate Order Total", font = "Times 14 bold", bg="green", fg="black", command = self.computeTotal).grid(row = 11, column = 0, sticky = W)
        Button(self.window, text = "Help", font = "Times 14 bold", bg="yellow", fg="black").grid(row = 11, column = 1, sticky = E)
        
        
        
            
                
        self.window.mainloop() # Create an event loop to display the window


    


    def computeTotal(self):
            subTotal = self.getSubtotal(
                float(self.ProductPriceVar.get()),
                int(self.ProductQuantityVar.get()))
            self.subTotalVar.set(format(subTotal, '10.2f'))
            lbl = Label(self.window, text = "Sales Tax:", font = "Times 12 bold")
            lbl.grid(sticky = W, column = 0, row = 9)
            lbl = Label(self.window, text = "      13%", font = "Times 12 bold")
            lbl.grid(sticky = W, column = 1, row = 9)
            orderTotal = float(self.subTotalVar.get()) * 0.13 + float(self.subTotalVar.get())
            self.orderTotalVar.set(format(orderTotal, '10.2f',))
        
        
    def getSubtotal(self, Productprice, Productquantity):
            subTotal = (Productprice * Productquantity)
            if checkbutton2 == 1:
                subTotal1 = subTotal * 0.98
                return subTotal1
            else:
                return subTotal

    def checkbuttonvalue1(self):
        global checkbutton2
        checkbutton2 = 1

    def checkbuttonvalue2(self):
        global checkbutton2
        checkbutton2 = 0
        
OrderApplication()  # Create GUI