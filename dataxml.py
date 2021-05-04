import time
import xml.etree.ElementTree as ET
import sqlite3


def new_mesure(temperature: str, pression: str, altitude: str):
    tree = ET.parse("data.xml")
    root = tree.getroot()
    new = ET.SubElement(root, "mesure", attrib={"timestamp": str(time.time()),
                                                "temperature": str(temperature),
                                                "pression": str(pression),
                                                "altitude": str(altitude)})
    tree = ET.ElementTree(root)
    tree.write("data.xml")


def to_db():
    tree = ET.parse("data.xml")
    root = tree.getroot()

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    for child in root:
        print(child.attrib)
        cursor.execute("INSERT INTO mesures(timestamp, temperature, pression, altitude) VALUES(?, ?, ?, ?)", (
            child.attrib["timestamp"],
            child.attrib["temperature"],
            child.attrib["pression"],
            child.attrib["altitude"]
        ))

    conn.commit()
    with open("data.xml", 'w') as f:
        f.write("<data></data>")
