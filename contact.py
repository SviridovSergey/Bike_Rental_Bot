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
    print(f"DEBUG: Sending to chat {config.GROUP_CHAT_ID}, thread {config.TOPIC_MESSAGE_ID}")
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

@router.message(ApplicationStates.waiting_for_confirmation, F.text == "✅ Подтвердить")
async def process_confirmation(message: types.Message, state: FSMContext):
    """Финальное подтверждение и отправка в группу"""
    data = await state.get_data()
    
    print(f"DEBUG: Sending to chat {config.GROUP_CHAT_ID}, thread {config.TOPIC_MESSAGE_ID}")
    
    # Формируем сообщение для группы
    group_message = f"""
🚴 <b>НОВАЯ ЗАЯВКА</b> 🚴

👤 <b>ФИО:</b> {data.get('full_name')}
📞 <b>Телефон:</b> {data.get('phone')}
📍 <b>Точка:</b> {data.get('location_name')}
🔧 <b>Услуга:</b> {data.get('service_name')}
📅 <b>День:</b> {data.get('date')}
🆔 <b>User ID:</b> {data.get('user_id')}
⏰ <b>Создано:</b> {datetime.now().strftime('%H:%M %d.%m.%Y')}

📞 <b>Менеджер:</b> {config.MANAGER_PHONE}
"""
    
    try:
        await message.bot.send_message(
            chat_id=config.GROUP_CHAT_ID,
            text=group_message,
            message_thread_id=config.TOPIC_MESSAGE_ID if config.TOPIC_MESSAGE_ID else None
        )
        print("DEBUG: Сообщение отправлено в группу")
        await message.answer("✅ Заявка отправлена!", reply_markup=get_main_keyboard())
    except Exception as e:
        print(f"ERROR: {e}")
        await message.answer(f"❌ Ошибка отправки: {e}")
    
    await state.clear()