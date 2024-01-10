import datetime

login_endpoint_1 = ('https://pv.inteless.com/oauth/token')
plants_endpoint_1 = ('https://pv.inteless.com/api/v1/plants?page=1&limit=10&name=&status=')
energy_base_url_1 = "https://pv.inteless.com/api/v1/plant/energy/"

login_endpoint_2 = ('https://api.sunsynk.net/oauth/token')
plants_endpoint_2 = ('https://api.sunsynk.net/api/v1/plants?page=1&limit=10&name=&status=')
energy_base_url_2 = "https://api.sunsynk.net/api/v1/plant/energy/"

flow_chart_endpoint = "flow"
day_readings_endpoint = "day?lan=en"
month_readings_endpoint = "month?lan=en"

def get_flow_chart_endpoint(plant_id, date: datetime.date):
    energy_base_url = energy_base_url_1 if REGION == 1 else energy_base_url_2
    return f'{energy_base_url}{plant_id}/{flow_chart_endpoint}?date={date.strftime("%Y-%m-%d")}'

def get_day_readings_endpoint(plant_id, date: datetime.date):
    energy_base_url = energy_base_url_1 if REGION == 1 else energy_base_url_2
    return f'{energy_base_url}{plant_id}/{day_readings_endpoint}&date={date.strftime("%Y-%m-%d")}'

def get_month_readings_endpoint(plant_id, date):
    energy_base_url = energy_base_url_1 if REGION == 1 else energy_base_url_2
    return f'{energy_base_url}{plant_id}/{month_readings_endpoint}&date={date.strftime("%Y-%m")}&id={plant_id}'

def get_login_endpoint():
    login_endpoint = login_endpoint_1 if REGION == 1 else login_endpoint_2
    return login_endpoint

def get_plants_endpoint():
    plants_endpoint = plants_endpoint_1 if REGION == 1 else plant_endpoint_2
    return plants_endpoint
