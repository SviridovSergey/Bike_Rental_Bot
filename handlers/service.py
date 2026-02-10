from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards import get_date_keyboard
from .start import ApplicationStates

router = Router()

@router.message(ApplicationStates.waiting_for_service)
async def process_service(message: types.Message, state: FSMContext):
    service_map = {
        "🚲 Аренда": "rent",
        "🔧 Ремонт": "repair",
        "⚙️ Запчасти": "parts",
        "📋 Техосмотр": "inspection"
    }
    
    if message.text not in service_map:
        if message.text != "⬅️ Назад":
            await message.answer("Пожалуйста, выберите услугу из предложенных:")
        return
    
    if message.text == "⬅️ Назад":
        from keyboards import get_location_keyboard
        await message.answer("Выберите локацию:", reply_markup=get_location_keyboard())
        await state.set_state(ApplicationStates.waiting_for_location)
        return
    
    service_key = service_map[message.text]
    service_name = message.text
    
    await state.update_data(service=service_key, service_name=service_name)
    
    data = await state.get_data()
    location_name = data.get('location_name', '')
    
    await message.answer(
        f"📍 <b>Точка:</b> {location_name}\n"
        f"📋 <b>Услуга:</b> {service_name}\n\n"
        f"📅 <b>Теперь выберите день недели:</b>",
        reply_markup=get_date_keyboard()
    )
    await state.set_state(ApplicationStates.waiting_for_date)