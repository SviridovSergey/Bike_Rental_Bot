from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards import get_contact_keyboard
from .start import ApplicationStates

router = Router()

@router.message(ApplicationStates.waiting_for_date)
async def process_date(message: types.Message, state: FSMContext):
    days_map = {
        "Пн": "Понедельник",
        "Вт": "Вторник",
        "Ср": "Среда",
        "Чт": "Четверг",
        "Пт": "Пятница",
        "Сб": "Суббота",
        "Вс": "Воскресенье"
    }
    
    if message.text == "⬅️ Назад":
        from keyboards import get_service_keyboard
        await message.answer("Выберите услугу:", reply_markup=get_service_keyboard())
        await state.set_state(ApplicationStates.waiting_for_service)
        return
    
    if message.text not in days_map:
        await message.answer("Пожалуйста, выберите день из предложенных:")
        return
    
    day_name = days_map[message.text]
    await state.update_data(date=day_name)
    
    data = await state.get_data()
    location_name = data.get('location_name', '')
    service_name = data.get('service_name', '')
    
    await message.answer(
        f"✅ <b>Отлично! Подтвердите данные:</b>\n\n"
        f"<b>Точка:</b> {location_name}\n"
        f"<b>Услуга:</b> {service_name}\n"
        f"<b>День:</b> {day_name}\n\n"
        f"📱 <b>Теперь введите ваши контактные данные:</b>\n"
        f"Нажмите кнопку ниже чтобы поделиться номером телефона",
        reply_markup=get_contact_keyboard()
    )
    await state.set_state(ApplicationStates.waiting_for_contact)