import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Wedge, Circle

# ================================
# 设置绘图参数（顶刊风格）
# ================================
plt.rcParams.update({
    'font.family': 'times new roman',   # 字体（常用顶刊风格：Times New Roman）
    'font.size': 10,                    # 全局字体大小
    'axes.labelsize': 10,               # 坐标轴标签字体大小
    'axes.titlesize': 10,               # 标题字体大小
    'xtick.labelsize': 8,               # x 轴刻度字体大小
    'ytick.labelsize': 8,               # y 轴刻度字体大小
    'figure.dpi': 600,                  # 图像分辨率（显示时）
    'savefig.dpi': 600,                 # 保存图像分辨率
    'axes.unicode_minus': False,        # 避免负号显示异常
    'mathtext.fontset': 'custom',       # 数学字体设置
    'mathtext.rm': 'Arial',             # 数学公式正体
    'mathtext.it': 'Arial:italic',      # 数学公式斜体
    'mathtext.bf': 'Arial:bold'         # 数学公式粗体
})

# ================================
# 读取输入数据
# ================================
# 输入 CSV 文件必须是数值型的特征矩阵（行是样本，列是特征）
df = pd.read_csv("/home/wjl/data/DTI_prj/Arch_Lab/写作图相关代码/FusionSmi_项目图/热图/Feature.csv", encoding='utf-8')
feature = df   # 如果要筛选特定列，可以在这里修改

# ================================
# 计算皮尔森相关系数矩阵
# ================================
correlation_matrix = feature.corr(method='pearson')
correlation_matrix.to_csv('correlation_matrix_RdBu.csv', index=True)  # 保存矩阵为 CSV 方便复用

# ================================
# 绘制图形
# ================================
fig, ax = plt.subplots(figsize=(10, 8))  # 图形尺寸
cmap = plt.get_cmap("RdBu_r")            # 颜色映射（红蓝对比）

# 先绘制空白热图，用来生成坐标和颜色条
sns.heatmap(
    np.zeros_like(correlation_matrix),   # 空矩阵
    cmap=cmap,                           # 颜色映射
    annot=False,                         # 是否显示数值
    square=True,                         # 单元格保持正方形
    cbar_kws={
        "shrink": 0.8,                   # 颜色条缩放比例
        "label": "Pearson correlation coefficient", # 颜色条标签
        "ticks": np.arange(-1, 1.1, 0.5) # 颜色条刻度
    },
    vmin=-1, vmax=1,                     # 色彩范围固定在 [-1, 1]
    ax=ax
)

# ================================
# 绘制左下三角（扇形）、右上三角（气泡）、对角线（数值）
# ================================
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        value = correlation_matrix.iloc[i, j]
        color = cmap((value + 1)/2)   # [-1,1] → [0,1] 映射到颜色
        brightness = color[0]*0.299 + color[1]*0.587 + color[2]*0.114
        text_color = 'white' if brightness < 0.6 else 'black'

        # 左下三角：相关系数大小用扇形表示
        if i > j:
            outline = Circle((j+0.5, i+0.5), 0.4, facecolor='none',
                             edgecolor='gray', linewidth=0.8)
            ax.add_patch(outline)
            angle = 360 * abs(value)
            if value >= 0:
                wedge = Wedge((j+0.5, i+0.5), 0.4, 270, 270+angle,
                              facecolor=color, edgecolor='black', linewidth=0.5)
            else:
                wedge = Wedge((j+0.5, i+0.5), 0.4, 90, 90+angle,
                              facecolor=color, edgecolor='black', linewidth=0.5)
            ax.add_patch(wedge)

        # 右上三角：气泡 + 数值
        elif i < j:
            bubble = Circle((j+0.5, i+0.5), 0.4,
                            facecolor=color, edgecolor='gray', linewidth=0.8)
            ax.add_patch(bubble)
            ax.text(j+0.5, i+0.5, f"{value:.2f}", ha='center', va='center',
                    fontsize=10, color=text_color)

        # 对角线：固定显示 1.0
        else:
            diag_value = 1.0
            diag_color = cmap((diag_value + 1)/2)
            bubble = Circle((j+0.5, i+0.5), 0.4,
                            facecolor=diag_color, edgecolor='gray', linewidth=0.8)
            ax.add_patch(bubble)
            ax.text(j+0.5, i+0.5, f"{diag_value:.2f}", ha='center', va='center',
                    fontsize=10, color='white')

# ================================
# 坐标标签
# ================================
ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha='right')
ax.set_yticklabels(correlation_matrix.columns, rotation=0)

# 添加网格线
for x in range(len(correlation_matrix)+1):
    ax.axhline(x, color='white', linewidth=0.5)
    ax.axvline(x, color='white', linewidth=0.5)

# 调整边距
plt.tight_layout()

# ================================
# 保存为 JPEG 高分辨率
# ================================
plt.savefig('correlation_mixed_RdBu.jpg',
            dpi=600,
            bbox_inches='tight',
            pil_kwargs={'optimize': True})

print("热图已保存为 correlation_mixed_RdBu.jpg (600dpi)")
plt.show()
