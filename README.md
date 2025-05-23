# Hospital Management System (HMS) 📋

> **Авторы:** Abylkasymov Bekzat, Erikov Nursultan, Kubanychbekov Rinat

## 📌 Описание
Консольное приложение на Python для управления больничными данными через роли: **MainDoctor**, **Doctor**, **Nurse**, **Patient**. Используется база данных MySQL и реализованы ключевые принципы ООП.

---

## 🧠 Структура проекта

```
HospitalManagementSystem.py     # Точка входа, меню, выбор ролей
Patient.py                      # Работа с пациентами
Doctor.py                       # Работа с врачами
Nurse.py                        # Работа с медсёстрами
MainDoctor.py                   # Полные права на просмотр и редактирование
Instruction.py                  # Работа с медицинскими инструкциями
```

---

## 🔑 Пример: Авторизация (HospitalManagementSystem.py)

```python
if choice == '1':
    md = MainDoctor()
    md.login()
```
📷 ![auth_example](Class_Object.png)

---

## ➕ Пример: Добавление пациента (Patient.py)

```python
def add_patient(self):
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    ...
    cursor.execute("INSERT INTO patients (name, age, ...) VALUES (%s, %s, ...)", (...))
```
📷 ![add_patient](Constructor.png)

---

## 📋 Пример: Просмотр пациентов (MainDoctor.py)

```python
def view_patients(self):
    cursor.execute("SELECT * FROM patients")
    for patient in cursor.fetchall():
        print(patient)
```
📷 ![view_patients](Encapsulation.png)

---

## 🗑️ Пример: Удаление пациента (Patient.py)

```python
def delete_patient(self):
    pid = input("Enter Patient ID to delete: ")
    cursor.execute("DELETE FROM patients WHERE id = %s", (pid,))
```
📷 ![delete_patient](Inheritance.png)

---

## 🧬 Пример: Наследование и расширение (MainDoctor -> Doctor)

```python
class MainDoctor(Doctor):
    def delete_doctor(self):
        ...
```
📷 ![inheritance](Polymorphism.png)

---

## 🧪 Используемые технологии

- Python 3.10+  
- MySQL 8.0+  
- `mysql-connector-python`

---

## ⚙️ Как запустить

1. Установить MySQL и создать базу данных `hms`
2. Установить зависимости:
```bash
pip install mysql-connector-python
```
3. Запустить:
```bash
python HospitalManagementSystem.py
```

---

## 🎓 Ключевые принципы ООП в проекте

- ✅ **Инкапсуляция:** защищённые поля, геттеры и сеттеры  
- ✅ **Наследование:** `MainDoctor` наследует `Doctor`  
- ✅ **Полиморфизм:** одинаковые методы (`view_patients`) в разных классах  
- ✅ **Конструкторы:** `__init__` для инициализации объектов

---

