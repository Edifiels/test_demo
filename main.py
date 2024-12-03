import os
import platform
import time
import pyautogui


class CalculatorAutomation:
    def __init__(self):
        self.system_name = platform.system()
        self.buttons = {
            "0": "images/0.png",
            "1": "images/1.png",
            "2": "images/2.png",
            "3": "images/3.png",
            "4": "images/4.png",
            "5": "images/5.png",
            "6": "images/6.png",
            "7": "images/7.png",
            "8": "images/8.png",
            "9": "images/9.png",
            "+": "images/plus.png",
            "-": "images/minus.png",
            "*": "images/multiply.png",
            "/": "images/divide.png",
            "=": "images/equals.png"
        }

    def open_calculator(self):
        if self.system_name == "Windows":
            os.system("start calc")
        elif self.system_name == "Linux":
            os.system("gnome-calculator &")
        else:
            raise Exception(
                "Неизвестная операционная система: " + self.system_name)

    def click_button(self, image_name):
        try:
            button_location = pyautogui.locateOnScreen(
                image_name, confidence=0.9)
            if button_location is not None:
                button_center = pyautogui.center(button_location)
                pyautogui.click(button_center)
                print(f"Кнопка {image_name} успешно найдена и нажата.")
                return
            else:
                print(
                    f"Кнопка {image_name} не найдена на экране. Повторная попытка...")
                time.sleep(1)
        except Exception as e:
            print(f"Произошла ошибка при поиске кнопки {image_name}: {e}")
            exit(1)
        print(f"Ошибка: Кнопка {image_name} не найдена. Завершение работы.")
        exit(1)

    def perform_calculation(self, calculation_sequence):
        self.open_calculator()
        time.sleep(3)

        for button in calculation_sequence:
            self.click_button(self.buttons[button])
            time.sleep(0.5)

        print("Операция выполнена успешно!")


if __name__ == "__main__":
    calculator_automation = CalculatorAutomation()
    calculation = ["1", "2", "+", "7", "="]
    calculator_automation.perform_calculation(calculation)
