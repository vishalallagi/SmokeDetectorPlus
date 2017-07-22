#!usr/bin/python

from sense_hat import SenseHat
import Rpi.GPIO as gpio

HUMIDITYMAX = 255
HUMIDITYMIN = 0

TRIGGER = 4

def SetTriggerPin():
  gpio.setmode(gpio.BOARD)
  gpio.setup(TRIGGER, gpio.IN)

def ReadTriggerPin():
  return gpio.input(TRIGGER)

def SenseHatFireAlarmInd():
  #Turn LEDs ON to indicate fire alarm pattern
  a = 0

def SenseHatHumidityInd(humidity):
  #Turn LEDs ON to indicate Humidity indication
  humidity = 0
  
def ReadSenseHatInfo():
  #Read sensors information and return as a list to the caller
  return 1

def BluetoothInd():
  #Send information to BLE device
  status = False
  return status

def AudioInd(audio):
  #Send information via audio device
  audio = False

if __name__ == '__main__':
  while True:
    if ReadTriggerPin():
      SenseHatFireAlarmInd()
      BluetoothInd()
      AudioInd()
    if humidity < HUMIDITYMAX:
      SenseHatHumidityInd()
      AudioInd()
