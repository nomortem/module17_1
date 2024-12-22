from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL для подключения к базе данных SQLite
DATABASE_URL = 'sqlite:///./taskmanager.db'

# Создаем движок для базы данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Базовый класс для моделей
Base = declarative_base()

# Создание сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для создания таблиц в базе данных
def create_db():
    print("SQL для User:", str(User.__table__))
    print("SQL для Task:", str(Task.__table__))
    Base.metadata.create_all(bind=engine)