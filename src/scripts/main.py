from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import mysql.connector

app = FastAPI()

# ───────────── КОНФІГУРАЦІЯ БД ─────────────
db_config = {
    "host": "localhost",
    "port": 3305,
    "user": "root",
    "password": "mysqlpassword1",
    "database": "mydb"
}

# ───────────── МОДЕЛІ ─────────────
class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class Role(RoleBase):
    id: int

class UserBase(BaseModel):
    email: str
    password: str
    name: str
    surname: str
    nickname: str
    picture: Optional[bytes] = None

class User(UserBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class QuizBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    created_by: Optional[int]
    User_id: int

class Quiz(QuizBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

# ───────────── ENDPOINTS: Role ─────────────
@app.get("/roles", response_model=List[Role])
def get_roles():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Role")
    roles = cursor.fetchall()
    cursor.close()
    conn.close()
    return roles

@app.post("/roles", status_code=201)
def create_role(role: RoleBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Role (name, description) VALUES (%s, %s)",
        (role.name, role.description)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Role created"}

@app.put("/roles/{role_id}")
def update_role(role_id: int, role: RoleBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Role SET name=%s, description=%s WHERE id=%s",
        (role.name, role.description, role_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Role updated"}

@app.delete("/roles/{role_id}")
def delete_role(role_id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Role WHERE id=%s", (role_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Role deleted"}

# ───────────── ENDPOINTS: User ─────────────
@app.get("/users", response_model=List[User])
def get_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

@app.post("/users", status_code=201)
def create_user(user: UserBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO User (email, password, name, surname, nickname, picture, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())
    """, (user.email, user.password, user.name, user.surname, user.nickname, user.picture))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User created"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE User SET email=%s, password=%s, name=%s, surname=%s, nickname=%s, picture=%s, updated_at=NOW()
        WHERE id=%s
    """, (user.email, user.password, user.name, user.surname, user.nickname, user.picture, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User updated"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM User WHERE id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User deleted"}

# ───────────── ENDPOINTS: Quiz ─────────────
@app.get("/quizzes", response_model=List[Quiz])
def get_quizzes():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Quiz")
    quizzes = cursor.fetchall()
    cursor.close()
    conn.close()
    return quizzes

@app.post("/quizzes", status_code=201)
def create_quiz(quiz: QuizBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Quiz (name, description, created_by, created_at, updated_at, User_id)
        VALUES (%s, %s, %s, NOW(), NOW(), %s)
    """, (quiz.name, quiz.description, quiz.created_by, quiz.User_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Quiz created"}

@app.put("/quizzes/{quiz_id}")
def update_quiz(quiz_id: int, quiz: QuizBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Quiz SET name=%s, description=%s, created_by=%s, updated_at=NOW(), User_id=%s
        WHERE id=%s
    """, (quiz.name, quiz.description, quiz.created_by, quiz.User_id, quiz_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Quiz updated"}

@app.delete("/quizzes/{quiz_id}")
def delete_quiz(quiz_id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Quiz WHERE id=%s", (quiz_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Quiz deleted"}
