UPDATE_INTERVAL = 5
DEBUG_LOGGING = True
BATTERY_DISCHARGE_RATE = 2.5
BATTERY_MINIMUM_SOC = 15
INSECURE_MQTT = False

def set_values_from_options(options):
    global UPDATE_INTERVAL
    global DEBUG_LOGGING
    global BATTERY_DISCHARGE_RATE
    global INSECURE_MQTT

    UPDATE_INTERVAL = options['update_interval']
    DEBUG_LOGGING = options['debug_logging']
    BATTERY_DISCHARGE_RATE = options['battery_discharge_rate']
    INSECURE_MQTT = options['insecure_mqtt']