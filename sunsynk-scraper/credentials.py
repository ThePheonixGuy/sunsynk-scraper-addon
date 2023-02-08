mqtt_username:str
mqtt_password:str
mqtt_broker:str
mqtt_port:int

sunsynk_email:str
sunsynk_password:str

my_plant_id = 0
bearer_token = ""

def set_values_from_options(options):
    global mqtt_username
    global mqtt_password
    global mqtt_broker
    global mqtt_port
    global sunsynk_email
    global sunsynk_password
    global my_plant_id
    global bearer_token

    mqtt_username = options['mqtt_username'] if 'mqtt_username' in options else ''
    mqtt_password = options['mqtt_password'] if 'mqtt_password' in options else ''
    mqtt_broker = options['mqtt_host'] if 'mqtt_host' in options else '127.0.0.1'
    mqtt_port = options['mqtt_port'] if 'mqtt_port' in options else 1883
    sunsynk_email = options['sunsynk_email'] if 'sunsynk_email' in options else ''
    sunsynk_password = options['sunsynk_password'] if 'sunsynk_password' in options else ''