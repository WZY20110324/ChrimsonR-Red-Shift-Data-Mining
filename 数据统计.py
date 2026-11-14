import pymysql
from collections import Counter
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Tsinghua University High School",
    database="protein",
    charset='utf8mb4'
)
cursor = conn.cursor()
cursor.execute("SELECT tag_type FROM red_shift_proteins WHERE tag_type NOT IN ('无突变', '非标准突变')")
rows = cursor.fetchall()
all_mutations = []
for (tag,) in rows:
    if tag:
        items = tag.split('；')
        all_mutations.extend(items)
counter = Counter(all_mutations)
print(f"共发现 {len(counter)} 种不同的突变类型。")
print("所有突变类型出现次数（从高到低）：")
for item, count in counter.most_common():
    print(f"{item} ： {count} 次")
conn.close()
