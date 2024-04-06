import tkinter as tk
from model import PersonModel
from gui_view import PersonGUIView
from console_view import PersonConsoleView
from controller import PersonController


def main():
    print("Choose the mode:")
    print("1. GUI mode (Tkinter)")
    print("2. Console mode (CLI)")

    choice = input("Enter your choice (1 or 2): ")

    model = PersonModel()

    if choice == "1":
        root = tk.Tk()
        root.geometry("400x170")
        controller = PersonController(model, None)
        view = PersonGUIView(root, controller)
        controller.set_view(view)
        controller.execute()
    elif choice == "2":
        controller = PersonController(model, None)
        view = PersonConsoleView(controller)
        controller.set_view(view)
        controller.execute()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
