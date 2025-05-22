# Тестування працездатності системи

## 🔸POST - ЗАПИТ
### *-- Create Role --*
```bash
{
  "name": "Expert",
  "description": "Responsible for creating and evaluating quizzes"
}
```
![image](https://github.com/user-attachments/assets/79bfe40e-13e1-4a2c-9639-ffe26f31532a)
### *-- Create User --*
```bash
{
  "email": "diana.s@gmail.com",
  "password": "123!",
  "name": "Diana",
  "surname": "Siukalo",
  "nickname": "dirrialss"
}
```
![image](https://github.com/user-attachments/assets/f87b2d55-1bed-49ae-baf7-46af2a4ea7b3)
### *-- Create Quiz --*
```bash
{
  "name": "Mental Well-being Assessment",
  "description": "A short quiz to evaluate a person's current emotional and psychological state",
  "created_by": 1,
  "User_id": 1
}
```
![image](https://github.com/user-attachments/assets/201292d5-9fb0-448a-a738-c830610b67a8)


## 🔸GET - ЗАПИТ
### *-- Read Roles --*
![image](https://github.com/user-attachments/assets/53138daa-23af-4816-9fda-b4bd1b79479e)
### *-- Read Users --*
![image](https://github.com/user-attachments/assets/209f7d4d-268b-4a2f-88d8-7ccb484b9b2d)
### *-- Read Quizzes --*
![image](https://github.com/user-attachments/assets/64bb770b-ed27-441e-bc47-e94ba368d50e)

## 🔸PUT - ЗАПИТ

### *-- Update Role --*
```bash
{
  "name": "Diana",
  "description": "Has full access to the system"
}

```
![image](https://github.com/user-attachments/assets/917a381a-97f8-4601-aaa8-56607176748f)

### *-- Update User --*
```bash
{
  "email": "diana.s@gmail.com",
  "password": "123!",
  "name": "Siukalo",
  "surname": "Siukalo",
  "nickname": "dirrialss"
}
```
![image](https://github.com/user-attachments/assets/5d5539be-a323-4c4f-844f-7c44776a24dd)

### *-- Update Quiz --*
```bash
{
  "name": "Mental Well-being Assessment",
  "description": "Test",
  "created_by": 1,
  "User_id": 2
}
```
![image](https://github.com/user-attachments/assets/fba3f5d8-7ee0-450d-978b-d1a538d86d21)

## 🔸DELETE - ЗАПИТ

### *-- Delete Role --*
![image](https://github.com/user-attachments/assets/84031767-ea95-49ff-a943-cf684077d3ea)

### *-- Delete User --*
![image](https://github.com/user-attachments/assets/d89cbaa1-63de-47f3-b9ad-1d7c96ba5391)

### *-- Delete Quiz --*
![image](https://github.com/user-attachments/assets/1237555e-71f5-4fdb-91f7-90be214a0131)


