import sys
sys.path.append('..')
from src.tat_demo import mitosis
chunk = 'A'*60000
print(f'Митоз: {len(mitosis(chunk))} чанка')
