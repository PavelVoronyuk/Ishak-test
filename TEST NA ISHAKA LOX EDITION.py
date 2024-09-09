import tkinter as tk 
from tkinter import messagebox 


class Ishak:
    Q_AND_A = { 
        "Тест на ишака, введите цифры 1 или 2 :": [
            "Ты ишак!!! Иди лечись", "Ты не ишак, ай малядець!", "Ты шо мудозвон? Введи 1 или 2!"
        ], 
        "Вопрос 2! Есть ли у Ишака рога? 1-да 2-нет :": [
            "Правильно, ай малядець!", "Ты шо дебилоид? У ишака есть рога!!!!!!!!", "Та ты шо дебилоид???? Выбери 1 или 2!!!!"
        ], 
        "Вопрос 3! Кто сильнее? : Ишак или баран?   1 - ишак 2 - баран :": [
            "Ай какой малядець!! Настоящий поклонник ишака!", "Ишак сила , баран могила", "МАТЬ ЕБАЛ. ВЫБЕРИ 1 ИЛИ 2 НЕУЖЕЛИ ТАК СЛОЖНО?"
        ], 
        "Почему ишак есть ишак?  1-потому что   2-хз :": [
            "Правильно! Потому что так надо!", "Дегроид тупой!", "Тебе мозги вправить????? 1 ИЛИ 2 ЗАДАНИЕ ДЛЯ 1 IQ"
        ], 
        "Кто отчим?  1-Константин  2-Малыш :": [
            "Не правильно! Константин не отчим! Он раб!", "Конечно малыш, этот козёл всех собак в округе оприходовал", "Ливни бездарность, мудозвонище ебанное!"
        ], 
        "Кто надристал??  1-отчим  2-ишак :": [
            "Конечно отчим!", "Как ты мог такое подумать?! Нелюдь! Скот!", "Иди убейся х69"
        ]
    }


    def __init__(self): 
        self.count_question = 0 

        self.main_window = tk.Tk() 

        self.main_window.title("Ishak test GUI")
        self.main_window.geometry("780x450")
        self.main_window["bg"] = "#708090"

        self.__crete_frame()
        self.__setting_top_frame()
        self.__settings_middle_frame()
        self.__setting_bottom_frame()

        self.main_window.mainloop() 


    def __crete_frame(self): 
        self.top_frame = tk.Frame(self.main_window, bg="#708090") 
        self.middle_frame = tk.Frame(self.main_window, bg="#708090")
        self.botton_frame = tk.Frame(self.main_window, bg="#708090") 

        for item in [self.top_frame, self.middle_frame, self.botton_frame]: 
            item.pack()


    def __setting_top_frame(self): 
        self.str_var = tk.StringVar()
        self.str_var.set(list(self.Q_AND_A.items())[self.count_question][0])

        self.label_name = tk.Label(
            self.top_frame, 
            text="Тест на ишака", 
            bg="#708090", 
            fg="brown", 
            font=("Courier New", 45, "bold")
        )
        
        self.label_question = tk.Label(
            self.top_frame, 
            textvariable=self.str_var, 
            bg="#708090", 
            fg="#7FFFD4", 
            font=("Courier New", 15, "bold")
        )

        self.label_name.pack(pady=(10, 15))
        self.label_question.pack(pady=(20, 50))


    def __settings_middle_frame(self): 
        self.radio_var = tk.IntVar()  

        self.rb1 = tk.Radiobutton(
            self.middle_frame, 
            variable=self.radio_var, 
            value=1, 
            bg="#708090", 
            activebackground="#708090",
            fg="#7FFFD4", 
            activeforeground="#7FFFD4", 
            font=("Courier New", 15, "bold")
        )
        self.rb2 = tk.Radiobutton(
            self.middle_frame, 
            variable=self.radio_var, 
            value=2, 
            bg="#708090", 
            activebackground="#708090",
            fg="#7FFFD4", 
            activeforeground="#7FFFD4", 
            font=("Courier New", 15, "bold")
        )
        self.rb3 = tk.Radiobutton(
            self.middle_frame, 
            variable=self.radio_var,
            value=3, 
            bg="#708090", 
            activebackground="#708090",
            fg="#7FFFD4", 
            activeforeground="#7FFFD4", 
            font=("Courier New", 15, "bold")
        )

        for item, option in zip([self.rb1, self.rb2, self.rb3], [1, 2, 69]):
            item["text"] = option

        for item in [self.rb1, self.rb2, self.rb3]: 
            item.pack()

    def __setting_bottom_frame(self): 
        self.button_go_left = tk.Button(
            self.middle_frame, 
            bg="blue", 
            text="<",
            relief="solid",
            fg="white",
            activebackground="black", 
            activeforeground="white", 
            command=self.go_left
        )

        self.button_go_right = tk.Button(
            self.middle_frame, 
            bg="blue", 
            text=">",
            relief="solid",
            fg="white",
            activebackground="black", 
            activeforeground="white", 
            command=self.go_right
        )

        self.button_check = tk.Button(
            self.middle_frame, 
            bg="brown", 
            text="Обосраться!",
            relief="solid",
            fg="white",
            activebackground="black", 
            activeforeground="white", 
            command=self.check_button
        )

        for item in [self.button_go_left, self.button_check, self.button_go_right]: 
            item.pack(side="left", padx=10, ipady=10, ipadx=10, pady=50)


    def go_right(self):
        if self.count_question == len(self.Q_AND_A) - 1: 
            self.count_question = 0

        self.count_question += 1 
        self.str_var.set(list(self.Q_AND_A.items())[self.count_question][0])

    def go_left(self): 
        if self.count_question == 0: 
            self.count_question = len(self.Q_AND_A)
        
        self.count_question -= 1 
        self.str_var.set(list(self.Q_AND_A.items())[self.count_question][0])

    def check_button(self): 
        self.answer = self.radio_var.get() - 1
        self.answer_from_test = list(self.Q_AND_A.items())[self.count_question][1][self.answer] 

        messagebox.showinfo("Ishak says ...", self.answer_from_test)


if __name__ == "__main__": 
    Ishak() 







