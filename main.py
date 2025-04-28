import sys
import os
import pandas as pd
import utils.data as data
import utils.algorithm as alg

### Functions ###
def main():
    ### Data ###
    am_pm_flag = 'a'
    float_rn_list = 0
    float_pca_list = 0
    floor_list = [
        {'floor': '3e', 'capRN': 0, 'capPCA': 0, 'RN': 3, 'PCA': 2, 'eRN': 0, 'ePCA': 0},
        {'floor': '4w', 'capRN': 0, 'capPCA': 0, 'RN': 5, 'PCA': 2, 'eRN': 0, 'ePCA': 0},
        {'floor': '5e', 'capRN': 0, 'capPCA': 0, 'RN': 1, 'PCA': 2, 'eRN': 0, 'ePCA': 0},
        {'floor': '5t', 'capRN': 0, 'capPCA': 0, 'RN': 2, 'PCA': 1, 'eRN': 0, 'ePCA': 0},
        {'floor': '5w', 'capRN': 0, 'capPCA': 0, 'RN': 7, 'PCA': 2, 'eRN': 0, 'ePCA': 0},
        {'floor': '5t', 'capRN': 0, 'capPCA': 0, 'RN': 3, 'PCA': 2, 'eRN': 0, 'ePCA': 0},
        {'floor': '5w', 'capRN': 0, 'capPCA': 0, 'RN': 2, 'PCA': 3, 'eRN': 0, 'ePCA': 0},
        {'floor': '6e', 'capRN': 0, 'capPCA': 0, 'RN': 2, 'PCA': 4, 'eRN': 0, 'ePCA': 0},
        {'floor': '6t', 'capRN': 0, 'capPCA': 0, 'RN': 5, 'PCA': 2, 'eRN': 0, 'ePCA': 0},
        {'floor': '6W', 'capRN': 0, 'capPCA': 0, 'RN': 3, 'PCA': 1, 'eRN': 0, 'ePCA': 0},
        {'floor': '7h', 'capRN': 0, 'capPCA': 0, 'RN': 2, 'PCA': 1, 'eRN': 0, 'ePCA': 0},
        {'floor': '7t', 'capRN': 0, 'capPCA': 0, 'RN': 5, 'PCA': 1, 'eRN': 0, 'ePCA': 0},
        {'floor': '8h', 'capRN': 0, 'capPCA': 0, 'RN': 4, 'PCA': 4, 'eRN': 0, 'ePCA': 0},
        {'floor': '9f', 'capRN': 0, 'capPCA': 0, 'RN': 3, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': 'ptca', 'capRN': 0, 'capPCA': 0, 'RN': 4, 'PCA': 1, 'eRN': 0, 'ePCA': 0},
        {'floor': 'icut', 'capRN': 0, 'capPCA': 0, 'RN': 10, 'PCA': 1, 'eRN': 0, 'ePCA': 0},
        {'floor': 'sicu', 'capRN': 0, 'capPCA': 0, 'RN': 4, 'PCA': 1, 'eRN': 0, 'ePCA': 0},
        {'floor': 'nicu', 'capRN': 0, 'capPCA': 0, 'RN': 5, 'PCA': 0, 'eRN': 0, 'ePCA': 0}
        ]

    print('#############################################')
    print('# Welcome to the Hospital Staffing Program! #')
    print('#############################################')
    # 1. Ask for starting input from user.
    #  -Number of extra Float RNs and PCAs.
    # am_pm_flag = input('Is this for the AM or PM shift? (a/p): ')
    float_rn_list = int(input('Enter how many float RNs are on tonight: '))
    float_pca_list = int(input('Enter how many float PCAs are on tonight: '))
    #  -Cap for each floor.
    for i in range(len(floor_list)):
        print(f'\n[Floor --- {floor_list[i]["floor"]}]')
        floor_list[i]['capRN'] = int(input(f'Enter RN cap: '))
        floor_list[i]['capPCA'] = int(input(f'Enter PCA cap: '))
    #  -Dict containing all floor expectations.
    floor_stats = data.get_excel_sheets()
    # 2. update floorList with the number of RNs and PCAs on each floor based on caps.
    update_floor_list(floor_list, floor_stats)
    # 3. Move staff where RNs and PCAs need to go.
    alg.RN_algorythm(floor_list, float_rn_list)
    alg.PCA_algorythm(floor_list, float_pca_list)
    # 4. Ask for changing input from user.
    # change_flag = input('Are there any changes to the staffing? (y/n): ')
    #  -Enter new cap for each floor.
    # if change_flag.lower() == 'y':
    #     for i in range(len(floor_list)):
    #         floor_list[i]['cap'] = int(input(f'Enter new RN cap for {floor_list[i]["floor"]}: '))
    # 5. Export Excel/CSV file.
    # 6. Print results.
    print_results(floor_list, float_rn_list, float_pca_list)

def update_floor_list(floor_list, floor_stats):
    # 1. Update floors with current RNs and PCAs.
    for i in range(len(floor_list)):
        if floor_list[i]['RN'] > floor_list[i]['capRN']:
            # 2. Calculate extra RNs and PCAs.
            floor_list[i]['eRN'] = floor_list[i]['RN'] - floor_list[i]['capRN']
            if floor_list[i]['eRN'] > 0:
                floor_list[i]['RN'] -= floor_list[i]['eRN']
            floor_list[i]['ePCA'] = floor_list[i]['PCA'] - floor_list[i]['capPCA']
            if floor_list[i]['ePCA'] > 0:
                floor_list[i]['PCA'] -= floor_list[i]['ePCA']

def print_results(floor_list, float_rn_list, float_pca_list):
    print('\n=== Floor Plan ===')
    for i in range(len(floor_list)):
        print(f'Floor: {floor_list[i]["floor"]}, RN Cap: {floor_list[i]["capRN"]}, RNs: {floor_list[i]["RN"]}, PCA cap: {floor_list[i]["capPCA"]},  PCAs: {floor_list[i]["PCA"]}')
        if floor_list[i]['eRN'] > 0:
            print(f' - Extra RNs: {floor_list[i]["eRN"]}')
        if floor_list[i]['eRN'] < 0:
            print(f' - Need RNs: {floor_list[i]["eRN"]}')
        if floor_list[i]['ePCA'] > 0:
            print(f' - Extra PCAs: {floor_list[i]["ePCA"]}')
        if floor_list[i]['ePCA'] < 0:
            print(f' - Need PCAs: {floor_list[i]["ePCA"]}')
    print('===================')
    if float_rn_list > 0:
        print(f'Extra Float RNs: {float_rn_list}')
    if float_pca_list > 0:
        print(f'Extra Float PCAs: {float_pca_list}')

### Main function ###
if __name__ == '__main__':
    sys.exit(main())