import tkinter as tk

class Window():
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("PYtris")

		self.label = tk.Label(self.root, text="This is our first GUI!")
		self.label.pack()

		self.text = tk.Text(self.root, cnf = "jopa\njopa\njopa")

		self.greet_button = tk.Button(self.root, text = "Greet", command = self.greet)
		self.greet_button.pack()

		self.close_button = tk.Button(self.root, text = "Close", command = self.root.quit)
		self.close_button.pack()

	def greet(self):
		self.label.configure(text="Hello, World!")

window = Window()
window.root.mainloop()
