from aiogram import Router, types
from aiogram.exceptions import TelegramRetryAfter, TelegramNetworkError, TelegramServerError
import logging
import asyncio

router = Router()
logger = logging.getLogger(__name__)

@router.errors()
async def error_handler(event: types.ErrorEvent):
    exception = event.exception
    
    if isinstance(exception, TelegramRetryAfter):
        # Flood control - ждем указанное время
        logger.warning(f"Flood control! Wait {exception.retry_after} seconds")
        await asyncio.sleep(exception.retry_after)
        return True
    
    elif isinstance(exception, (TelegramNetworkError, TelegramServerError)):
        # Сетевые ошибки - логируем и продолжаем
        logger.error(f"Network error: {exception}")
        return True
    
    logger.error(f"Unhandled exception: {exception}", exc_info=True)
    return False