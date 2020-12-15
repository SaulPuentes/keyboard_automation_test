import json
import time
from pykeyboard import PyKeyboard

k = PyKeyboard()

def input_scan(barcode):
  time.sleep(1)
  k.type_string(barcode)
  k.tap_key(k.enter_key)

def fill_box(boxcode):
  print(boxcode)
  input_scan(boxcode)
  time.sleep(1) # await until server get the data
  input_scan('H12D07010320')
  input_scan('K01K03050724')
  input_scan('D09D06030320')
  input_scan('S19E07080420')
  input_scan('T11E07090420')
  input_scan('BG1')
  input_scan('BASCULA')
  input_scan('K01K03080320')
  input_scan(boxcode)
  time.sleep(1) # await for completed animation


# To Create an Alt+Tab combo
k.press_key(k.alt_key)
k.tap_key(k.tab_key)
k.release_key(k.alt_key)

# Iterate over all boxes
with open('boxes.json') as json_file:
    data = json.load(json_file)
    for b in data['boxes']:
      fill_box(b['boxcode'])