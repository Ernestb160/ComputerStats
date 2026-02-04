import tkinter as tk
import psutil

class SystemApp:
    def __init__(self, root):
        self.root = root

        self.root.overrideredirect(True)  # remove window decorations
        self.root.attributes("-topmost", True)  # keep window on top of games..
        self.root.attributes("-alpha", 0.7)  # see through the window
        self.root.title("ComputerStats") # you get this part I'm sure this comment is irrelivant.

        #some more mathy stuff

        width = 300
        height = 150
        x = self.root.winfo_screenwidth() - width
        y = 0 
        self.root.geometry(f"{width}x{height}+{x}+{y}") #calculates the edge of the specific screen running the program

        #time for some s-s-style

        self.root.configure(bg="#1e1e1e")  # dark background color
        self.label = tk.Label(root, text="CPU Usage: 0%", font=("Helvetica", 16), fg="#ff00dd", bg="#1e1e1e")
        self.label.pack(expand=True)

        #ez part frfr
        self.update_cpu()
        self.update_ram()


    """
    def update_stats(self):
        cpu_usage = psutil.cpu_percent()
        #cpu usage
        self.label.config(text=f"CPU: {cpu_usage}%")

        #ram one
        memory = psutil.virtual_memory()
        ram_usage = memory.percent
        self.label.config(text=f"CPU: {cpu_usage}%\nRAM: {ram_usage}%")
        
        # upd super duper fast!! 
        self.root.after(100, self.update_stats)
    """ 
    ## This IS a cool idea, but the CPU update speed is too fast, making the app look super super fast for the cpu and normal for the ram, due to the cpu fluxuating so
    ##fast. I will keep this code here for future reference though. It's kinda my own version of git at this point.. Instead we will do a slower cpu update tick, but
    ## keep the ram update tick fast.

    def update_cpu(self):
        cpu_usage = psutil.cpu_percent()
        self.label.config(text=f"CPU Usage: {cpu_usage}%")
        self.root.after(1000, self.update_cpu)  # Update every second. Delayed more than ram to reduce fluxuation effect.
    
    def update_ram(self):
        memory = psutil.virtual_memory()
        ram_usage = memory.percent
        self.label.config(text=f"CPU Usage: {psutil.cpu_percent()}%\nRAM Usage: {ram_usage}%")
        self.root.after(200, self.update_ram)  # Update every 200 milliseconds, ram doesn't fluxuate as fast as cpu.

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemApp(root)
    root.mainloop()
