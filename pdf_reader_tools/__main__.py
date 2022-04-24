import keyboard
from pdf_reader_tools import key_bindings
from pdf_reader_tools import line


def main():
    while True:
        if keyboard.is_pressed(key_bindings.LINE):
            line.line()
        if keyboard.is_pressed(key_bindings.EXIT):
            return


if __name__ == "__main__":
    main()
