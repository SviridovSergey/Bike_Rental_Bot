import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramNetworkError

from config import config
from handlers import routers

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    )
    dp = Dispatcher(storage=MemoryStorage())
    
    for router in routers:
        dp.include_router(router)
    
    max_retries = 5
    retry_delay = 30
    
    for attempt in range(max_retries):
        try:
            logger.info(f"Попытка подключения {attempt + 1}/{max_retries}")
            
            await bot.delete_webhook(drop_pending_updates=True)
            
            logger.info("Бот запущен!")
            
            await dp.start_polling(
                bot,
                allowed_updates=dp.resolve_used_update_types(),
                polling_timeout=60,
                relax=5.0
            )
            
            break
            
        except TelegramNetworkError as e:
            logger.error(f"Сетевая ошибка: {e}")
            if attempt < max_retries - 1:
                logger.info(f"Переподключение через {retry_delay}с...")
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Экспоненциальная задержка
                continue
            else:
                raise
        except Exception as e:
            logger.error(f"Критическая ошибка: {e}")
            break
    
    # Закрываем сессию
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())