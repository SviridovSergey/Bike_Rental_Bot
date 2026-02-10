from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from datetime import datetime
from aiogram.fsm.state import State, StatesGroup

from keyboards import get_main_keyboard, get_confirm_keyboard, get_fio_keyboard
from .start import ApplicationStates
from config import config

router = Router()

@router.message(F.text == "❌ Отменить")
async def cancel_handler(message: types.Message, state: FSMContext):
    """Обработка отмены из любого состояния"""
    from keyboards import get_main_keyboard
    
    await message.answer(
        "Заявка отменена",
        reply_markup=get_main_keyboard()
    )
    await state.clear()

async def ask_for_contact(message: types.Message, state: FSMContext):
    """Запрашиваем контакт напрямую"""
    from keyboards import get_contact_keyboard
    await message.answer(
        "📱 <b>Поделитесь номером телефона:</b>\n"
        "Нажмите кнопку ниже ⬇️",
        reply_markup=get_contact_keyboard()
    )

@router.message(ApplicationStates.waiting_for_contact, F.contact)
async def process_contact(message: types.Message, state: FSMContext):
    """Обработка контакта"""
    phone = message.contact.phone_number
    
    # Получаем имя пользователя
    user = message.from_user
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
    if not full_name:
        full_name = f"@{user.username}" if user.username else "Не указано"
    
    await state.update_data(
        phone=phone,
        full_name=full_name,
        user_id=user.id
    )
    
    data = await state.get_data()
    
    summary = f"""
📋 <b>Проверьте заявку:</b>

👤 <b>Клиент:</b> {full_name}
📞 <b>Телефон:</b> {phone}
📍 <b>Точка:</b> {data.get('location_name')}
🔧 <b>Услуга:</b> {data.get('service_name')}
📅 <b>День:</b> {data.get('date')}

✅ <b>Все верно?</b>
"""
    
    from keyboards import get_confirm_keyboard
    await message.answer(
        summary,
        reply_markup=get_confirm_keyboard()
    )
    await state.set_state(ApplicationStates.waiting_for_confirmation)