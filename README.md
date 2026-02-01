<p align="center">
  <img src="pecon.jpg" alt="PeCon" width="250">
</p>

### A Lightweight Econometrics Library in C & Cython

**PeCon** is a high-performance econometrics and statistics library written in **pure C** with **Cython bindings**, designed for researchers and developers who want **speed, control, and minimal dependencies**.

Unlike NumPy, SciPy, or Statsmodels, **PeCon implements its own numerical core in C**, making it lightweight, fast, and suitable for low-level or embedded scientific workflows.

---

## ✨ Features

- 🚀 **High performance** (C backend, minimal Python overhead)
- 🧮 Core econometrics & statistics implemented **from scratch**
- 📦 No heavy dependencies (NumPy optional)
- 🔌 Clean Python API
- 🧠 Designed for research, teaching, and reproducibility

---

## 🛠 Installation

```bash
pip install pecon
```
### Development (Editable Install)

After cloning the repo
```bash
pip install -e .
```
---

## 🚀 Quick Start

```python
from pecon import stats

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

coef, pval = stats.corr(x, y)
print(coef, pval)
```
---
## 🤝 Contributing

### Contributions are welcome:

- New econometric models
- Optimized C routines
- Documentation & examples

Open an issue or submit a pull request.

---

## 👨‍💻 Author

**BenusF**
