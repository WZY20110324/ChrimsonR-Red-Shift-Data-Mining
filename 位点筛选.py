from Bio.PDB import PDBParser, NeighborSearch
import numpy as np
parser = PDBParser(QUIET=True)
structure = parser.get_structure('chrimson', r'C:\Users\smeil\Downloads\5zih.pdb')
ret_atoms = []
for model in structure:
    for chain in model:
        for residue in chain:
            if residue.get_resname().strip() == 'LYR':
                for atom in residue:
                    atom_name = atom.get_name().strip()
                    if atom_name.startswith('C') and atom_name not in ('CA','CB','CG','CD','CE'):
                        ret_atoms.append(atom)
print(f"提取到 {len(ret_atoms)} 个视黄醛碳原子")
ret_coords = np.array([atom.get_coord() for atom in ret_atoms])
center = ret_coords.mean(axis=0)
print(f"视黄醛中心坐标: {center}")
all_atoms = []
for model in structure:
    for chain in model:
        for residue in chain:
            if residue.get_id()[0] == ' ':
                for atom in residue:
                    all_atoms.append(atom)
print(f"蛋白原子总数: {len(all_atoms)}")
ns = NeighborSearch(all_atoms)
nearby_residues = ns.search(center, 6.0, level='R')
print(f"\n6 Å范围内共找到 {len(nearby_residues)} 个残基：")
for res in nearby_residues:
    print(f"  {res.get_resname()}{res.get_id()[1]} (链 {res.get_parent().id})")
