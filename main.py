import json
from datetime import datetime
import os


class Notes:
    file = os.getcwd() + '/' + 'notes.json'

    def __init__(self):
        self.title = None
        self.msg = None
        self.notebook = None
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.json_note = []

    def save_note(self):
        with open(Notes.file, 'w') as f:
            json.dump(self.json_note, f, indent=4)

    def create_note(self, count_id):
        self.title = input('Введите название заметки: ')
        self.msg = input('Введите заметку: ')
        note_id = count_id + 1
        note = {'id': note_id, 'title': self.title, 'messeg': self.msg, 'create_at': self.time}
        self.json_note.append(note)
        self.save_note()
        print("Заметка создана")
        return

    def read_note(self):
        print('Если хотите прочитать определенную заметку напишите - 0, если все то напишите - 1')
        do = int(input('что хотите сделать : '))
        if do == 0:
            found_note_id = int(input('Введите id заметки для чтения : '))
            for note in self.json_note:
                if note['id'] == found_note_id:
                    print(f'ID заметки : {note['id']}')
                    print(f'Заголовок заметки : {note['title']}')
                    print(f'Текст заметки : {note['messeg']}')
                    print(f'Заметка создана в : {note['create_at']}')
                    if 'update_at' in note:
                        print(f'Заметка изменена в : {note['update_at']}')
                    print('_______________________________________________')
                    return
                else:
                    print("Такой заметки не найдено")
                    return
        elif do == 1:
            for note in self.json_note:
                print(f'ID заметки : {note['id']}')
                print(f'Заголовок заметки : {note['title']}')
                print(f'Текст заметки : {note['messeg']}')
                print(f'Заметка создана в : {note['create_at']}')
                if 'update_at' in note:
                    print(f'Заметка изменена в : {note['update_at']}')
                print('_______________________________________________')

    def update_note(self):
        found_note_id = int(input('Введите id заметки для редактирования : '))
        for note in self.json_note:
            if note['id'] == found_note_id:
                new_title = input(f'Введите новый заголовок:\nстарый: {note['title']}\n')
                new_msg = input(f'Введите новую заметку:\nстарая: {note['messeg']}\n')
                note['title'] = new_title
                note['messeg'] = new_msg
                note['update_at'] = self.time
                self.save_note()
                print("Заметка отредактирована")
                return
            else:
                print("Такой заметки не найдено")
                return

    def del_note(self):
        found_note_id = int(input('Введите id заметки которую хотите удалить : '))
        for note in self.json_note:
            if note['id'] == found_note_id:
                self.json_note.remove(note)
                self.save_note()
                print('Заметка удалена')
                return
            else:
                print("Такой заметки не найдено")
                return

    def run(self):
        note_id = None
        if not os.path.exists(Notes.file):
            with open(Notes.file, 'w') as j:
                print('создайте первую заметку')
                self.create_note(0)
        with open(Notes.file, 'r') as file:
            try:
                json_load = json.load(file)
                if json_load:
                    self.json_note = json_load
                    note_id = int(dict(json_load[-1]).get('id'))
            except json.decoder.JSONDecodeError:
                print('создайте первую заметку')
                self.create_note(0)
                print('Первая заметка создана')
                return
        print("что вы хотите сделать")
        print('1 - создать', '2 - прочитать', '3 - редактировать', '4 - удалить', '0 - выйти')
        try:
            try:
                do = int(input('что сделать : '))
                while do != 0:
                    if len(self.json_note) == 0:
                        print("Создайте первую заметку чтобы начать работать с блокнотом")
                        self.create_note(0)
                    elif do == 1:
                        self.create_note(note_id)
                    elif do == 2:
                        self.read_note()
                    elif do == 3:
                        self.update_note()
                    elif do == 4:
                        self.del_note()
                    elif do == 0:
                        print("До новых встреч")
                    else:
                        print("Я не понял, что вы хотите сделать, поэтому закончил работу")
                    do = int(input('что сделать : '))
            except ValueError:
                print("Я не понял, что вы хотите сделать, поэтому закончил работу")
        except KeyboardInterrupt:
            print("Работа законченна")


x = Notes()
x.run()
