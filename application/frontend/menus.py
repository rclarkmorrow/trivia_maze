from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class menus():

    def __init__(self):

        # Create a window
        root = Tk()
        root.geometry("1000x1000")
        root.title('Trivia Maze')

        # Create a menu configuration
        my_menu = Menu(root)
        root.config(menu=my_menu)

        # Create a 'File' menu buttom
        file_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label='File', menu=file_menu)

        # Create a 'Save Game' button
        file_menu.add_command(label='Save Game', command=self.save_game)
        file_menu.add_separator()

        # Create a 'Load Game' button
        file_menu.add_command(label='Load Game', command=self.load_game)
        file_menu.add_separator()

        # Create a 'Exit' button
        file_menu.add_command(label='Exit', command=root.quit)
        file_menu.add_separator()

        # Create a 'Help' button
        help_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label='Help', menu=help_menu)

        # Create a 'About' button
        help_menu.add_command(label='About', command=self.about_us)
        help_menu.add_separator()

        # Create a 'Game Instructions' button
        help_menu.add_command(label='Game Instructions', command=self.game_instructions)
        help_menu.add_separator()

        # Close the loop
        root.mainloop()

    def save_game(self):
        """
        The method is to save the game
        When the save game button is pressed this code needs to be executed
        """
        pass

    def load_game(self):
        """
        This method is used to load the game.

        """
        filedialog.askopenfilename(initialdir="./files", title='Select A File',
                                                   filetypes=[("All files", "*.*")])

        #my_label = Label(root, text=root.filename).pack()

    def about_us(self):
        """
        This methods displays the 'about us' content
        """
        messagebox.showinfo('About Us', 'This is a Trivia maze game')

    def game_instructions(self):
        """
        This method displays the game instructions
        """
        messagebox.showinfo('Instructions', 'Step 1: Read the Trivia Questions\n'
                                            'Step 2: Select and Submit the answer\n'
                                            'Step 3: Use the arrows to traverse\n'
                                            'Step 4: Move from entrance to exit')

if __name__ == "__main__":
    name = "XYZ"
    menus()
