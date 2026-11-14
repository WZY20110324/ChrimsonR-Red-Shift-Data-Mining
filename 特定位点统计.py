import pymysql
import re
from collections import defaultdict, Counter
aa_class = {
    'G': '非极性的脂肪族', 'A': '非极性的脂肪族', 'V': '非极性的脂肪族',
    'L': '非极性的脂肪族', 'I': '非极性的脂肪族', 'P': '非极性的脂肪族',
    'S': '不带电荷的极性', 'T': '不带电荷的极性', 'C': '不带电荷的极性',
    'M': '不带电荷的极性', 'N': '不带电荷的极性', 'Q': '不带电荷的极性',
    'F': '芳香族', 'Y': '芳香族', 'W': '芳香族',
    'D': '带电荷的极性', 'E': '带电荷的极性', 'U': '带电荷的极性',
    'H': '带电荷的极性', 'R': '带电荷的极性', 'K': '带电荷的极性', 'O': '带电荷的极性'
}
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Tsinghua University High School",
    database="protein",
    charset='utf8mb4'
)
cursor = conn.cursor()
cursor.execute("SELECT mutation_sites FROM red_shift_proteins")
rows = cursor.fetchall()
pattern = re.compile(r'([A-Z])(\d+)([A-Z])')
target_wt = {'L', 'I', 'V'}
stats = {aa: Counter() for aa in target_wt}
for (mut_str,) in rows:
    if not mut_str:
        continue
    found = pattern.findall(mut_str)
    for wt, pos, mt in found:
        if wt in target_wt:
            stats[wt][mt] += 1
print("=" * 50)
print("针对 L、I、V 的突变倾向统计")
print("=" * 50)
for wt in ['L', 'I', 'V']:
    print(f"\n【起点氨基酸 {wt}】（分类：{aa_class.get(wt, '未知')}）")
    if not stats[wt]:
        print("  数据库中未找到该氨基酸作为起点的突变记录")
        continue
    for mt, count in stats[wt].most_common():
        mt_class = aa_class.get(mt, '未知')
        print(f"   → 突变为 {mt}（{mt_class}）: {count} 次")
total_counter = Counter()
for mut_str, in rows:
    if not mut_str:
        continue
    found = pattern.findall(mut_str)
    for wt, pos, mt in found:
        if wt in target_wt:
            total_counter[mt] += 1
print("\n" + "=" * 50)
print("L、I、V 整体最常见的突变目标 TOP 10")
print("=" * 50)
for mt, count in total_counter.most_common(10):
    mt_class = aa_class.get(mt, '未知')
    print(f"  → {mt}（{mt_class}）: {count} 次")
conn.close()
