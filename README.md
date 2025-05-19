Hospital Management System (HMS)
Описание
Hospital Management System (HMS) — консольное приложение для управления данными больницы. Позволяет работать с информацией о пациентах, врачах, медсестрах и инструкциях через разные роли: MainDoctor, Doctor, Nurse и Patient.

Система поддерживает операции добавления, удаления, просмотра записей и аутентификации пользователей.

Технологии
Python 3.x

MySQL 8.x

mysql-connector-python (для подключения Python к MySQL)

Структура проекта
HospitalManagementSystem.py — главный файл с точкой входа в программу и меню пользователя.

Модули классов:

Patient.py — класс для работы с пациентами (добавление, удаление, просмотр и авторизация).

Doctor.py — класс для работы с врачами.

Nurse.py — класс для работы с медсестрами.

MainDoctor.py — класс для главного врача.

Instruction.py — класс для работы с инструкциями.

Установка и настройка
1. Установка MySQL
Установите MySQL сервер (https://dev.mysql.com/downloads/mysql/).

Создайте базу данных hms:

sql
Копировать
Редактировать
CREATE DATABASE hms;
USE hms;
Создайте таблицу patients:

sql
Копировать
Редактировать
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    height DECIMAL(5,2),
    weight DECIMAL(5,2),
    illness VARCHAR(255),
    dob DATE,
    arrival_date DATE
);
Аналогично создайте таблицы для врачей, медсестер и инструкций по структуре вашего проекта.

2. Установка зависимостей Python
Рекомендуется создать виртуальное окружение и установить пакет для работы с MySQL:

bash
Копировать
Редактировать
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install mysql-connector-python
Запуск
Выполните команду в терминале:

bash
Копировать
Редактировать
python HospitalManagementSystem.py
Использование
При запуске выберите тип аккаунта: MainDoctor, Doctor, Nurse, или Patient.

Введите логин и пароль для аутентификации.

В зависимости от роли получите доступ к функциям:

Добавление, удаление и просмотр пациентов, врачей, медсестер.

Просмотр и управление расписанием врачей.

Просмотр и добавление инструкций.

Просмотр информации о пациентах и личных данных.

Формат даты
Вводите даты в формате ДД.ММ.ГГГГ, например: 20.12.2005.

Система автоматически преобразует их в формат ГГГГ-ММ-ДД для корректного сохранения в MySQL.

Пример добавления пациента
Пример ввода данных при добавлении пациента:

mathematica
Копировать
Редактировать
Enter Patient Name: Ivan Ivanov
Enter Patient Age: 45
Enter Patient Gender: Male
Enter Patient Height: 175
Enter Patient Weight: 78.0
Enter Patient Illness: Hypertension
Enter Patient Date of Birth (e.g., 20.12.2005): 12.04.1978
Enter Patient's Arrival Date (e.g., 01.05.2025): 10.05.2025
Авторизация
Patient:

Логин: Pat

Пароль: 321

Пароли для других ролей задаются в соответствующих классах.

Важные моменты
Вход в систему с использованием встроенных логинов и паролей.

Обработка исключений с выводом ошибок.

Использование подготовленных SQL-запросов с параметрами для безопасности.

Консольный интерфейс с меню.
