from tkinter import *

expenses = 4681.38
aj_wage = 400 #Weekly
chelcie_wage = 1866.51 #Biweekly

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):

		#Labels

		self.aj_funds_label = Label(self, text= "A.J.'s Current Funds:")
		self.aj_funds_label.grid(row= 0, column= 0, columnspan= 2, sticky= W)

		self.chelcie_funds_label = Label(self, text= "Chelcie's Current Funds:")
		self.chelcie_funds_label.grid(row= 1, column= 0, columnspan= 2, sticky= W)

		self.cost_label = Label(self, text= "Planned Expense:")
		self.cost_label.grid(row= 2, column= 0, columnspan= 2, sticky= W)

		self.funds_display_label = Label(self, text= "Current Funds After Purchase:")
		self.funds_display_label.grid(row= 3, column= 0, columnspan= 2, sticky= W)

		self.aj_upcoming_checks_label = Label(self, text= "AJ checks by upcoming 1st:")
		self.aj_upcoming_checks_label.grid(row= 4, column= 0, columnspan= 2, sticky= W)

		self.chelcie_upcoming_checks_label = Label(self, text= "Chelcie checks by upcoming 1st:")
		self.chelcie_upcoming_checks_label.grid(row= 5, column= 0, columnspan= 2, sticky= W)

		self.upcoming_cost_label = Label(self, text= "Planned Expense for Upcoming Month:")
		self.upcoming_cost_label.grid(row= 6, column= 0, columnspan= 2, sticky= W)

		self.upcoming_funds_display_label = Label(self, text= "Funds After Expenses for Upcoming Month:")
		self.upcoming_funds_display_label.grid(row= 7, column= 0, columnspan= 2, sticky= W)

		self.aj_next_checks_label = Label(self, text= "AJ checks by next 1st:")
		self.aj_next_checks_label.grid(row= 8, column= 0, columnspan= 2, sticky= W)

		self.chelcie_next_checks_label = Label(self, text= "Chelcie checks by next 1st:")
		self.chelcie_next_checks_label.grid(row= 9, column= 0, columnspan= 2, sticky= W)

		self.next_cost_label = Label(self, text= "Planned Expense for Next Month:")
		self.next_cost_label.grid(row= 10, column= 0, columnspan= 2, sticky= W)

		self.next_funds_display_label = Label(self, text= "Funds After Expenses for Next Month:")
		self.next_funds_display_label.grid(row= 11, column= 0, columnspan= 2, sticky= W)

		self.aj_following_checks_label = Label(self, text= "AJ checks by following 1st:")
		self.aj_following_checks_label.grid(row= 12, column= 0, columnspan= 2, sticky= W)

		self.chelcie_following_checks_label = Label(self, text= "Chelcie checks by following 1st:")
		self.chelcie_following_checks_label.grid(row= 13, column= 0, columnspan= 2, sticky= W)

		self.following_cost_label = Label(self, text= "Planned Expense for Following Month:")
		self.following_cost_label.grid(row= 14, column= 0, columnspan= 2, sticky= W)

		self.following_funds_display_label = Label(self, text= "Funds After Expenses for Following Month:")
		self.following_funds_display_label.grid(row= 15, column= 0, columnspan= 2, sticky= W)

		#Entry Fields

		self.aj_funds_entry = Entry(self)
		self.aj_funds_entry.grid(row= 0, column= 2, sticky= W)

		self.chelcie_funds_entry = Entry(self)
		self.chelcie_funds_entry.grid(row= 1, column= 2, sticky= W)

		self.cost_entry = Entry(self)
		self.cost_entry.grid(row= 2, column= 2, sticky= W)

		self.aj_upcoming_checks_entry = Entry(self)
		self.aj_upcoming_checks_entry.grid(row= 4, column= 2, columnspan= 2, sticky= W)

		self.chelcie_upcoming_checks_entry = Entry(self)
		self.chelcie_upcoming_checks_entry.grid(row= 5, column= 2, columnspan= 2, sticky= W)

		self.upcoming_cost_entry = Entry(self)
		self.upcoming_cost_entry.grid(row= 6, column= 2, columnspan= 2, sticky= W)

		self.aj_next_checks_entry = Entry(self)
		self.aj_next_checks_entry.grid(row= 8, column= 2, columnspan= 2, sticky= W)

		self.chelcie_next_checks_entry = Entry(self)
		self.chelcie_next_checks_entry.grid(row= 9, column= 2, columnspan= 2, sticky= W)

		self.next_cost_entry = Entry(self)
		self.next_cost_entry.grid(row= 10, column= 2, columnspan= 2, sticky= W)

		self.aj_following_checks_entry = Entry(self)
		self.aj_following_checks_entry.grid(row= 12, column= 2, columnspan= 2, sticky= W)

		self.chelcie_following_checks_entry = Entry(self)
		self.chelcie_following_checks_entry.grid(row= 13, column= 2, columnspan= 2, sticky= W)

		self.following_cost_entry = Entry(self)
		self.following_cost_entry.grid(row= 14, column= 2, columnspan= 2, sticky= W)

		#Buttons

		self.calculate_funds= Button(self, text="Calculate", command= self.funds_calculate)
		self.calculate_funds.grid(row=3, column=4, sticky= W)

		self.calculate_upcoming_funds= Button(self, text="CAN", command= self.upcoming_funds_calculate)
		self.calculate_upcoming_funds.grid(row=7, column=4, sticky= W)

		self.calculate_next_funds= Button(self, text="WE", command= self.next_funds_calculate)
		self.calculate_next_funds.grid(row=11, column=4, sticky= W)

		self.calculate_following_funds= Button(self, text="AFFORD IT!?!", command= self.following_funds_calculate)
		self.calculate_following_funds.grid(row=15, column=4, sticky= W)

		#Text Widget

		self.funds_display = Text(self, width = 15, height= 1, wrap= WORD)
		self.funds_display.grid(row= 3, column= 2, columnspan= 2, sticky= W)

		self.upcoming_funds_display = Text(self, width = 15, height= 1, wrap= WORD)
		self.upcoming_funds_display.grid(row= 7, column= 2, columnspan= 2, sticky= W)

		self.next_funds_display = Text(self, width = 15, height= 1, wrap= WORD)
		self.next_funds_display.grid(row= 11, column= 2, columnspan= 2, sticky= W)

		self.following_funds_display = Text(self, width = 15, height= 1, wrap= WORD)
		self.following_funds_display.grid(row= 15, column= 2, columnspan= 2, sticky= W)

	def funds_calculate(self):
		aj_funds = float(self.aj_funds_entry.get())
		chelcie_funds = float(self.chelcie_funds_entry.get())
		cost = float(self.cost_entry.get())
		funds= aj_funds + chelcie_funds - cost
		self.funds_display.delete(0.0, END)
		self.funds_display.insert(0.0, "$%.2f" % funds)

	def upcoming_funds_calculate(self):
		aj_new_funds_upcoming = aj_wage * int(self.aj_upcoming_checks_entry.get())
		chelcie_new_funds_upcoming = chelcie_wage * int(self.chelcie_upcoming_checks_entry.get())
		upcoming_funds = (float(self.aj_funds_entry.get()) + float(self.chelcie_funds_entry.get()) - float(self.cost_entry.get())) + aj_new_funds_upcoming + chelcie_new_funds_upcoming - expenses - float(self.upcoming_cost_entry.get())
		self.upcoming_funds_display.delete(0.0, END)
		self.upcoming_funds_display.insert(0.0, "$%.2f" % upcoming_funds)

	def next_funds_calculate(self):
		aj_new_funds_next = aj_wage * int(self.aj_next_checks_entry.get())
		chelcie_new_funds_next = chelcie_wage * int(self.chelcie_next_checks_entry.get())
		next_funds = ((float(self.aj_funds_entry.get()) + float(self.chelcie_funds_entry.get()) - float(self.cost_entry.get())) + (aj_wage * int(self.aj_upcoming_checks_entry.get()) + chelcie_wage * int(self.chelcie_upcoming_checks_entry.get()) - float(self.upcoming_cost_entry.get()) - expenses)) + aj_new_funds_next + chelcie_new_funds_next - expenses - float(self.next_cost_entry.get())
		self.next_funds_display.delete(0.0, END)
		self.next_funds_display.insert(0.0, "$%.2f" % next_funds)

	def following_funds_calculate(self):
		aj_new_funds_following = aj_wage * int(self.aj_following_checks_entry.get())
		chelcie_new_funds_following = chelcie_wage * int(self.chelcie_following_checks_entry.get())
		following_funds = ((float(self.aj_funds_entry.get()) + float(self.chelcie_funds_entry.get()) - float(self.cost_entry.get())) + (aj_wage * int(self.aj_upcoming_checks_entry.get()) + chelcie_wage * int(self.chelcie_upcoming_checks_entry.get()) - float(self.upcoming_cost_entry.get()) - expenses) + (aj_wage * int(self.aj_next_checks_entry.get()) + chelcie_wage * int(self.chelcie_next_checks_entry.get()) - expenses - float(self.next_cost_entry.get()))) + aj_new_funds_following + chelcie_new_funds_following - expenses - float(self.following_cost_entry.get())
		self.following_funds_display.delete(0.0, END)
		self.following_funds_display.insert(0.0, "$%.2f" % following_funds)


root = Tk()
root.title("CAN... WE... AFFORD IT!?!")
root.geometry("600x400")
app= Application(root)
root.mainloop()