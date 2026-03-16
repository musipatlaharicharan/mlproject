import json

path = r'c:\hraicharan\mlproject\src\EDA STUDENT PERFORMANCE .ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'source' in cell:
        if any('StudentsPerformance.csv' in s for s in cell['source']):
            cell['source'] = ["df=pd.read_csv('../stud.csv')\n", "df.head()"]
            cell['outputs'] = []
            if 'execution_count' in cell:
                cell['execution_count'] = None

with open(path, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(nb, f, indent=1)
