import os        # Інструменти для роботи з системою (очищення екрана)
import platform  # Для отримання даних про твій Linux
import shutil    # Для розрахунку місця на диску
import time      # Для створення затримки в 1 секунду
import psutil    # Для виведення навантаження ПК
from datetime import datetime # Для роботи з часом

while True:      # Початок вічного циклу (оновлення панелі)
    os.system('clear') # Очищуємо старий текст, щоб панель не "бігла" вниз
    
    # Отримуємо поточний час у форматі Години:Хвилини:Секунди
    now = datetime.now().strftime("%H:%M:%S")
    
    # Рахуємо вільне місце (ділимо на 2 у 30-й степені, щоб отримати ГБ)
    free = shutil.disk_usage("/").free // (2**30)
    cpu_load = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    print("=" * 35)
    print(f" Панель керування Wriffinor")
    print("=" * 40)
    print(f" Поточний час: {now}")
    print(f"Навантаження CPU: {cpu_load}")
    print(f"Використано RAM: {ram.percent}% ({ram.used // (2**20)} MB)")
    print(f" Вільний простір: {free} ГБ")
    # Визначаємо статус залежно від навантаження
    if cpu_load > 80 or ram.percent > 80:
        status = "!! Помилка: Велика загрузка !!"
        # Записуємо у файл
        with open("log.txt", "a") as file:
         file.write(f"{now} - Увага: Навантаження CPU {cpu_load}%\n")
    else:
        status = "Нормальний"
     # Тепер виводимо цей статус
    print(f"Статус системи: {status}")   
    print("=" * 40)
    
    time.sleep(1) # Робимо паузу на 1 секунду перед наступним оновленням