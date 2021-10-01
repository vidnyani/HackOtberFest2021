import tkinter as tk

def leap(year):
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                return True
            else:  
                return False
        else:  
            return True
    else:  
        return False

def check_days(n, leap):
    if(leap):
        if(n == '01' or n == '03' or n == '05' or n == '07' or n == '08' or n == '10' or n == '12'):
            return (31)
        elif(n == '02'):
            return(29)
        else:
            return(30)
    if(leap == False):
        if(n == '01' or n == '03' or n == '05' or n == '07' or n == '08' or n == '10' or n == '12'):
            return (31)
        elif(n == '02'):
            return(28)
        else:
            return(30)


def check (i):
    if(len(str(i))==1):
        i = "0"+str(i)
        return (i)
    else:
        return(i)

def generate():
    loc = str(e3.get())
    n1 = int(e1.get())
    n2 = int(e2.get())
    if(not loc):
        tk.Label(master,text = "Check the input").grid(row = 5, column = 1)
    else:
        loc = loc.replace('\\', '/')
        if(loc.endswith('/')):
            f = open(loc+"date-list.txt", "w")
        else:
            f = open(loc+"/date-list.txt", "w")
        while(n1<=n2):
            val = leap(n1)
            for i in range(0,12):
                i = check(i+1)
                days = check_days(i, val)
                for j in range(0,days):
                    j = check(j+1)
                    f.write(str(j)+e4.get()+str(i)+e4.get()+str(n1)+"\n")
            n1+=1
                    
        tk.Label(master,text = "Success").grid(row = 5, column = 3)

master = tk.Tk()
master.geometry("400x200")
master.title("Dates generator")
tk.Label(master, 
         text="Starting year : ").grid(row=0, column = 2)
tk.Label(master, 
         text="Ending year : ").grid(row=1, column = 2)
tk.Label(master, 
         text="Location : ").grid(row=2, column = 2)
tk.Label(master, 
         text="Seperator : ").grid(row=3, column = 2)
tk.Label(master, 
         text="Leave the seperator blank to ").grid(row=4, column = 2)
tk.Label(master, 
         text="get the result without any space").grid(row=4, column = 3)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=3)
e2.grid(row=1, column=3)
e3.grid(row=2, column=3)
e4.grid(row=3, column=3)

tk.Button(master, 
          text='Generate', 
          command=generate).grid(row=5, 
                                    column=3, 
                                    sticky=tk.W, 
                                    pady=4)

tk.mainloop()