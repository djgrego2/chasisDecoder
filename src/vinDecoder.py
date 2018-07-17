import time
import requests
start_time = time.time()

def removeNone(s):
    if s is None or s is '':
        return 'NULL'
    return str(s)

with open("listaVin.txt", "r") as ins:
    listaVin = []
    for line in ins:
        listaVin.append(line)

    with open("datosVinPrueba.txt", "a") as fileHeader:
        fileHeader.write(
            "No.|VIN|Destination Market|Make|Manufacturer Name|Model|Model Year|Plant City|Series|Trim|Vehicle Type|Plant Country|Plant Company Name|Plant State|Manufacturer Id|Body Class|Doors|Windows|Transmission Style|Transmission Speeds|Brake System Type|Engine Number of Cylinders|Displacement (CC)|Displacement (CI)|Displacement (L)|Engine Model|Engine Power (KW)|Fuel Type - Primary|Valve Train Design|Fuel Type - Secondary|Fuel Delivery / Fuel Injection Type|Engine Brake (hp)|Park Assist|NCSA Body Type|NCSA Make|NCSA Model")
        fileHeader.write("\n")

    listaDatos = []

    try:
        for counter in range(0, len(listaVin)):
            lista = listaVin[counter].rstrip()

            r = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvaluesextended/" + lista + "?format=json")
            data = r.json()

            VIN = removeNone(data['Results'][0]['VIN']).split(',')
            DestinationM = removeNone(data['Results'][0]['DestinationMarket']).split(',')
            Make = removeNone(data['Results'][0]['Make']).split(',')
            ManufacturerN = removeNone(data['Results'][0]['Manufacturer'])
            Model = removeNone(data['Results'][0]['Model']).split(',')
            ModelY = removeNone(data['Results'][0]['ModelYear']).split(',')
            PlantCity = removeNone(data['Results'][0]['PlantCity']).split(',')
            Series = removeNone(data['Results'][0]['Series']).split(',')
            Trim = removeNone(data['Results'][0]['Trim']).split(',')
            VehicleType = removeNone(data['Results'][0]['VehicleType']).split(',')
            PlantCountry = removeNone(data['Results'][0]['PlantCountry']).split(',')
            PlantCompany = removeNone(data['Results'][0]['PlantCompanyName']).split(',')
            PlantState = removeNone(data['Results'][0]['PlantState']).split(',')
            ManufacturerId = removeNone(data['Results'][0]['ManufacturerId']).split(',')
            BodyClass = removeNone(data['Results'][0]['BodyClass']).split(',')
            Doors = removeNone(data['Results'][0]['Doors']).split(',')
            Windows = removeNone(data['Results'][0]['Windows']).split(',')
            TransmissionStyle = removeNone(data['Results'][0]['TransmissionStyle']).split(',')
            TransmissionSpeeds = removeNone(data['Results'][0]['TransmissionSpeeds']).split(',')
            BrakeSystemT = removeNone(data['Results'][0]['BrakeSystemType']).split(',')
            EngineNumberC = removeNone(data['Results'][0]['EngineCylinders']).split(',')
            DisplacementCC = removeNone(data['Results'][0]['DisplacementCC']).split(',')
            DisplacementCI = removeNone(data['Results'][0]['DisplacementCI']).split(',')
            DisplacementL = removeNone(data['Results'][0]['DisplacementL']).split(',')
            EngineModel = removeNone(data['Results'][0]['EngineModel']).split(',')
            EnginePowerKW = removeNone(data['Results'][0]['EngineKW']).split(',')
            FuelTypePrimary = removeNone(data['Results'][0]['FuelTypePrimary']).split(',')
            ValveTrainDesign = removeNone(data['Results'][0]['ValveTrainDesign']).split(',')
            FuelTypeSecondary = removeNone(data['Results'][0]['FuelTypeSecondary']).split(',')
            FuelDelivery = removeNone(data['Results'][0]['FuelInjectionType']).split(',')
            EngineBrakeHP = removeNone(data['Results'][0]['EngineHP']).split(',')
            ParkAssist = removeNone(data['Results'][0]['ParkAssist']).split(',')
            NCSABody = removeNone(data['Results'][0]['NCSABodyType']).split(',')
            NCSAMake = removeNone(data['Results'][0]['NCSAMake']).split(',')
            NCSAModel = removeNone(data['Results'][0]['NCSAModel']).split(',')

            #listaDatos.append("|"+VIN[0]+"|" + DestinationM[0]+"|" + Make[0]+"|" + ManufacturerN+"|" + Model[0]+"|" + ModelY[0]+"|" + PlantCity[0]+"|" + Series[0]+"|" + Trim[0]+"|" + VehicleType[0]+"|" + PlantCountry[0]
                               #+"|" + PlantCompany[0]+"|" + PlantState[0]+"|" + ManufacturerId[0]+"|" + BodyClass[0]+"|" + Doors[0]+"|" + Windows[0]+"|" + TransmissionStyle[0]+"|" + TransmissionSpeeds[0]
                               #+"|" + BrakeSystemT[0]+"|" + EngineNumberC[0]+"|" + DisplacementCC[0]+"|" + DisplacementCI[0]+"|" + DisplacementL[0]+"|" + EngineModel[0]+"|" + EnginePowerKW[0]+"|" + FuelTypePrimary[0]
                               #+"|" + ValveTrainDesign[0]+"|" + FuelTypeSecondary[0]+"|" + FuelDelivery[0]+"|" + EngineBrakeHP[0]+"|" + ParkAssist[0]+"|" + NCSABody[0]+"|" + NCSAMake[0]+"|" + NCSAModel[0])

            with open("datosVinPrueba.txt", "a") as filePrueba:

                    filePrueba.write(str(counter))
                    filePrueba.write("|"+VIN[0])
                    filePrueba.write("|"+DestinationM[0])
                    filePrueba.write("|"+Make[0])
                    filePrueba.write("|"+ManufacturerN)
                    filePrueba.write("|"+Model[0])
                    filePrueba.write("|"+ModelY[0])
                    filePrueba.write("|"+PlantCity[0])
                    filePrueba.write("|"+Series[0])
                    filePrueba.write("|"+Trim[0])
                    filePrueba.write("|"+VehicleType[0])
                    filePrueba.write("|"+PlantCountry[0])
                    filePrueba.write("|"+PlantCompany[0])
                    filePrueba.write("|"+PlantState[0])
                    filePrueba.write("|"+ManufacturerId[0])
                    filePrueba.write("|"+BodyClass[0])
                    filePrueba.write("|"+Doors[0])
                    filePrueba.write("|"+Windows[0])
                    filePrueba.write("|"+TransmissionStyle[0])
                    filePrueba.write("|"+TransmissionSpeeds[0])
                    filePrueba.write("|"+BrakeSystemT[0])
                    filePrueba.write("|"+EngineNumberC[0])
                    filePrueba.write("|"+DisplacementCC[0])
                    filePrueba.write("|"+DisplacementCI[0])
                    filePrueba.write("|"+DisplacementL[0])
                    filePrueba.write("|"+EngineModel[0])
                    filePrueba.write("|"+EnginePowerKW[0])
                    filePrueba.write("|"+FuelTypePrimary[0])
                    filePrueba.write("|"+ValveTrainDesign[0])
                    filePrueba.write("|"+FuelTypeSecondary[0])
                    filePrueba.write("|"+FuelDelivery[0])
                    filePrueba.write("|"+EngineBrakeHP[0])
                    filePrueba.write("|"+ParkAssist[0])
                    filePrueba.write("|"+NCSABody[0])
                    filePrueba.write("|"+NCSAMake[0])
                    filePrueba.write("|"+NCSAModel[0])

                    filePrueba.write("\n")
                    print("Agregando al txt -- " + str(counter))

            #time.sleep(0.5)

    except Exception:
        print("Error " + listaVin[counter])
        pass

print(len(listaDatos))

print("Time elapsed: {:.2f}s".format(time.time() - start_time))
print("Completo un total de: " + str(counter +1) + " VIN")
print("El ultimo VIN decodificado fue: " + listaVin[counter])