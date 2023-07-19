import tkinter as tk

class Calctiny(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.ans = 0
        self.num = "0"
        self.opr = ' '
        self.key = ' '
        self.memory = []
        self.prev = ' '
        self.values = []
        self.operators = []
        self.precedence = {'+': 1, '-': 1, 'X': 2, '/': 2}
        self.ctxt = tk.Entry(self, width=20, font=('Arial 24'), border=2, fg="black", bg="#abbab1")
        self.btxt = ['MS', 'MR', 'M', 'MC',
                      '7', '8', '9', '/',
                     '4', '5', '6', 'X',
                     '1', '2', '3', '-',
                     '0', '.', '(', '+',
                     'CE', 'C', ')', '='
                     ]
        self.buttons = []
        self.L = [
            lambda e: self.handle_number(((e.widget).cget("text"))),
            lambda e: self.handle_operator(((e.widget).cget("text"))),
            lambda e: self.clear_entry(),
            lambda e: self.clear(),
            lambda e: self.memory_store(),
            lambda e: self.memory_recall(((e.widget).cget("text"))),
            lambda e: self.handle_parentheses(((e.widget).cget("text")))
        ]
        self.create_widgets()
        
        

    def create_widgets(self):
        self.ctxt.grid(row=0, column=0, columnspan=4)

        for i in range(len(self.btxt)):
            row = i // 4 + 1
            col = i % 4
            if self.btxt[i] == '=':
                button = tk.Button(self, text=self.btxt[i], width=9, height=2, fg="white", bg="#FA8072", font="Segoe 12")
            else:
                button = tk.Button(self, text=self.btxt[i], width=9, height=2, fg="white", bg="#333333", font="Segoe 12")
            button.grid(row=row, column=col)
            button.bind("<Button-1>", self.L[0] if button.cget("text").isdigit() or button.cget("text") == '.' else \
                                      self.L[1] if button.cget("text") not in ('CE', 'C', 'MS', 'MR','M','MC', '(', ')') else \
                                      self.L[2] if button.cget("text") == 'CE' else \
                                      self.L[3] if button.cget("text") == 'C' else \
                                      self.L[4] if button.cget("text") == 'MS' else \
                                      self.L[5] if button.cget("text") == 'MR' or button.cget("text") == 'M' or button.cget("text") == 'MC' else \
                                      self.L[6])
            self.buttons.append(button)

    def handle_number(self, text):
        self.key = text
        #self.num = '0'
        if self.key == '.' and '.' in self.num:
            return
        if self.num == '0' and self.key != '.':
            self.num = self.key
        else:
            self.num += self.key
        if self.prev == ')':
            self.prev = ' '
        self.ctxt.delete(0, tk.END)
        self.ctxt.insert(tk.END, self.num)

    def handle_operator(self, text):
        if self.num != '0':
            self.values.append(self.num)
            self.num ='0'
        self.key = text

        if len(self.operators) >= 1 and self.operators[-1] != '(' and self.prev != ')':
            if len(self.operators) >=2:
                self.num='0'
                while self.operators and self.precedence.get(self.operators[-1]) >= self.precedence.get(self.operators[-2]):
                    self.calculate()
            else:
                self.num='0'
                self.calculate()
        elif self.key == '=':
            if len(self.operators) >= 1:
                self.calculate()

            else:
                self.num = self.ans
                self.operators = []
                self.num='0'

        if self.key != '=':
            self.operators.append(self.key)
        self.num = '0'

        
    def handle_parentheses(self, text):
        if text == '(':
            self.operators.append(text)
            self.num = '0'
        elif text == ')':
            self.values.append(self.num)
            self.num = '0'
            self.prev = ')'
            while self.operators[-1] != '(':
                self.calculate()
            self.operators.pop()

    def calculate(self):
        self.num = '0'
        while len(self.operators) >= 1 and len(self.values) >= 2 and self.operators[-1] != '(':
            self.opr = self.operators.pop()
            x = float(self.values.pop())
            y = float(self.values.pop())
            
            if self.opr == '+':
                self.ans = y + x
            elif self.opr == '-':
                self.ans = y - x
            elif self.opr == 'X':
                self.ans = y * x
            elif self.opr == '/':
                self.ans = y / x
            
            self.values.append(str(self.ans))
            
       
        self.ctxt.delete(0, tk.END)
        self.ctxt.insert(tk.END, str(self.ans))

    def clear_entry(self):
        self.ctxt.delete(0, tk.END)
        self.num = '0'

    def clear(self):
        self.ctxt.delete(0, tk.END)
        self.ans = 0
        self.num = '0'
        self.opr = ' '
        self.key = ' '
        self.prev = ' '
        self.values = []
        self.operators = []

    def memory_store(self):
        if self.ctxt.get():
            self.memory.append(float(self.ctxt.get()))
        #print(self.memory)

    def memory_recall(self, text):
        if text == 'MR':
            if self.memory:
                self.ctxt.delete(0, tk.END)
                self.ctxt.insert(tk.END, str(self.memory[-1]))
            else:
                self.ctxt.delete(0, tk.END)

        elif text == 'M':
            self.ctxt.delete(0, tk.END)
            self.ctxt.insert(tk.END, str(self.memory))

        elif text == 'MC':
            self.ctxt.delete(0, tk.END)
            self.memory =[]


root = tk.Tk()
root.title("Infix Calculator")
root.geometry("366x346")
root.resizable(0, 0)
root.config(bg="#333333")
app = Calctiny(master=root)
app.grid()
root.mainloop()