import xml.etree.ElementTree as ET
import sqlite3

class PartyAnimal:
    x = 0
    def __init__(self):
        print('I am Constructor')
    def _party_(self):
        self.x = self.x + 1
        print('So far:',self.x)
    def __del__(self):
        print('I am Destructor')
pa = PartyAnimal()
pa._party_();
pa._party_();
pa._party_();

pa = 55

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
print(dir(cur))
