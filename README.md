# Matplotlib Plot Collection

This project is a curated collection of **Matplotlib plotting examples** that I have developed during my research and learning. It covers common visualization types including line plots, bar charts, scatter plots, heatmaps, error bands, 3D structures, and more.

The goal is to provide **simple, reusable, and ready-to-run scripts** for quick reference by yourself or other researchers.

---

## 🚀 Features

* Covers common **Matplotlib plot types**
* Ready-to-run scripts, easy to modify
* Each example is **well-commented** for better understanding
* Supports **Chinese fonts** (if configured)
* Built with **Python + Matplotlib**, no extra dependencies required

---

## 📁 Project Structure

```
matplotlib-demos/
│
├── scripts/          # Python plotting scripts
│   ├── line_plot.py
│   ├── bar_chart.py
│   ├── scatter_plot.py
│   └── ...
│
├── examples/         # Output images (optional)
│
├── requirements.txt  # Python dependencies
└── README.md
```

---

## 🧪 Example Use Case

For example, to plot **cellular thermal shift assay (CETSA) curves**:

```python
# Example: plotting CETSA curve
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array([37, 42, 47, 52, 57, 62])
signal = np.array([1.0, 0.92, 0.85, 0.60, 0.35, 0.10])

plt.figure(figsize=(6,4))
plt.plot(temperature, signal, marker='o', linestyle='-', color='b', label='Protein stability')
plt.xlabel('Temperature (°C)')
plt.ylabel('Signal Intensity')
plt.title('CETSA Curve')
plt.legend()
plt.grid(True)
plt.show()
```

---

## ⚡ Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/matplotlib-demos.git
cd matplotlib-demos
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run any script inside `scripts/`:

```bash
python scripts/line_plot.py
```

---

## 🎨 Notes

* All scripts are **self-contained** and can be adapted for your own data
* For Chinese font support, configure `matplotlib` with a proper font family:

```python
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```
