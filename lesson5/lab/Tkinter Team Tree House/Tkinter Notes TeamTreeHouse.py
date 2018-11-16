#tkinter notes from TeamTreeHouse Vids

import tkinter


    
    
def funcTry():
    
    # creates a root window/app
    # Tk() for library
    root = tkinter.Tk()
    
    hi_there = tkinter.Label (
        # what does this label belong to
        root,
        text = "Hi there!",
        bg = "red",
        fg = "white"
    )
    
    # pack method that lets tkinter figure out where objects should go
    # tkinter.X for horizontal, Y for vertical, Both for both
    hi_there.pack(fill = tkinter.BOTH, expand = True)
    
    
    my_name = tkinter.Label(root, text = "My name is Anisha")
    my_name.pack()
    
    # pack is harder to figure out, like floats in CSS
    
    root.mainloop()



DEFAULT_GAP = 60 * 25


def actualAPP():
    
    class Pymodoro:
        
        def __init__(self, master):
            
            self.master = master
            self.mainframe = tkinter.Frame(self.master, bg = 'white')
            self.mainframe.pack(fill = tkinter.BOTH, expand = True)
        
            # string var to store strings
            self.timer_text = tkinter.StringVar()
            # text we display, do something when updated
            self.timer_text.trace('w', self.build_timer)
            
            self.timer_left = tkinter.IntVar()
            self.timer_left.set(DEFAULT_GAP)
            # track whether timer is running
            self.running = False
        
            self.build_grid()
            self.build_banner()
            self.build_buttons()
            self.build_timer()
            
            self.update()
            
        def build_grid(self):
            
            self.mainframe.columnconfigure(0, weight = 1)
            self.mainframe.rowconfigure(0, weight = 0)
            self.mainframe.rowconfigure(1, weight = 1)
            self.mainframe.rowconfigure(2, weight = 0)
        
        def build_banner(self):
            
            banner = tkinter.Label(
                self.mainframe,
                background = 'red',
                text = 'Pymodoro',
                fg = 'white',
                font = ('Helvetica', 24)
            )
            
            banner.grid(
                row = 0, column = 0,
                sticky = 'ew',
                # directions for where we want something to be
                # ew = east and west
                padx = 10, pady = 10
                #padding
            )
            
        def build_buttons(self):
            
            buttons_frame = tkinter.Frame(self.mainframe)
            
            buttons_frame.grid(
                row = 2, 
                column = 2, 
                sticky = 'nsew', 
                padx = 10
            )
            
            buttons_frame.columnconfigure(0, weight = 1)
            buttons_frame.columnconfigure(1, weight = 1)
            
            # creates start button
            self.start_button = tkinter.Button(
                buttons_frame,
                text = 'Start',
                command = self.start_timer
            )
            
            # creates stop button
            self.stop_button = tkinter.Button(
                buttons_frame,
                text = 'Stop',
                command = self.stop_timer
            )
            
            # assign button
            self.start_button.grid(row = 0, column = 0, sticky = 'ew')
            self.stop_button.grid(row = 0, column = 1, sticky = 'ew')
            
            self.stop_button.config(state = tkinter.DISABLED)
    
        # args because have to know how many variables are coming in    
        def build_timer(self, *args): 
           
            timer = tkinter.Label(
                self.mainframe,
                # get the variable for different texts
                text = self.timer_text.get(),
                font = ('Helvetica', 36)
            )    
        
            timer.grid(row = 1, column = 0, sticky = 'nsew')
        
        # start timer when button is clicked
        def start_timer(self):
            
            self.timer_left.set(DEFAULT_GAP)
            # track whether timer is running
            self.running = True
            # print('started')
            
            self.stop_button.config(state = tkinter.NORMAL)
            self.start_button.config(state = tkinter.DISABLED)
            
        def stop_timer(self):
            self.running = False
            # print('stopped')
            
            self.stop_button.config(state = tkinter.DISABLED)
            self.start_button.config(state = tkinter.NORMAL)
        
        def minutes_seconds(self, seconds):
            return int(seconds/60), int(seconds%60)
        
        def update(self):
            # print('updated')
            
            # decrement timer here
            time_left = self.timer_left.get()
            
            if self.running and time_left:
                
                minutes, seconds = self.minutes_seconds(time_left)
                self.timer_text.set(
                    '{:0>2}:{:0>2}'.format(minutes, seconds)
                )
                
                self.timer_left.set(time_left - 1)
           
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

actualAPP()