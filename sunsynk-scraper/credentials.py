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

    mqtt_username = options['mqtt_username']
    mqtt_password = options['mqtt_password']
    mqtt_broker = options['mqtt_host']
    mqtt_port = options['mqtt_port']
    sunsynk_email = options['sunsynk_email']
    sunsynk_password = options['sunsynk_password']