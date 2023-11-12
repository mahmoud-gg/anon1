from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("جار الاتصال ب مستودع بيانات مونجو...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("تم الاتصال بـمستودع بيانات مونجو.")
except:
    LOGGER(__name__).error("فشل في الاتصال بـمستودع بيانات مونجو.")
    exit()
