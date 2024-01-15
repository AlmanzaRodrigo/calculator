import tkinter as tk
from tkinter import font
from pathlib import Path


class Calculator():
    def __init__(self) -> None:
        self.current_input = float(0)
        self.memory = float(0)
        self.operation = None
        self.result = None

    def create_window(self):
        """creates a tkinter window"""
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("290x390")
        self.root.resizable(0,0)
        self.root.iconbitmap(Path.cwd() / "calculator.ico")
    
    def create_win_elements(self):
        """Creates GUI elements"""
        self.display_font = font.Font(weight=font.BOLD, size=17)

        self.frames = {}
        self.frames["display_frame"] = tk.Frame(self.root, bg="#A1B5C5", padx=21, pady=20)
        self.frames["buttons_frame"] = tk.Frame(self.root, bg="#D6DEE0", padx=20, pady=20)

        self.display = {}
        self.display["display"] = tk.Label(self.frames["display_frame"], bg="#CDD6B6", width=400, height=50)
        self.display["number_display"] = tk.Label(self.display["display"], text="0", bg="#CDD6B6", fg="#4B6E84", font=self.display_font, anchor="se", width=17)
        self.display["memory_display"] = tk.Label(self.display["display"], text="M =", bg="#CDD6B6", fg="#4B6E84")

        self.buttons = {}
        self.buttons["button_mc"] = tk.Button(self.frames["buttons_frame"], text="MC", bg="#4B6E84", fg="white", width=6, height=2, command=self.btt_mc)
        self.buttons["button_madd"] = tk.Button(self.frames["buttons_frame"], text="M+", bg="#4B6E84", fg="white", width=6, height=2, command=self.btt_mem_add)
        self.buttons["button_div"] = tk.Button(self.frames["buttons_frame"], text="%", bg="#4B6E84", fg="white", width=6, height=2, command=self.btt_div)
        self.buttons["button_mult"] = tk.Button(self.frames["buttons_frame"], text="X", bg="#4B6E84", fg="white", width=6, height=2, command=self.btt_mult)

        self.buttons["button7"] = tk.Button(self.frames["buttons_frame"], text="7", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_7)
        self.buttons["button8"] = tk.Button(self.frames["buttons_frame"], text="8", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_8)
        self.buttons["button9"] = tk.Button(self.frames["buttons_frame"], text="9", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_9)
        self.buttons["button_sub"] = tk.Button(self.frames["buttons_frame"], text="-", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_sub)

        self.buttons["button4"] = tk.Button(self.frames["buttons_frame"], text="4", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_4)
        self.buttons["button5"] = tk.Button(self.frames["buttons_frame"], text="5", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_5)
        self.buttons["button6"] = tk.Button(self.frames["buttons_frame"], text="6", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_6)
        self.buttons["button_add"] = tk.Button(self.frames["buttons_frame"], text="+", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_add)

        self.buttons["button1"] = tk.Button(self.frames["buttons_frame"], text="1", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_1)
        self.buttons["button2"] = tk.Button(self.frames["buttons_frame"], text="2", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_2)
        self.buttons["button3"] = tk.Button(self.frames["buttons_frame"], text="3", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_3)
        self.buttons["button_clear"] = tk.Button(self.frames["buttons_frame"], text="CL", bg="#D17831", fg="white", width=6, height=2, command=self.btt_clear)

        self.buttons["button0"] = tk.Button(self.frames["buttons_frame"], text="0", bg="#7592A5", fg="white", width=15, height=2, command=self.btt_0)
        self.buttons["button_dot"] = tk.Button(self.frames["buttons_frame"], text=".", bg="#7592A5", fg="white", width=6, height=2, command=self.btt_dot)
        self.buttons["button_equal"] = tk.Button(self.frames["buttons_frame"], text="=", bg="#D17831", fg="white", width=6, height=2, command=self.btt_equal)

    def draw_elements(self):
        """Draw GUI elements in tkinter window"""
        self.frames["display_frame"].pack()
        self.frames["buttons_frame"].pack()
        self.display["display"].pack()
        self.display["memory_display"].grid(row=0, sticky="nw")
        self.display["number_display"].grid(row=1, sticky="se")

        self.buttons["button_mc"].grid(row=0, column=0, padx=5, pady=5)
        self.buttons["button_madd"].grid(row=0, column=1, padx=5, pady=5)
        self.buttons["button_div"].grid(row=0, column=2, padx=5, pady=5)
        self.buttons["button_mult"].grid(row=0, column=3, padx=5, pady=5)

        self.buttons["button7"].grid(row=1, column=0, padx=5, pady=5)
        self.buttons["button8"].grid(row=1, column=1, padx=5, pady=5)
        self.buttons["button9"].grid(row=1, column=2, padx=5, pady=5)
        self.buttons["button_sub"].grid(row=1, column=3, padx=5, pady=5)

        self.buttons["button4"].grid(row=2, column=0, padx=5, pady=5)
        self.buttons["button5"].grid(row=2, column=1, padx=5, pady=5)
        self.buttons["button6"].grid(row=2, column=2, padx=5, pady=5)
        self.buttons["button_add"].grid(row=2, column=3, padx=5, pady=5)

        self.buttons["button1"].grid(row=3, column=0, padx=5, pady=5)
        self.buttons["button2"].grid(row=3, column=1, padx=5, pady=5)
        self.buttons["button3"].grid(row=3, column=2, padx=5, pady=5)
        self.buttons["button_clear"].grid(row=3, column=3, padx=5, pady=5)

        self.buttons["button0"].grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        self.buttons["button_dot"].grid(row=4, column=2, padx=5, pady=5)
        self.buttons["button_equal"].grid(row=4, column=3, padx=5, pady=5)

    # number buttons methods
    def btt_1(self):
        self.num_btt_func("1")

    def btt_2(self):
        self.num_btt_func("2")

    def btt_3(self):
        self.num_btt_func("3")

    def btt_4(self):
        self.num_btt_func("4")

    def btt_5(self):
        self.num_btt_func("5")

    def btt_6(self):
        self.num_btt_func("6")

    def btt_7(self):
        self.num_btt_func("7")

    def btt_8(self):
        self.num_btt_func("8")

    def btt_9(self):
        self.num_btt_func("9")
    
    def btt_0(self):
        self.num_btt_func("0")

    def btt_dot(self):
        if "." not in self.get_display():
            self.set_display(self.get_display() + ".")

    def num_btt_func(self, number):
        """control the functionality of all numbers 
        buttons"""
        if self.is_first_input():
            self.set_display(number)
            self.current_input = float(number)
        else:
            self.set_display(self.get_display() + number)
            self.current_input = float(self.get_display())

    # arithmetic buttons methods
    def btt_add(self):
        self.arith_btt_func(lambda x, y: x + y)
        #self.arith_btt_func("+")
    
    def btt_sub(self):
        self.arith_btt_func(lambda x, y: x - y)
        #self.arith_btt_func("-")

    def btt_mult(self):
        self.arith_btt_func(lambda x, y: x * y)
        #self.arith_btt_func("*")

    def btt_div(self):
        self.arith_btt_func(lambda x, y: x / y)
        #self.arith_btt_func("/")
    
    def arith_btt_func(self, operation):
        if self.result == None:
            self.result = self.current_input
            self.operation = operation
            self.set_display("")
        elif self.operation != None:
            self.result = self.operation(self.result, self.current_input)
            self.current_input = float(0)
            self.operation = operation
            self.set_display("")
        else:
            self.operation = operation
            self.set_display("")

    def btt_equal(self):
        if self.operation != None:
            self.result = self.operation(self.result, self.current_input)
            self.current_input = float(0)
            self.operation = None
            self.set_display(str(self.result))

    # memory buttons methods
    def btt_mc(self):
        self.set_display("", "memory_display")

    def btt_mem_add(self):
        if self.result != None:
            self.memory += self.result
            self.set_display(str(self.memory), "memory_display")
        else:
            self.memory += self.current_input
            self.set_display(str(self.memory), "memory_display")

    def btt_clear(self):
        self.__init__()
        self.set_display("0")
        self.set_display("", "memory_display")

    # control methods
    def is_display_overflow(self, one_display):
        if one_display == "number_display":
            return len(self.get_display(one_display)) > 17
        elif one_display == "memory_display":
            return len(self.get_display(one_display)) > 10
    
    def is_first_input(self):
        return self.get_display() == "0"

    
    # getters and setters
    def set_display(self, value, display="number_display"):
        if display == "memory_display":
            if value == "":
                self.display[display].config(text="M = " + value)
            elif self.is_display_overflow("memory_display"):
                pass
            else:
                self.display[display].config(text="M = " + value)
        
        elif display == "number_display":
            if self.is_display_overflow("number_display"):
                pass
            else:
                self.display[display].config(text = value)
    
    def get_display(self, display="number_display"):
        return self.display[display]["text"]
    

    def run(self):
        self.create_window()
        self.create_win_elements()
        self.draw_elements()
        self.root.mainloop()


if __name__ == "__main__":
    app = Calculator()
    app.run()