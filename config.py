import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

@dataclass
class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    GROUP_CHAT_ID: int = int(os.getenv("GROUP_CHAT_ID", "-1002758652800"))
    TOPIC_MESSAGE_ID: int = int(os.getenv("TOPIC_MESSAGE_ID", "8774"))
    MANAGER_PHONE: str = os.getenv("MANAGER_PHONE", "+79998887766")

    LOCATIONS = {
        "west": "ул. Соколова, 80 (Западный район)\nВремя работы: 9:00-22:00",
        "center": "ул. Жмайлова, 27в (Центральный район)\nВремя работы: 10:00-23:00"
    }
    
    SERVICES = {
        "rent": "Аренда велосипеда 🚲",
        "repair": "Ремонт 🔧",
        "parts": "Покупка запчастей ⚙️",
        "inspection": "Техосмотр 📋"
    }
    
    def __post_init__(self):
        if not self.BOT_TOKEN:
            raise ValueError("❌ BOT_TOKEN не найден! Укажите его в .env файле")
        print(f"✅ Конфигурация загружена: Группа={self.GROUP_CHAT_ID}")

# Создаем экземпляр конфигурации
config = Config()