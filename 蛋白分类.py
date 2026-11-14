import pymysql
import re
aa_class = {
    'G': '非极性的脂肪族', 'A': '非极性的脂肪族', 'V': '非极性的脂肪族',
    'L': '非极性的脂肪族', 'I': '非极性的脂肪族', 'P': '非极性的脂肪族',
    'S': '不带电荷的极性', 'T': '不带电荷的极性', 'C': '不带电荷的极性',
    'M': '不带电荷的极性', 'N': '不带电荷的极性', 'Q': '不带电荷的极性',
    'F': '芳香族', 'Y': '芳香族', 'W': '芳香族',
    'D': '带电荷的极性', 'E': '带电荷的极性', 'U': '带电荷的极性',
    'H': '带电荷的极性', 'R': '带电荷的极性', 'K': '带电荷的极性', 'O': '带电荷的极性'
}
pattern = re.compile(r'([A-Z])(\d+)([A-Z])')
def classify_mutation(mut_str):
    if not mut_str or mut_str.strip() in ('', '/', 'None'):
        return '无突变'
    found = pattern.findall(mut_str)
    if not found:
        return '非标准突变'
    labels = []
    for wt, pos, mt in found:
        wt_class = aa_class.get(wt, '未知')
        mt_class = aa_class.get(mt, '未知')
        labels.append(f"{wt_class}→{mt_class}")
    
    return '；'.join(labels)
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Tsinghua University High School",
    database="protein",
    charset='utf8mb4'
)
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s" % data)
cursor.execute("SELECT id,mutation_sites,tag_type FROM red_shift_proteins")
rows = cursor.fetchall()
for (id_val, mut_str, old_tag) in rows:
    category = classify_mutation(mut_str)
    cursor.execute(
        "UPDATE red_shift_proteins SET tag_type = %s WHERE id = %s",
        (category, id_val)
    )
conn.commit()
print("分类更新完成！")
cursor.execute("SELECT id, mutation_sites, tag_type FROM red_shift_proteins LIMIT 10")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, 突变: {row[1]}, 类别: {row[2]}")
cursor.close()
conn.close()
