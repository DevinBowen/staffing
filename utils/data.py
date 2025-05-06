import pandas as pd

def get_cap_data(am_pm_flag):
    floor_caps = {}
    file_path = "./data/excel/Grids for Staffing Office.xlsx"
    sheets = pd.read_excel(file_path, sheet_name=None, header=4)
    # print(sheets.keys())  # Debug: Print all sheet names

    for sheet in sheets:
        df = sheets[sheet]
        df = df.loc[:, ~df.columns.str.startswith('Unnamed')]

        df.loc[:, 'CENSUS'] = pd.to_numeric(df['CENSUS'], errors='coerce')
        df = df[df['CENSUS'] > 0]
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df.round(0).astype("Int64")

        if am_pm_flag == 'am':
            am_cols = df.columns[1:6]
            df = df[['CENSUS'] + list(am_cols)].copy()
        elif am_pm_flag == 'pm':
            pm_cols = df.columns[6:]
            df = df[['CENSUS'] + list(pm_cols)].copy()

        floor_caps[sheet] = df
        # print(floor_caps[sheet])
    return floor_caps

def update_caps(floor_list, floor_caps):
    # print('- in update_caps -')
    for floor in floor_list:
        df = floor_caps[floor['floor']]
        # print(df)
        cap = floor['cap']
        if cap == 0:
            continue
        # print(f'Floor: {floor["floor"]}')
        # print(floor_caps[floor['floor']])

        cn_col = df.filter(like='CN', axis=1).columns[0]
        rnlpn_col = df.filter(like='RN/ LPN', axis=1).columns[0]
        pca_col = df.filter(like='NA', axis=1).columns[0]

        CN = df.loc[df['CENSUS'] == cap, cn_col].values[0]
        RNLPN = df.loc[df['CENSUS'] == cap, rnlpn_col].values[0]
        PCA = df.loc[df['CENSUS'] == cap, pca_col].values[0]

        floor['capRN'] = int(CN + RNLPN)
        floor['capPCA'] = int(PCA)

        # print(floor)
    return floor_list

def update_floor_list(floor_list):
    # print('- in update_floor_list -')
    for floor in floor_list:
        floor['eRN'] = floor['RN'] - floor['capRN']
        if floor['eRN'] > 0:
            floor['RN'] -= floor['eRN']
        floor['ePCA'] = floor['PCA'] - floor['capPCA']
        if floor['ePCA'] > 0:
            floor['PCA'] -= floor['ePCA']
        # print(f'Floor: {floor["floor"]}')
        # print(floor)

    return floor_list