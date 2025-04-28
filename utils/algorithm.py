def RN_algorythm(floor_list, float_rn_list):
    print('Processing RN algorithm...')
    # 1. Move Floor RNs to appropriate floors.
    for floor in floor_list:
        if floor['eRN'] == 0:
            continue
        if floor['eRN'] < 0:
            for extra in floor_list:
                if floor['eRN'] == 0:
                    break
                if extra['eRN'] > 0:
                    floor['RN'] -=floor['eRN']
                    extra['eRN'] += floor['eRN']
    # 2. Move Float RNs to appropriate floors.
    for floor in floor_list:
        if floor['eRN'] < 0 and float_rn_list > floor['eRN']:
            floor['RN'] -= floor['eRN']
            float_rn_list += floor['eRN']
    return floor_list, float_rn_list

def PCA_algorythm(floor_list, float_pca_list):
    print('Processing PCA algorithm...')
    # 1. Move Floor RNs to appropriate floors.
    for floor in floor_list:
        if floor['ePCA'] == 0:
            continue
        if floor['ePCA'] < 0:
            for extra in floor_list:
                if floor['ePCA'] == 0:
                    break
                if extra['ePCA'] > 0:
                    floor['PCA'] -=floor['ePCA']
                    extra['ePCA'] += floor['ePCA']
    # 2. Move Float RNs to appropriate floors.
    for floor in floor_list:
        if floor['ePCA'] < 0 and float_pca_list > floor['ePCA']:
            floor['PCA'] -= floor['ePCA']
            float_pca_list += floor['ePCA']
    return floor_list, float_pca_list