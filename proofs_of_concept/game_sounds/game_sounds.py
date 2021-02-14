"""
    This class requires the installation of the module 'playsound'
    which can be installed with the command:
    `python3 -m pip install playsound`

    Additional dependencies 'PyObjC' and 'PyObjC-core' may be required
    on MacOs and can be installed with the following command:
    `python3 -m pip install PyObjC PyObjC-core`

    NOTE: it is highly recommended that you install all dependencies
    in a virtual Python environment.
"""

import tkinter as tk
from tkinter import ttk
from playsound import playsound

class GameSounds:
    """
      Main class to test sounds on event (button click) in Tkinter
    """
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x400')
        self.root.title('Sound Buttons')
        self.success_button = ttk.Button(
            self.root,
            text='Success (YAY!)',
            # Note: if you 'command=function()' the command runs on execution
            # because Tkinter assigns the results fo the function to command.
            # so to execute on click it's either 'command=function' for no args
            # or 'command=lambda: function('arg') with args.
            command=lambda: GameSounds.play_sound('success')
        )
        self.success_button.pack(
            ipadx=10,
            ipady=10,
            expand=True
        )
        self.failure_button = ttk.Button(
            self.root,
            text='Failure =( =( !!',
            command=lambda: GameSounds.play_sound('failure')
        )
        self.failure_button.pack(
            ipadx=10,
            ipady=10,
            expand=True
        )

    @staticmethod
    def play_sound(sound):
        if sound == 'success':
            print('I am clicked success!!')
            playsound('success.wav')

        elif sound == 'failure':
            print('I am clicked failure!!')
            playsound('failure.mp3')


if __name__ == '__main__':
    root = tk.Tk()
    test_gui = GameSounds(root)
    root.mainloop()