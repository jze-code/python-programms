import tkinter as tk
from tkinter import ttk,messagebox
class RestaurantOrderMnagement:
    def __init__(self,root):
        self.root= root
        self.root.title("restaurant mangement app")
        self.menu_items ={
            "FRIES MEAL": 2,
            "LUNCH MEAl": 2,
            "DRINKS":1

        }
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5
                    anchor=tk.CENTER)
        ttk.Label(frame,
                  text="restaurant order management").grid(row=0,
                                                           columnspan=3)
        self.menu_labels={}
        self.menu_quantities={}
        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,
                            text=f"(item) ($[price]):",)
            label.grid(row=1,column=0)
            self.menu_labels[item]=label
            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=1,column=1)
            self.menu_quantities[item]=quantity_entry
        order_button=ttk.Button(frame,
                                         text="Place Order",
                                         command=self.place_order)
        order_button.grid(row=len(self.menu_items)+2,
                         columnsspan=3)
    def place_order(self):
        total_coast=0
        order_summary="Order summary:\n"
        for item,entry in self.menu_quantities.items():
            quantity=entry.get()
            if quantity.isdigit():
                quantity=int(quantity)
                price=self.menu_items[item]
                cost=quantity*price
                total_cost+=cost
                if quantity>=0:
                    order_summary+=F"\nTotal Cost:{total_cost}"
                    messagebox.showinfo(
                        "order placed"
                        order_summary)
                else:
                    messagebox.showerror("Error","please oreder at least one item")
                if __name__=="__main__":
                    root=tk.Tk()
                    app=RestaurantOrderMnagement(root)
                    root.geometry("800x600")
                    root.mainloop()

                    


        

    