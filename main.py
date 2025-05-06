import sys
import os
import pandas as pd
import utils.data as data
import utils.algorithm as alg

def main():
    floor_list = [
        {'floor': '3East', 'cap': 0, 'capRN': 0, 'capPCA': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '4West', 'cap': 0, 'capRN': 0, 'capPCA': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0},
        {'floor': '5East', 'cap': 0, 'capRN': 0, 'capPCA': 0, 'RN': 0, 'PCA': 0, 'eRN': 0, 'ePCA': 0}
    ]

    print('#############################################')
    print('# Welcome to the Hospital Staffing Program! #')
    print('#############################################')
    # 1. Initial input retrieval
    am_pm_flag = input('\nIs this for the AM or PM shift? (am/pm): ').lower()
    float_rn_count = int(input('\nEnter how many float RNs are on tonight: '))
    float_pca_count = int(input('Enter how many float PCAs are on tonight: '))
    for floor in floor_list:
        print(f'\n[Floor --- {floor['floor']}]')
        floor['cap'] = int(input('Enter floor cap: '))
        floor['RN'] = int(input('Enter number of RNs: '))
        floor['PCA'] = int(input('Enter number of PCAs: '))
    floor_caps = data.get_cap_data(am_pm_flag)

    # 2. Processing data
    data.update_caps(floor_list, floor_caps)
    data.update_floor_list(floor_list)
    floor_list, float_rn_count = alg.RN_algorithm(floor_list, float_rn_count)
    floor_list, float_pca_count = alg.PCA_algorithm(floor_list, float_pca_count)

    # 4. Update if changes
    # change_flag = input('Are there any changes to the staffing? (y/n): ')
    #  -Enter new cap for each floor.
    # if change_flag.lower() == 'y':
    #     for i in range(len(floor_list)):
    #         floor_list[i]['cap'] = int(input(f'Enter new RN cap for {floor_list[i]["floor"]}: '))
    # 5. Export Excel/CSV file.

    print_results(floor_list, float_rn_count, float_pca_count)

def print_results(floor_list, float_rn_count, float_pca_count):
    print('\n\n#############################################')
    print('#               Hospital plan               #')
    print('#############################################')
    for i in range(len(floor_list)):
        print(f'\nFloor: {floor_list[i]["floor"]}, RN Cap: {floor_list[i]["capRN"]}, RNs: {floor_list[i]["RN"]}, PCA cap: {floor_list[i]["capPCA"]},  PCAs: {floor_list[i]["PCA"]}')
        if floor_list[i]['eRN'] > 0:
            print(f' - Extra RNs: {floor_list[i]["eRN"]}')
        if floor_list[i]['eRN'] < 0:
            print(f' - Need RNs: {abs(floor_list[i]["eRN"])}')
        if floor_list[i]['ePCA'] > 0:
            print(f' - Extra PCAs: {floor_list[i]["ePCA"]}')
        if floor_list[i]['ePCA'] < 0:
            print(f' - Need PCAs: {abs(floor_list[i]["ePCA"])}')
    print('\n   [========================================]\n')
    if float_rn_count > 0:
        print(f'Extra Float RNs: {float_rn_count}')
    if float_pca_count > 0:
        print(f'Extra Float PCAs: {float_pca_count}')
    print('\n#############################################')
    print('#                                           #')
    print('#############################################')

### Main function ###
if __name__ == '__main__':
    sys.exit(main())