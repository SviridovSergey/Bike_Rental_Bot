from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📋 Создать заявку")
    builder.button(text="📞 Контакты")
    builder.button(text="ℹ️ О нас")
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def get_location_keyboard():
    """Клавиатура выбора локации"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="ул. Соколова, 80")        
    builder.button(text="ул. Жмайлова, 27в")      
    builder.button(text="⬅️ Назад")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True)

def get_service_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="🚲 Аренда")
    builder.button(text="🔧 Ремонт")
    builder.button(text="⚙️ Запчасти")
    builder.button(text="📋 Техосмотр")
    builder.button(text="⬅️ Назад")
    builder.adjust(2, 2, 1)
    return builder.as_markup(resize_keyboard=True)

def get_date_keyboard():
    builder = ReplyKeyboardBuilder()
    days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс", "⬅️ Назад"]
    for day in days:
        builder.button(text=day)
    builder.adjust(3, 3, 2)
    return builder.as_markup(resize_keyboard=True)

def get_contact_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📱 Отправить контакт", request_contact=True)
    builder.button(text="⬅️ Отмена")
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def get_confirm_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="✅ Подтвердить")
    builder.button(text="❌ Отменить")
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def get_back_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="⬅️ Назад")
    return builder.as_markup(resize_keyboard=True)

def get_fio_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="👤 Ввести ФИО")
    builder.button(text="⬅️ Назад")
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)