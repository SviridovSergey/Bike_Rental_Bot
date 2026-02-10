from aiogram import Bot
from database.models import Application
from config import Config

async def send_to_admin(application: Application, bot: Bot):
    message_text = f"""
<b>НОВАЯ ЗАЯВКА!</b>

👤 <b>Клиент:</b> {application.full_name}
📞 <b>Телефон:</b> {application.phone}
📍 <b>Точка:</b> {application.location}
🔧 <b>Услуга:</b> {application.service}
📅 <b>День:</b> {application.date}
🆔 <b>User ID:</b> {application.user_id}
⏰ <b>Создано:</b> {application.created_at.strftime('%H:%M %d.%m.%Y')}

📞 <b>Менеджер:</b> {Config.MANAGER_PHONE}
"""
    
    try:
        await bot.send_message(
            chat_id=Config.ADMIN_CHAT_ID,
            text=message_text,
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"Ошибка отправки админу: {e}")