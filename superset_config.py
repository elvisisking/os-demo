import os
import demo_init

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = 'mysql://superset:superset@mysql:3306/superset'
SECRET_KEY = 'thisISaSECRET_1234'

POSTGRES_DATABASE = "superset_demo"
POSTGRES_USERNAME = "postgres"
POSTGRES_PASSWORD = ""

demo_init.create_driver()
demo_init.create_traffic_violation()
demo_init.create_driver_offenses()
demo_init.create_route()
demo_init.create_car_data()
demo_init.create_weather_data()
demo_init.create_demo_dashboard()
