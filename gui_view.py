import tkinter as tk


class PersonGUIView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Person Information")

        self.first_name_label = tk.Label(root, text="First Name:")
        self.first_name_label.pack()

        self.first_name_entry = tk.Entry(root)
        self.first_name_entry.pack()

        self.last_name_label = tk.Label(root, text="Last Name:")
        self.last_name_label.pack()

        self.last_name_entry = tk.Entry(root)
        self.last_name_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def submit(self):
        first_name, last_name = self.collect_and_get_user_data()
        self.controller.update_user_data(first_name, last_name)

    def run(self):
        self.root.mainloop()

    def display_full_name(self, full_name):
        self.result_label.config(text=f"Full Name: {full_name}")

    def collect_and_get_user_data(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        return first_name, last_name
