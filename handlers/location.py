from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards import get_service_keyboard
from .start import ApplicationStates

router = Router()

@router.message(ApplicationStates.waiting_for_location)
async def process_location(message: types.Message, state: FSMContext):
    # Обновляем mapping
    location_map = {
        "ул. Соколова, 80": "west",          # ← Новый текст кнопки
        "ул. Жмайлова, 27в": "center"        # ← Новый текст кнопки
    }
    
    if message.text not in location_map:
        await message.answer("Пожалуйста, выберите локацию из предложенных:")
        return
    
    location_key = location_map[message.text]
    location_name = "ул. Соколова, 80" if location_key == "west" else "ул. Жмайлова, 27в"
    
    await state.update_data(location=location_key, location_name=location_name)
    
    await message.answer(
        f"📍 <b>Выбрана точка:</b> {location_name}\n\n"
        f"📋 <b>Теперь выберите услугу:</b>",
        reply_markup=get_service_keyboard()
    )
    await state.set_state(ApplicationStates.waiting_for_service)