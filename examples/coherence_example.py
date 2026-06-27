import sys
sys.path.append('..')
from src.tat_demo import coherence
import numpy as np
v1 = np.array([1,0,0])
v2 = np.array([0,1,0])
print(f'Когеренция: {coherence(v1, v2):.3f}')
