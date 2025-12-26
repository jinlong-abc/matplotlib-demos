import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Wedge, Circle

# ================================
# 设置绘图参数（顶刊风格）
# ================================
def set_plot_style():
    plt.rcParams.update({
        'font.family': 'times new roman',
        'font.size': 10,
        'axes.labelsize': 10,
        'axes.titlesize': 10,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'figure.dpi': 600,
        'savefig.dpi': 600,
        'axes.unicode_minus': False,
        'mathtext.fontset': 'custom',
        'mathtext.rm': 'Arial',
        'mathtext.it': 'Arial:italic',
        'mathtext.bf': 'Arial:bold'
    })

# ================================
# 绘制混合相关性热图函数
# ================================
def plot_mixed_correlation_heatmap(
        csv_file: str,
        save_path: str = 'correlation_mixed_RdBu.jpg',
        figsize: tuple = (10, 8),
        cmap_name: str = 'RdBu_r',
        show_values: bool = True,
        select_columns: list = None):
    """
    绘制混合型相关性热图（左下三角扇形、右上三角气泡+数值、对角线固定1.0）

    输入 CSV 文件要求：
    -----------------
    - 行：样本
    - 列：特征
    - 全部为数值型
    - 示例：
    
        Sample,Feature1,Feature2,Feature3,Feature4
        S1,0.23,1.2,3.4,0.5
        S2,0.45,0.8,2.1,0.7
        S3,0.12,1.5,3.9,0.2

    参数:
    ----------
    csv_file : str
        CSV 文件路径
    save_path : str
        保存图像路径（支持 .jpg, .png 等格式）
    figsize : tuple
        图像尺寸 (宽, 高)
    cmap_name : str
        matplotlib 颜色映射名称
    show_values : bool
        是否在右上三角显示数值
    select_columns : list or None
        如果只想绘制部分特征，可传入列名列表。默认 None 表示使用全部特征。

    返回:
    ----------
    correlation_matrix : pd.DataFrame
        计算得到的皮尔森相关系数矩阵
    """
    set_plot_style()

    # 读取数据
    df = pd.read_csv(csv_file, encoding='utf-8')
    if select_columns is not None:
        df = df[select_columns]

    feature = df  # 可根据需求筛选列

    # 计算相关系数矩阵
    correlation_matrix = feature.corr(method='pearson')
    correlation_matrix.to_csv('correlation_matrix_RdBu.csv', index=True)

    # 绘图
    fig, ax = plt.subplots(figsize=figsize)
    cmap = plt.get_cmap(cmap_name)

    # 绘制空热图以生成坐标和颜色条
    sns.heatmap(
        np.zeros_like(correlation_matrix),
        cmap=cmap,
        annot=False,
        square=True,
        cbar_kws={
            "shrink": 0.8,
            "label": "Pearson correlation coefficient",
            "ticks": np.arange(-1, 1.1, 0.5)
        },
        vmin=-1, vmax=1,
        ax=ax
    )

    n = len(correlation_matrix)
    for i in range(n):
        for j in range(n):
            value = correlation_matrix.iloc[i, j]
            color = cmap((value + 1)/2)
            brightness = color[0]*0.299 + color[1]*0.587 + color[2]*0.114
            text_color = 'white' if brightness < 0.6 else 'black'

            # 左下三角：扇形
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
                if show_values:
                    ax.text(j+0.5, i+0.5, f"{value:.2f}", ha='center', va='center',
                            fontsize=10, color=text_color)

            # 对角线：固定显示1.0
            else:
                diag_value = 1.0
                diag_color = cmap((diag_value + 1)/2)
                bubble = Circle((j+0.5, i+0.5), 0.4,
                                facecolor=diag_color, edgecolor='gray', linewidth=0.8)
                ax.add_patch(bubble)
                ax.text(j+0.5, i+0.5, f"{diag_value:.2f}", ha='center', va='center',
                        fontsize=10, color='white')

    # 坐标标签
    ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha='right')
    ax.set_yticklabels(correlation_matrix.columns, rotation=0)

    # 网格线
    for x in range(n+1):
        ax.axhline(x, color='white', linewidth=0.5)
        ax.axvline(x, color='white', linewidth=0.5)

    plt.tight_layout()
    plt.savefig(save_path, dpi=600, bbox_inches='tight', pil_kwargs={'optimize': True})
    print(f"热图已保存为 {save_path} (600dpi)")
    plt.show()

    return correlation_matrix

# ================================
# 使用示例
# ================================
# correlation_matrix = plot_mixed_correlation_heatmap(
#     csv_file="Feature.csv",
#     save_path="correlation_mixed_RdBu.jpg",
#     figsize=(12,10),
#     cmap_name="RdBu_r",
#     show_values=True,
#     select_columns=["Feature1","Feature2","Feature3"]
# )
