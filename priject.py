import os.path
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.messagebox import showerror, showinfo

    

def note_pad_edit():
    if(notes_listbox.curselection()):
        help = 'edit'
        note_pad(help) 
    else:
        showerror(title="не выполнено", message="файл не выбран")

def note_pad_create():
    help = 'create'
    note_pad(help) 


def note_pad(help):

    

    window = Tk()
    window.title("Новое окно")
    window.geometry("500x500")

    pole_name=ttk.Entry(window)
    pole_name.place(x=260, y=5, height=25, width=200)

    label = ttk.Label(window, text="Название заметки")
    label.place(x=5, y=5)

    editor = Text(window, wrap="word")
    editor.place(x=5, y=40, height=380, width=450)

    def finish():
        window.destroy()  # ручное закрытие окна и всего приложения
        btn_edit.config(state = 'normal')
        delete_btn.config(state = 'normal')

    window.protocol("WM_DELETE_WINDOW", finish)


    if(help == 'edit'):
        
        btn_edit.config(state = 'disable')
        delete_btn.config(state = 'disable')
        selection = notes_listbox.curselection()
        pole_name.insert(0, notes_listbox.get(selection[0]))
        s = 'notes/'+notes_listbox.get(selection[0])+'.txt'
        with open(s, 'r', encoding='utf-8') as file:
            editor.insert('1.0', str(file.read()))
        


    def write_text(file_path):
        with open(file_path,'w', encoding='utf-8') as file:
            file.write(editor.get(1.0, END))
            if (os.path.exists(file_path)):
                showinfo(title="успешно", message="Заметка сохранена")
                add_notes_in_listbox()



    def save_text():
        file_path = 'notes/' + str(pole_name.get()) + '.txt'
        btn_edit.config(state = 'normal')
        delete_btn.config(state = 'normal')
       
        if(help=='create'):
            if(os.path.exists(file_path)):
                showerror(title="не выполнено", message="заметка с таким именем уже существует")

            else:    
                write_text(file_path)
                window.destroy()

        else:
            write_text(file_path)
            window.destroy()

    save_btn = ttk.Button(window, text="сохранить", command=save_text)
    save_btn.place(x=400, y=450, height=40, width=100)



        

    
def add_notes_in_listbox():
    # добавляем в список начальные элементы
    notes_listbox.delete(0, END)
    path = os.getcwd() + '/notes'
    # чтение записей
    with os.scandir(path) as listOfEntries:  
        for entry in listOfEntries:
            # печать всех записей, являющихся файлами
            if entry.is_file():
                notes_listbox.insert(END, entry.name.split('.txt')[0])   


def delete_notes():
    if(notes_listbox.curselection()):
        selection = notes_listbox.curselection()
        # мы можем получить удаляемый элемент по индексу
        os.remove('notes/'+notes_listbox.get(selection[0])+'.txt')
        notes_listbox.delete(selection[0])
    else:
        showerror(title="не выполнено", message="файл не выбран")

root = Tk()     # создаем корневой объект - окно
root.title("Приложение Заметки 1.0")     # устанавливаем заголовок окна
root.iconbitmap(default="ico/sketch.ico")
root.geometry("500x300+100+100")    # устанавливаем размеры окна

root.minsize(500,300)   # минимальные размеры: ширина - 200, высота - 15

btn_save = ttk.Button(text="Создать заметку", width=24, command=note_pad_create)
btn_save.pack(anchor=NW)
btn_edit = ttk.Button(text="Редактировать заметку", width=24, state='normal', command=note_pad_edit)
btn_edit.pack(anchor=NW)
delete_btn = ttk.Button(text="Удалить", width=24, state='normal', command=delete_notes, )
delete_btn.pack(anchor=NW)
 
# создаем список
notes_listbox = Listbox()
notes_listbox.place(x=154)

add_notes_in_listbox()




root.mainloop()