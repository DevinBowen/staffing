import os
import pandas as pd

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