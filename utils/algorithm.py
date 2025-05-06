def RN_algorithm(floor_list, float_rn_count):
    print('\nProcessing RN algorithm...')
    for floor in floor_list:
        if floor['eRN'] >= 0:
            continue
        for extra in floor_list:
            if floor['RN'] == floor['capRN']:
                        break
            elif extra['eRN'] == 0:
                continue
            elif extra['eRN'] > 0:
                for _ in range(extra['eRN']):
                    if floor['RN'] == floor['capRN']:
                        break
                    floor['RN'] += 1
                    floor['eRN'] += 1
                    extra['eRN'] -= 1
        for _ in range(float_rn_count):
            if floor['RN'] == floor['capRN']:
                break
            floor['RN'] += 1
            float_rn_count -= 1

    return floor_list, float_rn_count

def PCA_algorithm(floor_list, float_pca_count):
    print('\nProcessing PCA algorithm...')
    for floor in floor_list:
        if floor['ePCA'] >= 0:
            continue
        for extra in floor_list:
            if floor['PCA'] == floor['capPCA']:
                        break
            elif extra['ePCA'] == 0:
                continue
            elif extra['ePCA'] > 0:
                for _ in range(extra['ePCA']):
                    if floor['PCA'] == floor['capPCA']:
                        break
                    floor['PCA'] += 1
                    floor['ePCA'] += 1
                    extra['ePCA'] -= 1
        for _ in range(float_pca_count):
            if floor['PCA'] == floor['capPCA']:
                break
            floor['PCA'] += 1
            float_pca_count -= 1

    return floor_list, float_pca_count