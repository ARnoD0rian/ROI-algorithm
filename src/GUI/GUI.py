from helper.helper import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askstring
import sys
from algorithm.algorithm import algorithm


class GUI:
    def __init__(self) -> None:
        
        self.constants = Constants()
        
        self.root = tk.Tk()
        self.root.title("алгоритм роя частиц")
        self.root.geometry('430x670')
        self.root['background'] = "gray"
        self.root.resizable(False, False)
        
        self.style_frame = ttk.Style()
        self.style_frame.configure("Style.TFrame", background = "gray")
        self.style_check_button = ttk.Style()
        self.style_check_button.configure("TCheckbutton", font=("Arial", 12), background="black", foreground = "black")
        self.style_button = ttk.Style()
        self.style_button.configure("TButton", font=("Arial", 18), background="black", foreground = "black", padding=(10,10,10,10))
        self.style_mini_label = ttk.Style()
        self.style_mini_label.configure("Mini.TLabel", font=("Arial", 12), padding = 5, foreground="black", background="gray")
        self.style_label = ttk.Style()
        self.style_label.configure("TLabel", font=("Arial", 14), padding = 5, foreground="white", background="gray")
        self.style_label_top = ttk.Style()
        self.style_label_top.configure("Top.TLabel", font=("Arial", 18), padding = 10, foreground="white", background="gray")
        
        self.main_menu = tk.Menu()
        self.main_menu.add_cascade(label="сохранить", command=self.safe_paremetres)
        self.main_menu.add_cascade(label="запустить", command=self.start_algoritm)
        self.main_menu.add_cascade(label="показать перемещение роя", command=self.show)
        self.main_menu.add_cascade(label="выход", command=sys.exit)
        
        self.input_Frame = ttk.Frame(self.root, style="Style.TFrame")
        
        self.information_input_Label = ttk.Label(self.input_Frame, text="Входные данные", style="Top.TLabel") 
        self.information_input_Label.grid(row=0, column=0, columnspan=2)
        
        self.function_Label = ttk.Label(self.input_Frame, text="функция: ", style="Mini.TLabel")
        self.function_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.function_Entry.insert('end', "4*(x-2)**4 + (x-2*y)**2")
        self.function_Label.grid(column=0, row=1)
        self.function_Entry.grid(column=1, row=1)
        
        self.ROI_SIZE_Label = ttk.Label(self.input_Frame, text="величина роя: ", style="Mini.TLabel")
        self.ROI_SIZE_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.ROI_SIZE_Entry.insert('end', "100")
        self.ROI_SIZE_Label.grid(column=0, row=2)
        self.ROI_SIZE_Entry.grid(column=1, row=2)
        
        self.ITETATION_Label = ttk.Label(self.input_Frame, text="количество итераций: ", style="Mini.TLabel")
        self.ITETATION_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.ITETATION_Entry.insert('end', "100")
        self.ITETATION_Label.grid(column=0, row=3)
        self.ITETATION_Entry.grid(column=1, row=3)
        
        self.MAX_SPEED_Label = ttk.Label(self.input_Frame, text="максимальная скорость: ", style="Mini.TLabel")
        self.MAX_SPEED_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.MAX_SPEED_Entry.insert('end', "10.0")
        self.MAX_SPEED_Label.grid(column=0, row=4)
        self.MAX_SPEED_Entry.grid(column=1, row=4)
        
        self.INERTION_Label = ttk.Label(self.input_Frame, text="коэффициент эннерции: ", style="Mini.TLabel")
        self.INERTION_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.INERTION_Entry.insert('end', "0.5")
        self.INERTION_Label.grid(column=0, row=5)
        self.INERTION_Entry.grid(column=1, row=5)
        
        self.MAX_COORDINATE_Label = ttk.Label(self.input_Frame, text="максимальная координата: ", style="Mini.TLabel")
        self.MAX_COORDINATE_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.MAX_COORDINATE_Entry.insert('end', "100.0")
        self.MAX_COORDINATE_Label.grid(column=0, row=6)
        self.MAX_COORDINATE_Entry.grid(column=1, row=6)
        
        self.MIN_COORDINATE_Label = ttk.Label(self.input_Frame, text="минимальная координата: ", style="Mini.TLabel")
        self.MIN_COORDINATE_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.MIN_COORDINATE_Entry.insert('end', "-100.0")
        self.MIN_COORDINATE_Label.grid(column=0, row=7)
        self.MIN_COORDINATE_Entry.grid(column=1, row=7)
        
        self.F_P_Label = ttk.Label(self.input_Frame, text="коэффициент глобального ускорения: ", style="Mini.TLabel")
        self.F_P_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.F_P_Entry.insert('end', "2.001")
        self.F_P_Label.grid(column=0, row=8)
        self.F_P_Entry.grid(column=1, row=8)
        
        self.F_G_Label = ttk.Label(self.input_Frame, text="коэффициент локального ускорения: ", style="Mini.TLabel")
        self.F_G_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.F_G_Entry.insert('end', "2.001")
        self.F_G_Label.grid(column=0, row=9)
        self.F_G_Entry.grid(column=1, row=9)
        
        self.K_Label = ttk.Label(self.input_Frame, text="коэффициент K: ", style="Mini.TLabel")
        self.K_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.K_Entry.insert('end', "0.9")
        self.K_Label.grid(column=0, row=10)
        self.K_Entry.grid(column=1, row=10)
        
        self.input_Frame.grid(row=0, column=0)
        
        self.table_Frame = ttk.Frame(self.root, style="Style.TFrame", padding=10)
        self.table_Frame.grid(row=2, column=0, columnspan=2)
        
        self.Scrollbar = ttk.Scrollbar(self.table_Frame)
        self.Scrollbar.grid(row=0, column=2, sticky='ns')
        
        self.Table = ttk.Treeview(self.table_Frame, yscrollcommand=self.Scrollbar.set)
        self.Table['columns'] = ('Результат', 'координата x', 'координата y')
        
        self.Table.heading('#0', text='Номер')
        self.Table.heading('Результат', text='Результат')
        self.Table.heading('координата x', text='координата x')
        self.Table.heading('координата y', text='координата у')
        self.Table.column('#0', width=50)
        self.Table.column('#1', width=110)
        self.Table.column('#2', width=105)
        self.Table.column('#3', width=105)

        self.Scrollbar.config(command=self.Table.yview)
        
        self.Table.grid(row=0, column=0, columnspan=2, sticky='nsew')
        
        self.solution_Frame = ttk.Frame(self.root, style="Style.TFrame")
        
        self.best_solution_Label = ttk.Label(self.solution_Frame, text=f"лучшее решение={self.constants.BEST_SOLUTION} при x={self.constants.BEST_COORDINATE[0]}, y={self.constants.BEST_COORDINATE[1]}", style="TLabel")
        self.best_solution_Label.grid(row=1, column=0)
        
        self.solution_Frame.grid(row=1, column=0)
        
        self.root.config(menu=self.main_menu)
    
    def start(self):
        self.root.mainloop()
    
    def start_algoritm(self):
        self.constants = algorithm(self.constants, add_in_moving=True)
        self.best_solution_Label.config(text=f"лучшее решение={round(self.constants.BEST_SOLUTION, 3)} при x={round(self.constants.BEST_COORDINATE[0], 3)}, y={round(self.constants.BEST_COORDINATE[1], 3)}") 

        images = list()
        
        for i in range(self.constants.ITERATION):
            images.append(ImageClip(f"{DIRECTORY}/location_{i}.png").set_duration(0.1))
            
        clip = concatenate_videoclips(images, method="compose")
        clip.write_videofile("ROI.mp4", fps=24)
        
    def safe_paremetres(self):
        self.constants.FUNC = Func(self.function_Entry.get())
        self.constants.ROI_SIZE = int(self.ROI_SIZE_Entry.get())
        self.constants.MAX_SPEED = float(self.MAX_SPEED_Entry.get())
        self.constants.MAX_COORDINATE = float(self.MAX_COORDINATE_Entry.get())
        self.constants.MIN_COORDINATE = float(self.MIN_COORDINATE_Entry.get())
        self.constants.INERTION = float(self.INERTION_Entry.get())
        self.constants.ITERATION = int(self.ITETATION_Entry.get())
        self.constants.F_P = float(self.F_P_Entry.get())
        self.constants.F_G = float(self.F_G_Entry.get())
        self.constants.FI = self.constants.F_P + self.constants.F_G
        self.constants.K = float(self.K_Entry.get())
        self.constants.X = 2*self.constants.K / abs(2 - self.constants.FI - (self.constants.FI**2 - 4*self.constants.FI) ** 0.5)
        self.constants.swarm = create_swarm(self.constants.MIN_COORDINATE, self.constants.MAX_COORDINATE, self.constants.MAX_SPEED, self.constants.INERTION, self.constants.F_P, self.constants.F_G, self.constants.K, self.constants.X, self.constants.ROI_SIZE)
        self.constants.moving = list()
        showinfo(title="успех", message="параметры сохранены")
    def show(self):
        N = int(askstring("количество поколений", "Введите количество поколений"))
        self.show_image(N, self.constants.moving)
    
    def show_image(self, N:int, moving):
        if N * self.constants.ROI_SIZE > len(moving):
            showerror(title="ошибка", message="вы не создали столько поколений")
            return
        
        particles = [moving[i] for i in range(len(moving) - 1, len(moving) - N * self.constants.ROI_SIZE - 1, -1)]
        
        for i in range(len(self.Table.get_children())):
            self.Table.delete(self.Table.get_children()[0])
        
        for i in range(len(particles)):
            local_solution = self.constants.FUNC.value(particles[i].local_solution)
            self.Table.insert("", "end", text=f"{i + 1}", values=(round(local_solution, 3), round(particles[i].x[0], 3), round(particles[i].x[1], 3)))
        
        x = list()
        y = list()
        for particle in particles:
            x.append(particle.x[0])
            y.append(particle.x[1])
        plt.clf()   
        plt.plot(x, y, 'go')
        plt.xlabel("x")
        plt.ylabel("Y")
        plt.show()