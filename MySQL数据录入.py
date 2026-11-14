import pandas as pd
from sqlalchemy import create_engine
EXCEL_FILE = r'D:/red_shift_proteins.xlsx'
DB_PASSWORD = 'Tsinghua University High School'
DB_NAME = 'protein'
TABLE_NAME = 'red_shift_proteins'
df = pd.read_excel(EXCEL_FILE, sheet_name=0, header=0)
print(f"从 Excel 读取到 {len(df)} 行数据")
df.columns = df.columns.str.strip()
table_columns = ['protein_name', 'original_sequence', 'mutation_sites', 'search_name', 
                 'red_shift_nm', 'parent_protein', 'emission_wavelength', 'excitation_wavelength',
                 'shift_type', 'reference', 'remarks', 'tag_type']
if 'tag_type' not in df.columns:
    df['tag_type'] = None
df = df[table_columns]

print("映射后的列名：", df.columns.tolist())
engine = create_engine(
    f'mysql+pymysql://root:{DB_PASSWORD}@localhost/{DB_NAME}?charset=utf8mb4'
)
df.to_sql(
    TABLE_NAME,
    con=engine,
    if_exists='append',
    index=False,
    chunksize=100
)

print("✅ Excel 数据导入 MySQL 成功！")
