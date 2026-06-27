import sys
sys.path.append('..')
from src.tat_demo import parse_marker
for ex in ['слово/', 'фраза//', 'предложение///']:
    content, level = parse_marker(ex)
    print(f'{ex} → уровень {level}')
