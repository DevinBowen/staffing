import sys
import os
import pandas as pd

### Functions ###
def main():
    ### Data ###
    floor_list = [
        {'floor': '3E', 'cap': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '3W', 'cap': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '4E', 'cap': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '4W', 'cap': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '5E', 'cap': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '5W', 'cap': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '6E', 'cap': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '6W', 'cap': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0}
        ]

    print('#############################################')
    print('# Welcome to the Hospital Staffing Program! #')
    print('#############################################')
    # 1. Ask for starting input from user.
    #  -Number of extra Float RNs and PCAs.
    float_rn_list = int(input('Enter how many float RNs are on tonight: '))
    float_pca_list = int(input('Enter how many float PCAs are on tonight: '))
    #  -Cap for each floor.
    for i in range(len(floor_list)):
        floor_list[i]['cap'] = int(input(f'Enter RN cap for {floor_list[i]["floor"]}: '))
    #  -CSVs containing all floor expectations.
    floor_stats = get_csv_files()
    # 2. update floorList with the number of RNs and PCAs on each floor based on caps.
    update_floor_list(floor_list, floor_stats)
    # 3. Move staff where RNs and PCAs need to go.
    RN_algorythm(floor_list, float_rn_list)
    PCA_algorythm(floor_list, float_pca_list)
    # 4. Ask for changing input from user.
    change_flag = input('Are there any changes to the staffing? (y/n): ')
    #  -Enter new cap for each floor.
    if change_flag.lower() == 'y':
        for i in range(len(floor_list)):
            floor_list[i]['cap'] = int(input(f'Enter new RN cap for {floor_list[i]["floor"]}: '))
    # 5. Export Excel/CSV file.
    for i in range(len(floor_list)):
        print(f'Floor: {floor_list[i]["floor"]}, Cap: {floor_list[i]["cap"]}, RNs: {floor_list[i]["RNs"]}, PCAs: {floor_list[i]["PCAs"]}')

def get_csv_files():
    folder_path = './csv/'
    all_dfs = []
    csv_folder = input('Enter the name of the CSV folder: ')
    csv_files = [f for f in os.listdir(folder_path+csv_folder) if f.endswith('.csv')]
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        all_dfs.append(df)
    for df in all_dfs:
        print(df)
    return all_dfs

def update_floor_list(floor_list, floor_stats):
    # 1. Update floors with current RNs and PCAs.
    for i in range(len(floor_list)):
        if floor_list[i]['RNs'] > floor_list[i]['cap']:
            # 2. Calculate extra RNs and PCAs.
            # floor_list[i]['RNs']
            # return
            print('function not finished')

def RN_algorythm(floor_list, float_rn_list):
    # 1. Move Floor RNs to appropriate floors.
    # 2. Move Float RNs to appropriate floors.
    print('function not finished')

def PCA_algorythm(floor_list, float_pca_list):
    # 1. Move Floor PCAs to appropriate floors.
    # 2. Move Float PCAs to appropriate floors.
    print('function not finished')

### Main function ###
if __name__ == '__main__':
    sys.exit(main())