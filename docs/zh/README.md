# 🧪 TAT-DEMO

**TAT (TreeAngleTap)** — 面向 LLM 的生物记忆。

本演示展示 TAT 的核心机制：

[![许可证: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maratsultanov2/TAT-DEMO/blob/main/demo.ipynb)

---

## 内容

| 机制 | 描述 |
|---|---|
| **块旋转木马** | 50 KB 环形缓冲区，溢出时分裂 |
| **标记 `/`** | 分层标记（词/短语/句子/段落） |
| **相干性 θ=1.987** | 带相位的复数相干性 |
| **有丝分裂 / 凋亡** | 块的裂变和清理 |
| **TAT-DIFF** | 状态增量（节省 99.99% token） |
| **全息记忆** | 从 42% 数据中恢复（原理） |

---

## 在 Colab 中运行

点击上方徽章，运行所有单元格，查看结果。

---

## 语言

- [English](docs/en/README.md)
- [Русский](docs/ru/README.md)
- [中文](docs/zh/README.md)

---

## 链接

- [TAT-ROOT](https://github.com/maratsultanov2/TAT-ROOT)
- [TAT-ONE-TAP](https://github.com/maratsultanov2/TAT-ONE-TAP)

---

## 许可证

- 代码: AGPL-3.0
