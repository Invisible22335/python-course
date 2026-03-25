import requests

city = input("Введите город: ")

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    "q": city,
    "units": "metric",
    "lang": "ru",
    "appid": "79d1ca96933b0328e1c7e3e7a26cb347"
}

weather_data = requests.get(url, params=params).json()

if weather_data.get("cod") == 200:
    temp_now = round(weather_data['main']['temp'])
    feels_now = round(weather_data['main']['feels_like'])
    press = weather_data['main']['pressure']
    wet = weather_data['main']['humidity']
    sky = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']

    print("Город:", city)
    print("Температура:", temp_now, "°C")
    print("Ощущается как:", feels_now, "°C")
    print("Давление:", press, "гПа")
    print("Влажность:", wet, "%")
    print("Погода:", sky)
    print("Ветер:", wind_speed, "м/с")

    if wind_speed < 5:
        print("Сообщение про ветер: ветер слабый")
    elif wind_speed < 10:
        print("Сообщение про ветер: ветер умеренный")
    else:
        print("Сообщение про ветер: ветер сильный")

else:
    print("Город не найден")