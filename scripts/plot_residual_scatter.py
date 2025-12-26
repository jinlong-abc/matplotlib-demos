import numpy as np
import matplotlib.pyplot as plt

def plot_residual_scatter(y_true, y_pred, save_path="residual_scatter.png",
                          scatter_color="#72B6A1", scatter_alpha=0.7, scatter_size=40,
                          scatter_edgecolor="k", scatter_linewidth=0.6,
                          line_color="#D47B3B", line_style="--", line_width=2,
                          figsize=(7,6), title="Residual Plot",
                          xtick_labelsize=18, ytick_labelsize=18):
    """
    绘制残差散点图（Residuals = Pred - True）。

    参数
    ----------
    y_true : np.ndarray
        真实值数组
    y_pred : np.ndarray
        预测值数组
    save_path : str
        保存图像路径
    scatter_color : str
        散点颜色
    scatter_alpha : float
        散点透明度
    scatter_size : float
        散点大小
    scatter_edgecolor : str
        散点边缘颜色
    scatter_linewidth : float
        散点边缘线宽
    line_color : str
        中心线颜色（y=0）
    line_style : str
        中心线线型
    line_width : float
        中心线宽度
    figsize : tuple
        图像大小
    title : str
        图标题
    xtick_labelsize : int
        x轴刻度字体大小
    ytick_labelsize : int
        y轴刻度字体大小
    """
    residuals = y_pred - y_true

    plt.figure(figsize=figsize)
    plt.scatter(y_true, residuals, alpha=scatter_alpha, s=scatter_size,
                edgecolor=scatter_edgecolor, linewidth=scatter_linewidth,
                color=scatter_color)
    plt.axhline(0, color=line_color, linestyle=line_style, lw=line_width)

    plt.title(title, fontsize=16, fontweight="bold")
    plt.tick_params(axis='x', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', labelsize=ytick_labelsize)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.grid(False)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

# import numpy as np
# import pandas as pd

# # 从 CSV 读取真实值和预测值
# # CSV 示例：ID,True,Pred
# df = pd.read_csv("example_residual_scatter.csv")

# y_true = df["True"].values
# y_pred = df["Pred"].values

# plot_residual_scatter(y_true, y_pred, save_path="residual_scatter_example.png")

# ID,True,Pred
# 1,3.0,2.8
# 2,5.0,5.2
# 3,7.0,6.5
# 4,9.0,8.9
# 5,11.0,11.3
# 6,6.5,6.8
# 7,8.2,8.0
# 8,10.1,10.0
