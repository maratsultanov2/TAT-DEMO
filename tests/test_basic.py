import sys
sys.path.append('..')
from src.tat_demo import coherence, parse_marker, ChunkCarousel
import numpy as np

def test_coherence():
    v1 = np.array([1,0,0])
    v2 = np.array([0,1,0])
    assert coherence(v1, v2) < 0.1
    print('✅ coherence тест пройден')

def test_marker():
    content, level = parse_marker('слово/')
    assert level == 1
    print('✅ marker тест пройден')

def test_carousel():
    c = ChunkCarousel()
    for i in range(15):
        c.add(f'x'*1000)
    assert len(c.chunks) == 10
    print('✅ carousel тест пройден')

if __name__ == '__main__':
    test_coherence()
    test_marker()
    test_carousel()
