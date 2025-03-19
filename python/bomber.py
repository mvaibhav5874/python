import pyautogui
import time

def type_and_send_message(message, delay=1, repetitions=1):
    try:
        for _ in range(repetitions):
            pyautogui.typewrite(message)
            pyautogui.press("enter")  # Simulates pressing the Enter key
            time.sleep(delay)

    except pyautogui.FailSafeException:
        print("PyAutoGUI fail-safe triggered. Move mouse to a corner of the screen to stop.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_user_input():
  """Gets user input for the message, repetitions, and delay."""

  message = input("Enter the message to send: ")
  while True:
    try:
      repetitions = int(input("Enter the number of repetitions: "))
      break
    except ValueError:
      print("Invalid input. Please enter an integer for repetitions.")

  while True:
    try:
      delay = float(input("Enter the delay between messages (in seconds): "))
      break
    except ValueError:
      print("Invalid input. Please enter a number for delay.")

  return message, repetitions, delay

if __name__ == "__main__":
    print("Place your cursor where you want to type the message.")
    time.sleep(5) #gives you 5 seconds to place cursor.
    message, repetitions, delay = get_user_input()
    type_and_send_message(message, delay, repetitions)