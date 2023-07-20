# Calculator-App
Calculator application developed using Python (Tkinter library)

- ### Calculator_Infix.py: 
    Calculator, which obeys the order of operations given when multiplication and division take precedence over addition and subtraction.  The calculator will be interactive, showing intermediate results along the way.  As a convenience to the user, bracketing keys  '(' and ')' are provided, so that the same calculation would be entered as { '1' '+' '(' '5' '-' '2' ')' 'x' '7' '=' } would first show a '1', then a '5', then a '2', then a '3', then a '7', and finally, a '22'.

- ### Calculator_RPN.py:
    Calculator, which operates in 'RPN' mode.   It has the same numbers 0-9, and the function buttons '+','-','x', '/',  but instead of '=' it has an 'enter' key.  The mode of entry for the following calculation would be {'1' 'enter' '5' 'enter' '2' '-''+' '7' 'x'  }, showing as outputs, '1', '5', '2', '3', '4' '7' '28'.

- ### Additional Usecases:
    - Accept decimal point '.' to handle both int and float inputs. 
    - A 'clear entry'key 'CE' and 'clear' key 'CE/C'.  
    - The memory store'MS' and memory recall keys 'M' and 'MR' and memory clear 'MC'.

- ## How to execute this code?
    python < pythonfilename >

    ![Infix Calculator GUI](/images/Infix.jpg)
    ![RPN Calculator GUI](/images//RPN.jpg)


