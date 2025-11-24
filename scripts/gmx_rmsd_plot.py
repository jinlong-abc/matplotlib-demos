import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# =========================================================
# 🎨【全局绘图参数区】—— 统一控制图形外观
# =========================================================

# --- 文件路径 ---
file_path = "/home/./rmsd_protein.xvg"

# --- Seaborn & Matplotlib 风格 ---
plot_style = "whitegrid"         # 可选: "white", "dark", "whitegrid", "darkgrid", "ticks"
plot_context = "talk"            # 控制字体比例: "paper", "notebook", "talk", "poster"
font_scale = 1.2                 # 字体缩放比例

# --- 图尺寸与分辨率 ---
figsize = (8, 4)
dpi = 300

# --- 线条样式 ---
line_color = "#BDBFC0"           # 主线颜色 (可用16进制)
line_width = 2.5                 # 线条粗细
smooth_color = "#E67E22"         # 平滑曲线颜色
smooth_window = 10               # 平滑窗口 (rolling window)
show_smooth = False              # 是否绘制平滑曲线

# --- 坐标轴 & 标题 ---
show_title = False
title_text = "Protein-Ligand RMSD Over Time"
title_fontsize = 18
xlabel_text = "Time (ns)"
ylabel_text = "RMSD (nm)"
label_fontsize = 14

# --- 网格参数 ---
show_grid = False
grid_style = "--"                # 可选: "-", "--", ":", "-."
grid_alpha = 0.3                 # 网格透明度

# --- 边框 (spines) 控制 ---
spine_color = "#191818"          # 边框颜色
spine_width = 1.5                # 边框粗细
show_top_spine = False           # 是否显示上边框
show_right_spine = False         # 是否显示右边框
show_bottom_spine = True         # 是否显示下边框
show_left_spine = True           # 是否显示左边框

# --- 坐标轴刻度控制 ---
tick_labelsize = 23              # 刻度字体大小
tick_length = 5                  # 刻度线长度
tick_width = 1.5                   # 刻度线粗细
tick_direction = "out"           # 刻度线方向: "in", "out", "inout"
tick_color = "#333333"           # 刻度线颜色
tick_labelweight = "normal"      # 刻度标签粗细: "normal" or "bold"

# --- 其他选项 ---
save_fig = True
output_file = "rmsd_plot_ACTN4_2.png"
show_fig = False
ylim_auto = False                 # 自动Y轴范围
ylim_range = (4.5, 5.5)            # 手动范围 (当 ylim_auto=False 时生效)

# =========================================================
# 🧩【函数定义区】
# =========================================================
def read_xvg(filepath):
    """读取 GROMACS .xvg 文件（忽略注释行）"""
    time, rmsd = [], []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith(('#', '@')) or not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                time.append(float(parts[0]))
                rmsd.append(float(parts[1]))
    return pd.DataFrame({'Time (ns)': time, 'RMSD (nm)': rmsd})

# =========================================================
# 📈【主绘图部分】
# =========================================================
df = read_xvg(file_path)

sns.set_theme(style=plot_style, context=plot_context, font_scale=font_scale)
plt.figure(figsize=figsize)

# 主曲线
sns.lineplot(
    data=df,
    x="Time (ns)",
    y="RMSD (nm)",
    color=line_color,
    linewidth=line_width,
    label="RMSD"
)

# 平滑曲线
if show_smooth:
    df["Smooth"] = df["RMSD (nm)"].rolling(window=smooth_window, center=True).mean()
    sns.lineplot(
        data=df,
        x="Time (ns)",
        y="Smooth",
        color=smooth_color,
        linewidth=2.0,
        label=f"Smoothed ({smooth_window}-pt)"
    )

# 标题与坐标轴
if show_title:
    plt.title(title_text, fontsize=title_fontsize, weight='bold', pad=15)

plt.xlabel(xlabel_text, fontsize=label_fontsize)
plt.ylabel(ylabel_text, fontsize=label_fontsize)

# Y轴范围
if not ylim_auto:
    plt.ylim(ylim_range)
else:
    plt.ylim(0, df["RMSD (nm)"].max() * 1.1)

# 网格设置
if show_grid:
    plt.grid(True, linestyle=grid_style, alpha=grid_alpha)
else:
    plt.grid(False)

# ------------------------------
# ⚙️ 坐标轴细节微调
# ------------------------------
ax = plt.gca()

# 边框控制
for spine_name, spine in ax.spines.items():
    if spine_name == "top":
        spine.set_visible(show_top_spine)
    elif spine_name == "right":
        spine.set_visible(show_right_spine)
    elif spine_name == "bottom":
        spine.set_visible(show_bottom_spine)
    elif spine_name == "left":
        spine.set_visible(show_left_spine)
    spine.set_color(spine_color)
    spine.set_linewidth(spine_width)

# 刻度控制
ax.tick_params(
    axis="both",
    which="major",
    direction=tick_direction,
    length=tick_length,
    width=tick_width,
    colors=tick_color,
    labelsize=tick_labelsize
)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight(tick_labelweight)

plt.tight_layout()
plt.legend(frameon=False)

# 保存与显示
if save_fig:
    plt.savefig(output_file, dpi=dpi, bbox_inches="tight")
if show_fig:
    plt.show()
