
# IOT using MQTT, Python and Node-Red for Jetson Nano/Raspberry Pi

A Python program whcih subscribes to a topic of a MQTT broker and outputs to GPIO  pinout of Jetson Nano or Raspberry.

## Tech Stack
- [Node Red](https://nodered.org/)
- [Paho MQTT Python library](https://github.com/eclipse/paho.mqtt.python)
- [Demonstration YouTube Video](https://youtu.be/WPmzoYwXj00)


## Run Locally

Clone the project

```bash
  git clone https://github.com/AshutoshGeek/MQTT-Python-Jetson-Nano.git
```

Go to the project directory

```bash
  cd MQTT-Python-Jetson-Nano
```

Install dependencies

```bash
  sudo pip3 install paho-mqtt
```

Run the code

```bash
  python3 mqtt_gpio.py
```

  