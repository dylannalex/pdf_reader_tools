import pyautogui
import keyboard
from pdf_reader_tools import key_bindings
from pdf_reader_tools import settings


def _draw_line(
    initial_position: tuple[int, int], final_position: tuple[int, int]
) -> None:
    """
    Drags mouse from initial position to final position.
    """
    pyautogui.moveTo(initial_position[0], initial_position[1])
    pyautogui.mouseDown()
    pyautogui.moveTo(final_position[0], final_position[1], settings.MOUSE_DRAG_TIME)
    pyautogui.mouseUp()


def line() -> None:
    """
    Records the mouse initial position when line's key binding is
    pressed, and the final position when it is released. Then draws
    a line from initial position to final position.

    A drawing tool (such as a pencil) should be selected before running
    this function.
    """
    initial_position = pyautogui.position()
    while keyboard.is_pressed(key_bindings.LINE):
        pass
    final_position = pyautogui.position()
    _draw_line(initial_position, final_position)
