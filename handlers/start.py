from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards import get_main_keyboard, get_location_keyboard
from config import config

router = Router()

class ApplicationStates(StatesGroup):
    waiting_for_location = State()
    waiting_for_service = State()
    waiting_for_date = State()
    waiting_for_contact = State()
    waiting_for_confirmation = State()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = """
🚴 <b>Добро пожаловать в KUARON!</b> 🚴

Мы предлагаем:
• Аренду электровелосипедов 🚲
• Ремонт 🔧
• Запчасти и аксессуары ⚙️
• Технический осмотр 📋

Для создания заявки нажмите "📋 Создать заявку"
"""
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = f"""
📋 <b>Доступные команды:</b>

/start - Главное меню
/help - Помощь

📞 <b>Контакты менеджера:</b>
{config.MANAGER_PHONE}

Работаем для вас 7 дней в неделю! ⏰
"""
    await message.answer(help_text)

@router.message(F.text == "📞 Контакты")
async def show_contacts(message: types.Message):
    await message.answer(f"📞 <b>Телефон менеджера:</b>\n{config.MANAGER_PHONE}")

@router.message(F.text == "ℹ️ О нас")
async def about_us(message: types.Message):
    about_text = """
<b>BikeService</b> - сеть велопрокатов и сервисных центров!

📍 <b>Наши точки:</b>
• ул. Соколова, 80 (Западный район)
• ул. Жмайлова, 27в (Центральный район)

⏰ <b>Режим работы:</b>
Ежедневно с 9:00 до 22:00
"""
    await message.answer(about_text)
    
@router.message(F.text == "📋 Создать заявку")
async def create_application(message: types.Message, state: FSMContext):
    await message.answer(
        "📍 <b>Выберите точку обслуживания:</b>\n\n"
        "• ул. Соколова, 80 (Западный район)\n"
        "• ул. Жмайлова, 27в (Центральный район)",
        reply_markup=get_location_keyboard()
    )
    await state.set_state(ApplicationStates.waiting_for_location)

@router.message(F.text == "⬅️ Назад")
async def back_to_main(message: types.Message, state: FSMContext):
    await state.clear()
    await cmd_start(message)