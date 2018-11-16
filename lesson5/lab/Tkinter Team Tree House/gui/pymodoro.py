import tkinter
# for alert window
from tkinter import messagebox

DEFAULT_GAP = 60 * 25
DEFAULT_GAP = 5


class Pymodoro:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)
        
        # string var to store strings
        self.timer_text = tkinter.StringVar()
        # text we display, do something when updated
        self.timer_text.trace('w', self.build_timer)
        self.time_left = tkinter.IntVar()
        self.time_left.set(DEFAULT_GAP)
        # when update changes, alert should check if it should fire messages
        self.time_left.trace('w', self.alert)
        # track whether timer is running
        self.running = False

        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()

        self.update()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            background='red',
            text='Pymodoro',
            fg='white',
            font=('Helvetica', 24)
        )
        banner.grid(
            row=0, column=0,
            # directions for where we want something to be
            # ew = east and west
            sticky='ew',
            # padding
            padx=10, pady=10
        )

    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        # creates start button
        self.start_button = tkinter.Button(
            buttons_frame,
            text='Start',
            command=self.start_timer
        )
        
        # creates stop button
        self.stop_button = tkinter.Button(
            buttons_frame,
            text='Stop',
            command=self.stop_timer
        )
        
        # assign button
        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')
        self.stop_button.config(state=tkinter.DISABLED)

    # args because have to know how many variables are coming in  
    def build_timer(self, *args):
        timer = tkinter.Label(
            self.mainframe,
            # get the variable for different texts
            text=self.timer_text.get(),
            font=('Helvetica', 36)
        )
        timer.grid(row=1, column=0, sticky='nsew')
        
    # start timer when button is clicked
    def start_timer(self):
        self.time_left.set(DEFAULT_GAP)
        # track whether timer is running
        self.running = True
        self.stop_button.config(state=tkinter.NORMAL)
        self.start_button.config(state=tkinter.DISABLED)
        # print('started')

    def stop_timer(self):
        self.running = False
        self.stop_button.config(state=tkinter.DISABLED)
        self.start_button.config(state=tkinter.NORMAL)
        # print('stopped')
    
    # it will get triggered, so need args
    def alert(self, *args):
        if not self.time_left.get():
            messagebox.showinfo('Timer done!', 'Your timer is done!')

    def minutes_seconds(self, seconds):
        return int(seconds/60), int(seconds%60)

    def update(self):
        # print('updated')
        
        # decrement timer here
        time_left = self.time_left.get()

        if self.running and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes, seconds)
            )
            self.time_left.set(time_left-1)
        else:
            minutes, seconds = self.minutes_seconds(DEFAULT_GAP)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes, seconds)
            )
            self.stop_timer()
            
        # called every second
        # 1000 = milliseconds
        self.master.after(1000, self.update)

if __name__ == '__main__':
    root = tkinter.Tk()
    Pymodoro(root)
    root.mainloop()