from aiogram import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Dict, Any, Awaitable
import asyncio

class FloodControlMiddleware(BaseMiddleware):
    def __init__(self, limit: float = 0.5):
        self.last_time = {}
        self.limit = limit
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        user_id = None
        
        if event.message:
            user_id = event.message.from_user.id
        elif event.callback_query:
            user_id = event.callback_query.from_user.id
        
        if user_id:
            current_time = asyncio.get_event_loop().time()
            
            if user_id in self.last_time:
                time_passed = current_time - self.last_time[user_id]
                if time_passed < self.limit:
                    if event.message:
                        await event.message.answer("⏳ Пожалуйста, подождите...")
                    return
            
            self.last_time[user_id] = current_time
        
        return await handler(event, data)