import sys
from PyQt5 import QtWidgets
import design
from shutil import copyfile

file = None
file_ttx = None


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.selectListFiles.clicked.connect(self.browse_folder)
        self.selectTTF.clicked.connect(self.select_ttf)
        self.done.clicked.connect(self.save_files)

    def save_files(self):
        path_to_save = QtWidgets.QFileDialog.getExistingDirectory(self, "Куда сохранить?")
        if (file_ttx and file_ttx[0] != '') and (file and file[0] != '') and path_to_save:
            with open(file[0]) as file_lists:
                for line in file_lists:
                    print('{}\t{}/{}'.format(file_ttx[0], path_to_save, line))
                    copyfile(file_ttx[0], '{}/{}'.format(path_to_save, line))

    def select_ttf(self):
        self.listWidget_2.clear()
        global file_ttx
        global file
        file_ttx = QtWidgets.QFileDialog.getOpenFileName(self, "Выбери шрифтик")
        if (file_ttx and file_ttx[0] != '') and (file and file[0] != ''):
            with open(file[0]) as file_lists:
                for line in file_lists:
                    self.listWidget_2.addItem(line)

    def browse_folder(self):
        self.listWidget_2.clear()
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        global file
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Список файлов")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        if file and file[0] != '':  # не продолжать выполнение, если пользователь не выбрал фаил
            with open(file[0]) as file_lists:
                for line in file_lists:
                    self.listWidget.addItem(line)  # добавить список в listWidget
        if (file_ttx and file_ttx[0] != '') and (file and file[0] != ''):
            with open(file[0]) as file_lists:
                for line in file_lists:
                    self.listWidget_2.addItem(line)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
