import sys

### Data ###
floorList = [
    {'floor': '3E', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '3W', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '4E', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '4W', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '5E', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '5W', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '6E', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '6W', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '7E', 'cap': 0, 'RNs': 0, 'PCAs': 0, },
    {'floor': '7W', 'cap': 0, 'RNs': 0, 'PCAs': 0, }
    ]

### Functions ###
def main():
    print('#############################################')
    print('# Welcome to the Hospital Staffing Program! #')
    print('#############################################')
    # 1. Ask for starting input from user.
    #  -Number of extra Float RNs and PCAs.
    floatRnList = int(input('Enter how many float RNs are on tonight: '))
    #  -Cap for each floor.
    for i in range(len(floorList)):
        floorList[i]['cap'] = int(input(f'Enter RN cap for {floorList[i]["floor"]}: '))
    #  -CSV containing all floor expectations.
    CSVFolder = input('Enter the name of the CSV folder: ')
    #  -CSV containing all float expectations.
    # 2. Move staff where RNs and PCAs need to go.
    #  -Check floors for extra RNs.
    #  -Check floors for extra PCAs.
    #  -Move Floor RNs to appropriate floors.
    #  -Move Float RNs to appropriate floors.
    #  -Move Floor PCAs to appropriate floors.
    #  -Move Float PCAs to appropriate floors.
    # 3. Ask for changing input from user.
    changeFlag = input('Are there any changes to the staffing? (y/n): ')
    #  -Enter new cap for each floor.
    if changeFlag.lower() == 'y':
        for i in range(len(floorList)):
            floorList[i]['cap'] = int(input(f'Enter new RN cap for {floorList[i]["floor"]}: '))
    # 4. Export Excel/CSV file.


    for i in range(len(floorList)):
        print(f'Floor: {floorList[i]["floor"]}, Cap: {floorList[i]["cap"]}, RNs: {floorList[i]["RNs"]}, PCAs: {floorList[i]["PCAs"]}')

if __name__ == '__main__':
    sys.exit(main())