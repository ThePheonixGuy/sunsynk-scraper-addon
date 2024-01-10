UPDATE_INTERVAL = 5
DEBUG_LOGGING = True
BATTERY_DISCHARGE_RATE = 2.5
BATTERY_MINIMUM_SOC = 15
INSECURE_MQTT = False
REGION = 1

def set_values_from_options(options):
    global UPDATE_INTERVAL
    global DEBUG_LOGGING
    global BATTERY_DISCHARGE_RATE
    global INSECURE_MQTT
    global REGION

    UPDATE_INTERVAL = options['update_interval'] if 'update_interval' in options else 60 
    DEBUG_LOGGING = options['debug_logging'] if 'debug_logging' in options else False
    BATTERY_DISCHARGE_RATE = options['battery_discharge_rate'] if 'battery_discharge_rate' in options else 2.5
    INSECURE_MQTT = options['insecure_mqtt'] if 'insecure_mqtt' in options else False
    REGION = options['region'] if 'region' in options else 1