def main():
    input('Задать минимальный высокий DPI: ')

    print('Сортировка завершена')
    print('Для выхода нажмите Enter')
    input()


if __name__ == '__main__':
    main()

# compilation
# pyinstaller -F -i check_dpi/icon.ico check_dpi/main.py
