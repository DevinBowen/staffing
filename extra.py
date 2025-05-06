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

floor_list = [
        {'floor': '3East', 'cap': 0, 'capRN': 0, 'capPCA': 0, 'RN': 7, 'PCA': 4, 'eRN': 0, 'ePCA': 0},
        {'floor': '4West', 'cap': 0, 'capRN': 0, 'capPCA': 0, 'RN': 5, 'PCA': 2, 'eRN': 0, 'ePCA': 0},
        {'floor': '5East', 'cap': 0, 'capRN': 0, 'capPCA': 0, 'RN': 1, 'PCA': 1, 'eRN': 0, 'ePCA': 0}
    ]

def get_csv_files():
    folder_path = './csv/'
    all_dfs = []
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        all_dfs.append(df)
    for df in all_dfs:
        print(df)
    return all_dfs

def get_excel_sheets():
    file_path = './data/excel/Grids for Staffing Office.xlsx'
    try:
        import openpyxl
    except ImportError:
        print("❌ 'openpyxl' is not installed. Please run: pip install openpyxl")
        return {}

    sheet_names = pd.ExcelFile(file_path).sheet_names
    floor_to_df = {}

    for sheet_name in sheet_names:
        # Read the whole sheet
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # --- Find the floor/unit name ---
        floor_name = None
        for col in df.columns:
            for value in df[col].head(10):  # Look at first 10 rows
                if isinstance(value, str) and 'UNIT:' in value:
                    floor_name = value.split('UNIT:')[-1].strip()
                    break
            if floor_name:
                break

        if not floor_name:
            floor_name = sheet_name  # fallback

        # --- Clean the sheet ---
        try:
            df_clean = clean_excel_sheets(df)
            floor_to_df[floor_name] = df_clean
        except Exception as e:
            print(f"⚠️ Skipping sheet '{sheet_name}' because of error: {e}")
            continue

    print(f"Total number of sheets processed: {len(floor_to_df)}")  # Debug: Print total processed sheets
    return floor_to_df

def clean_excel_sheets(df):
    header_row_index = df[df.iloc[:, 1] == 'CENSUS'].index[0]
    df.columns = df.iloc[header_row_index]
    df = df.drop(index=list(range(0, header_row_index + 1)))
    df = df.dropna(how='all')
    df = df.reset_index(drop=True)
    return df

def update_caps(floor_list, floor_stats):
    for floor in floor_list:
        floor_name = floor['floor']
        df = floor_stats.get(floor_name)

        if df is None:
            print(f"⚠️ No data for floor '{floor_name}'")
            continue

        try:
            # Normalize column names
            df.columns = [str(col).strip().lower() for col in df.columns]

            # Rename columns for consistency
            census_col = next(col for col in df.columns if 'census' in col)
            rn_col = next(col for col in df.columns if 'rn' in col or 'lpn' in col)
            pca_col = next((col for col in df.columns if 'na' in col or 'uc' in col), None)

            # Convert to numeric for filtering
            df[census_col] = pd.to_numeric(df[census_col], errors='coerce')

            # Use the max census value as the cap
            max_census = df[census_col].max()
            floor['cap'] = int(max_census)

            # Get row where census matches cap
            matching_row = df[df[census_col] == max_census]

            if not matching_row.empty:
                floor['capRN'] = int(matching_row[rn_col].values[0])
                if pca_col:
                    floor['capPCA'] = int(matching_row[pca_col].values[0])
                else:
                    floor['capPCA'] = 0
            else:
                print(f"⚠️ No matching row for census {max_census} on floor {floor_name}")

            print(floor)

        except Exception as e:
            print(f"❌ Error processing floor {floor_name}: {e}")