import json
import random
import datetime
import boto3
import time
time.sleep(300)

devNames = ['WAT01', 'WAT02', 'WAT03', 'WAT04', 'WAT05', 'WAT06', 'WAT07', 'WAT08', 'WAT09', 'WAT10']

iot = boto3.client('iot-data');

# generate Volume values
def getVolumeValues():
    data = {}
    data['devValue'] = random.randint(10, 100)
    data['devParameter'] = 'Volume'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Temperature values
def getTemperatureValues():
    data = {}
    data['devValue'] = random.randint(35, 70)
    data['devParameter'] = 'Temperature'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Fluoride values
def getFluorideValues():
    data = {}
    data['devValue'] = random.randint(30, 99)
    data['devParameter'] = 'Fluoride'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Chlorine values
def getChlorineValues():
    data = {}
    data['devValue'] = random.randint(5, 50)
    data['devParameter'] = 'Chlorine'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Lead values
def getLeadValues():
    data = {}
    data['devValue'] = random.randint(1, 10)
    data['devParameter'] = 'Lead'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Selenium values
def getSeleniumValues():
    data = {}
    data['devValue'] = random.randint(1, 7)
    data['devParameter'] = 'Selenium'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Radium values
def getRadiumValues():
    data = {}
    data['devValue'] = random.randint(3, 9)
    data['devParameter'] = 'Radium'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Phosphate values
def getPhosphateValues():
    data = {}
    data['devValue'] = random.randint(2, 50)
    data['devParameter'] = 'Phosphate'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Arsenic values
def getArsenicValues():
    data = {}
    data['devValue'] = random.randint(1, 20)
    data['devParameter'] = 'Arsenic'
    data['devId'] = random.choice(devNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# Generate each parameter's data input in varying proportions
while True:
    time.sleep(1)
    rnd = random.random()
    if (0 <= rnd < 0.10):
        data = json.dumps(getVolumeValues())
        
        response = iot.publish(
             topic='/mb3/devdata/volume',
             payload=data
        )
    elif (0.10<= rnd < 0.20):
        data = json.dumps(getTemperatureValues())
        
        response = iot.publish(
             topic='/mb3/devdata/temperature',
             payload=data
        )
    elif (0.20<= rnd < 0.30):
        data = json.dumps(getFluorideValues())
        
        response = iot.publish(
             topic='/mb3/devdata/fluoride',
             payload=data
        )
    elif (0.30<= rnd < 0.40):
        data = json.dumps(getLeadValues())
        
        response = iot.publish(
             topic='/mb3/devdata/lead',
             payload=data
        )
    elif (0.40<= rnd < 0.50):
        data = json.dumps(getSeleniumValues())
        
        response = iot.publish(
             topic='/mb3/devdata/selenium',
             payload=data
        )
    elif (0.50<= rnd < 0.60):
        data = json.dumps(getRadiumValues())
        
        response = iot.publish(
             topic='/mb3/devdata/radium',
             payload=data
        )
    elif (0.60<= rnd < 0.70):
        data = json.dumps(getPhosphateValues())
        
        response = iot.publish(
             topic='/mb3/devdata/phosphate',
             payload=data
        )
    elif (0.70<= rnd < 0.80):
        data = json.dumps(getArsenicValues())
        
        response = iot.publish(
             topic='/mb3/devdata/arsenic',
             payload=data
        )
    else:
        data = json.dumps(getChlorineValues())
        
        response = iot.publish(
             topic='/mb3/devdata/chlorine',
             payload=data
)
