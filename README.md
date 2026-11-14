ChrimsonR-Red-Shift-Data-Mining/
├── README.md                  # 项目主说明文档（见下文）
├── database/                  # 数据库部分
│   ├── schema.sql             # 建表 SQL 语句
│   └── data_import.py         # 用 Python (pandas + sqlalchemy) 将 Excel 导入 MySQL 的脚本
├── analysis/                  # 数据分析部分
│   ├── mutation_classifier.py # 正则表达式提取氨基酸突变并分类打标签
│   └── stats_analysis.py      # 统计分析（找出高频突变类型，生成统计结果）
└── structure/                 # 结构筛选部分
    └── pocket_screening.py    # 用 Biopython 计算发色团中心，筛选 6Å 范围内的残基

# ChrimsonR 突变数据挖掘与结构预测分析工具

本项目原为初三独立科研课题。旨在通过“数据挖掘+结构预测”的组合策略，为光敏蛋白 ChrimsonR 的光谱红移改造提供理性设计方案。

在此开源项目中，重点展示实现该科研目标所使用的**全流程 Python 自动化脚本与数据库构建技术**。

## 技术栈
- **数据存储**：MySQL (关系型数据库设计、主外键约束)
- **数据处理**：Python (Pandas, PyMySQL, 正则表达式)
- **结构计算**：Biopython, NumPy (KDTree 空间索引计算)

## 核心模块介绍

### 1. 数据库构建与数据导入 (`/database`)
- 设计了包含蛋白信息、突变位点、光谱数据的关联数据表。
- 使用 Pandas 读取收集到的突变数据 Excel 表格，批量写入 MySQL 数据库。

### 2. 文本解析与统计分析 (`/analysis`)
- 使用正则表达式解析突变字符串，利用字典映射将氨基酸转换为 4 大物理化学分类。
- 编写 SQL 聚合查询与 Python 数据统计，找出历史数据中成功率最高的突变方向。

### 3. 三维结构邻近残基筛选 (`/structure`)
- 自动解析 PDB 文件，计算视黄醛发色团的真实几何中心。
- 利用 `Bio.PDB.NeighborSearch` (KDTree) 高效检索 6Å 空间范围内的氨基酸残基，为后续定点突变提供靶点。

## 运行结果展示
见图片

## 作者
**[吴卓玥]** - 负责全部数据库搭建、Python 脚本编写与结构分析算法实现。
