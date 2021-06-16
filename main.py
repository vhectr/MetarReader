import PythonMETAR.metar
from PythonMETAR import Metar
from parse_data import parse_data

print("Vhectr MetarReader 1.0")
print("(c) 2021 Vhectr Software under the Apache License, Version 2.0")
print()

try:

    while True:
        print("[1] Fetch METAR from NOAA servers.")
        print("[2] Parse METAR data")
        print("[3] Fetch and parse METAR from NOAA servers.")
        print("[4] Exit")
        option = input()

        if option == "1":
            icao_code = input("Enter airport ICAO code: ")
            data = Metar(icao_code)
            print(data)

        if option == "2":
            icao_code = input("Enter ICAO code for METAR data: ")
            data = Metar(icao_code, input("Enter METAR data: "))
            print(parse_data(data))

        if option == "3":
            icao_code = input("Enter airport ICAO code: ")
            data = Metar(icao_code)
            print(parse_data(data))

        if option == "4":
            break


except PythonMETAR.metar.NOAAServError:
    print("METAR data not found for given ICAO code.")