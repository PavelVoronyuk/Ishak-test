import tkinter as tk
#ОКНО И ЕГО НАСТРОЙКА
win = tk.Tk()
win.title("Тест на ИШАКА")
win.geometry("800x550+400+100")
win.resizable(False, False)
win.config(bg="#85c7ed")
win.iconbitmap(r"C:\Users\ASUS\Desktop\python\ISHAK_TEST\ishak.ico")
#------------------------------------------------------------------------------------------------
#ЗДРАВИЯ ЖЕЛАЮ
privet = tk.Label(win, text="Проходи тест на ишака!!!!",
                   bg="#0f6191", fg="white", font=("Courier New", 20, "bold"), width=60)
privet.pack()
#------------------------------------------------------------------------------------------------
#СМЕНА ВОПРОСА
que_list = ["вв" ,"2. Тест на ишака", "3.Есть ли у Ишака рога?", "4.Кто сильнее? : Ишак или баран?", "5.Почему ишак есть ишак?", "6.Кто отчим?", "7.Кто надристал??", "КОНЕЦ", "КОНЕЦ Я СКАЗАЛ!!!!!"]

#------------------------------------------------------------------------------------------------
#ЛИСТЫ ВОПРОСОВ И ОТВЕТОВ
btn_vopr1_list = ["place1", "всмысле", "Естественно!!!!", "Ишак!!!", "хз", "Жужа!!", "Ишак", "КОНЕЦ", "КОНЕЦ!!!"]
#
otvet_list1 = ["Вот и правильно!", "Ты ишак!!! Иди лечись",
                "Правильно, ай малядець!", "Ай какой малядець!! Настоящий поклонник ишака!",
                  "Дегроид тупой!", "Не правильно! Жужа не отчим! Она ишак!",
                    "Как ты мог такое подумать?! Иди убейся!!!!!!!!", "КОНЕЦ", "КОНЕЦ!!!"]
#   
btn_vopr2_list = ["place1", "понял", "Нет!!!!!", "Баран??????????",
                   "Потому что!!", "Малыш гад", "Отчим!!!!", "КОНЕЦ", "КОНЕЦ!!!"]
#
otvet_list2 = ["Не ври чорт!!!", "Ты не ишак, ай малядець!", "Ты шо дебилоид? У ишака есть рога!!!!!!!!",
                "Ну ты и в самом деле баран тупой!\n Конечно ишак сильнее!",
                  "Правильно! Потому что так надо!", "Конечно малыш, этот козёл всех собак\n в округе оприходовал",
                    "Конечно отчим!", "КОНЕЦ", "КОНЕЦ!!!"]
#
class Otv_And_Next:
    otv_cnt = 0
    que_counter = 0
    @classmethod
    def vop_1(cls):
        if not cls.otv_cnt + 2 > len(otvet_list1):
            otvet["text"] = otvet_list1[cls.otv_cnt]
        if btn_vopr1["text"] == "КОНЕЦ!!!":
            win.quit()

    @classmethod
    def vop_2(cls):
        if not cls.otv_cnt + 2 > len(otvet_list2):
            otvet["text"] = otvet_list2[cls.otv_cnt]
        if btn_vopr1["text"] == "КОНЕЦ!!!":
            win.quit()

    @classmethod        
    def next_func(cls):
        if not cls.otv_cnt + 2 > len(otvet_list2):
            otvet["text"] = "..."
            btn_vopr1["text"] = btn_vopr1_list[cls.otv_cnt+1]
            btn_vopr2["text"] = btn_vopr2_list[cls.otv_cnt+1]
            cls.otv_cnt += 1
        if btn_vopr1["text"] == "КОНЕЦ!!!":
            win.quit()
        if not cls.que_counter + 1 > len(que_list):
            ques["text"] = que_list[cls.que_counter + 1]
            cls.que_counter += 1

    @classmethod
    def label_changer(cls):
        privet["text"] = "Тест начат!!!"
        btn_start.pack_forget()
        ques.pack(anchor='nw', padx=30, pady=30)
        btn_vopr1.pack(pady=20)
        btn_vopr2.pack(pady=50)
        otvet.pack()
        btn_next.pack()
#ЛЕЙБЛ ОТВЕТА
btn_start = tk.Button(bg="#eb493d", font=("Courier New", 20, "bold"), text="Начать",
                       relief=tk.RAISED, bd=10, activebackground="maroon", command = Otv_And_Next.label_changer)
#СТАРТ
btn_start.pack(pady=100)
otvet = tk.Label(text="...", font=("Courier New", 20, "bold"), bg="#85c7ed")
#------------------------------------------------------------------------------------------------
#ЛЕЙБЛ ВОПРОСА
ques = tk.Label(text="1. Ты ишак?", font=("Courier New", 20, "bold"), bg="#85c7ed")
#ОСНОВНЫЕ КНОПКИ
btn_vopr1 = tk.Button(text="Да", command = Otv_And_Next.vop_1, font=("Courier New", 20, "bold"), bg="#4ae32b")
btn_vopr2 = tk.Button(text="Нет", command = Otv_And_Next.vop_2, font=("Courier New", 20, "bold"), bg="#4ae32b")
btn_next = tk.Button(text="Далее", command = Otv_And_Next.next_func, font=("Courier New", 20, "bold"), bg="#f7b705")

#база
win.mainloop()