import network
import urequests as requests
from machine import Pin
from dht import DHT11
from time import sleep

wifi_ssid = "YOUR_WIFI_SSID"
wifi_password = "YOUR_WIFI_PASSWORD"
webhook_url = "https://maker.ifttt.com/trigger/esp32/with/key/YOUR_IFTTT_KEY"


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_password)
while not sta_if.isconnected():
    print(".", end = "")

dht11 = DHT11(Pin(15))

while True:
    dht11.measure()
    temperature = dht11.temperature()
    humidity = dht11.humidity()
    url = webhook_url + "?value1=" +  str(temperature) + "&value2=" + str(humidity)
    try:
        r = requests.get(url)
        print(r.text)
    except Exception as e:
        print(e)
    sleep(300)