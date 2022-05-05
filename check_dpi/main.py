from pathlib import Path

from PIL import Image


def main():
    # MIN_DPI = input('Задать минимальный высокий DPI: ')

    images = Path().rglob('*.jpg')
    for image in images:
        im = Image.open(image)
        print(image)
        print(im.format, im.size, im.mode)
        print(im.info)
        print()

    # print('Сортировка завершена')
    print('Для выхода нажмите Enter')
    input()


if __name__ == '__main__':
    main()

# compilation
# pyinstaller -F -i check_dpi/icon.ico check_dpi/main.py
