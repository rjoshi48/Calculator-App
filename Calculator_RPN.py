import tkinter as tk

class Calctiny(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.gotEQ = 0
        self.gotOPR = 0
        self.ans = 0
        self.num = "0"
        self.opr = ' '
        self.key = ' '
        self.memory= []
        self.values = []
        self.entry1 = tk.Entry(self, width=20, font=('Arial 24'), border=2, fg="black", bg="#abbab1")
        self.entry2 = tk.Entry(self, width=20, font=('Arial 24'), border=2, fg="black", bg="#abbab1")
        self.entry3 = tk.Entry(self, width=20, font=('Arial 24'), border=2, fg="black", bg="#abbab1")
        self.entry4 = tk.Entry(self, width=20, font=('Arial 24'), border=2, fg="black", bg="#abbab1")
        self.btxt = ['MS', 'MR', 'M', 'MC',
                    '7', '8', '9', '/',
                    '4', '5', '6', '*',
                    '1', '2', '3', '-',
                    '0', '.', '', '+',
                    'CE', 'C', '', 'Enter'
                    ]
        self.buttons = []
        self.L = [
            lambda e: self.handle_number(((e.widget).cget("text"))),
            lambda e: self.handle_operator(((e.widget).cget("text"))),
            lambda e: self.clear_entry(),
            lambda e: self.clear(),
            lambda e: self.memory_store(),
            lambda e: self.enter(),
            lambda e: self.memory_recall(((e.widget).cget("text")))
            
        ]
        self.create_widgets()

    def create_widgets(self):
        self.entry1.grid(row=0, column=0, columnspan=4)
        self.entry2.grid(row=1, column=0, columnspan=4)
        self.entry3.grid(row=2, column=0, columnspan=4)
        self.entry4.grid(row=3, column=0, columnspan=4)

        for i in range(len(self.btxt)):
            row = i // 4 + 4
            col = i % 4
            if self.btxt[i] == 'Enter':
                button = tk.Button(self, text=self.btxt[i], width=9, height=2, fg="white", bg="#FA8072", font="Segoe 12")
            else:
                button = tk.Button(self, text=self.btxt[i], width=9, height=2, fg="white", bg="#333333", font="Segoe 12")
            button.grid(row=row, column=col)
            button.bind("<Button-1>", self.L[0] if button.cget("text").isdigit() or button.cget("text") == '.' else \
                                      self.L[1] if button.cget("text") not in ('CE', 'C', 'MS', 'MR', 'M', 'MC','Enter') else \
                                      self.L[2] if button.cget("text") == 'CE' else \
                                      self.L[3] if button.cget("text") == 'C' else \
                                      self.L[4] if button.cget("text") == 'MS' else \
                                      self.L[5] if button.cget("text") == 'Enter' else \
                                      self.L[6])
            self.buttons.append(button)

    def handle_number(self, text):
        if self.ans != 0:
            self.values.append(self.ans)
            self.num ="0"
            self.ans = 0
            self.display()  
        
        self.key = text
        if self.key == '.' and '.' in self.num:
            return
        if self.num == '0' and self.key != '.':
            self.num = self.key
        else:
            self.num += self.key
        self.entry4.delete(0, tk.END)
        self.entry4.insert(tk.END, self.num)
    
    def enter(self):
        self.values.append(self.num)
        self.num = '0'
        self.entry4.delete(0, tk.END)
        self.entry4.insert(tk.END, self.num)
        self.display()


    def handle_operator(self, text):
        if self.ans != 0:
            self.ans = 0
        self.opr = text     

        #self.values.append(self.num)
        self.ans = str(eval(self.values[-1] + self.opr + self.num))
        self.num = self.ans
        self.values.pop()
        #print(self.values.pop())

        self.entry4.delete(0, tk.END)
        self.entry4.insert(tk.END, self.ans)

        self.display()
        

    def display(self):
        if len(self.values) >= 3:
            self.entry1.delete(0, tk.END)
            self.entry1.insert(tk.END, self.values[-3])
            self.entry2.delete(0, tk.END)
            self.entry2.insert(tk.END, self.values[-2])
            self.entry3.delete(0, tk.END)
            self.entry3.insert(tk.END, self.values[-1])
        elif len(self.values) == 2:
            self.entry1.delete(0, tk.END)
            self.entry1.insert(tk.END, "")
            self.entry2.delete(0, tk.END)
            self.entry2.insert(tk.END, self.values[-2])
            self.entry3.delete(0, tk.END)
            self.entry3.insert(tk.END, self.values[-1])
        elif len(self.values) == 1:
            self.entry1.delete(0, tk.END)
            self.entry1.insert(tk.END, "")
            self.entry2.delete(0, tk.END)
            self.entry2.insert(tk.END, "")
            self.entry3.delete(0, tk.END)
            self.entry3.insert(tk.END, self.values[-1])
        else:
            self.entry1.delete(0, tk.END)
            self.entry1.insert(tk.END, "")
            self.entry2.delete(0, tk.END)
            self.entry2.insert(tk.END, "")
            self.entry3.delete(0, tk.END)
            self.entry3.insert(tk.END, "")

    def clear_entry(self):
        self.entry4.delete(0, tk.END)
        self.num = "0"

    def clear(self):
        self.entry4.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry1.delete(0, tk.END)
        self.num = "0"
        self.ans = 0
        self.opr = ' '
        self.values=[]

    def memory_store(self):
        if self.entry4.get():
            self.memory.append(float(self.entry4.get()))
        #print(self.memory)

    def memory_recall(self, text):
        if text == 'MR':
            if self.memory:
                self.entry4.delete(0, tk.END)
                self.entry4.insert(tk.END, str(self.memory[-1]))
            else:
                self.entry4.delete(0, tk.END)

        elif text == 'M':
            self.entry4.delete(0, tk.END)
            self.entry4.insert(tk.END, str(self.memory))

        elif text == 'MC':
            self.entry4.delete(0, tk.END)
            self.memory =[]
        
root = tk.Tk()
root.title("RPN Calculator")
root.geometry("366x470")
root.resizable(0, 0)
root.config(bg="#333333")
app = Calctiny(master=root)
app.grid()
root.mainloop()
