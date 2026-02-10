from .start import router as start_router
from .location import router as location_router
from .service import router as service_router
from .date import router as date_router
from .contact import router as contact_router

routers = [
    start_router,
    location_router,
    service_router,
    date_router,
    contact_router,
]