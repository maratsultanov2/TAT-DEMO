# ============================================================
# TAT-DEMO: базовые механизмы
# ============================================================
import numpy as np

THETA = 1.987

def coherence(v1, v2, theta=THETA):
    c1 = v1 + 1j * (v1 * np.sin(theta))
    c2 = v2 + 1j * (v2 * np.sin(theta))
    dot = np.vdot(c1, c2)
    norm = np.linalg.norm(c1) * np.linalg.norm(c2) + 1e-8
    return abs(dot) / norm

def mitosis(chunk, max_size=50000):
    if len(str(chunk)) > max_size:
        mid = max_size // 2
        return [chunk[:mid], chunk[mid:]]
    return [chunk]

def apoptosis(chunks, threshold=0.3):
    return [c for c in chunks if c.get('coherence', 1.0) >= threshold]

class ChunkCarousel:
    def __init__(self, max_size=50000):
        self.max_size = max_size
        self.chunks = []
    def add(self, data):
        size = len(str(data).encode('utf-8'))
        if size > self.max_size:
            mid = len(str(data)) // 2
            self.chunks.append(str(data)[:mid])
            self.chunks.append(str(data)[mid:])
        else:
            self.chunks.append(str(data))
        if len(self.chunks) > 10:
            self.chunks = self.chunks[-10:]
        return self.chunks

def parse_marker(text):
    marker_len = len(text) - len(text.rstrip('/'))
    return text.rstrip('/'), marker_len

def tat_diff(state1, state2):
    return f"t:+{abs(len(str(state1))-len(str(state2)))}"
