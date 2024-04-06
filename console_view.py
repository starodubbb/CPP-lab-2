class PersonConsoleView:

    def __init__(self, controller):
        self.controller = controller

    def get_user_input(self, prompt):
        return input(prompt)

    def collect_and_get_user_data(self):
        first_name = self.get_user_input("Enter First Name: ")
        last_name = self.get_user_input("Enter Last Name: ")
        return first_name, last_name

    def display_full_name(self, full_name):
        print(f"Full Name: {full_name}")

    def run(self):
        first_name, last_name = self.collect_and_get_user_data()
        self.controller.update_user_data(first_name, last_name)
