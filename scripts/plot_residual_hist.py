import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator

def plot_residual_hist(y_true, y_pred, save_path="residual_hist.png",
                       hist_color="royalblue", kde_color="peachpuff", hist_alpha=0.6,
                       bins=40, line_color="gray", line_style="--", line_width=2,
                       figsize=(7,6), title="Residual Distribution",
                       xtick_step=3, ytick_step=9, xtick_labelsize=18, ytick_labelsize=18,
                       title_size=16):
    """
    绘制残差（y_pred - y_true）直方图，并叠加KDE曲线。

    参数
    ----------
    y_true : np.ndarray
        真实值数组
    y_pred : np.ndarray
        预测值数组
    save_path : str
        保存图像路径
    hist_color : str
        直方图颜色
    kde_color : str
        KDE曲线颜色
    hist_alpha : float
        直方图透明度
    bins : int
        直方图分箱数
    line_color : str
        中心线颜色
    line_style : str
        中心线线型
    line_width : float
        中心线宽度
    figsize : tuple
        图像大小
    title : str
        图标题
    xtick_step : float
        x轴刻度间隔
    ytick_step : float
        y轴刻度间隔
    xtick_labelsize : int
        x轴刻度字体大小
    ytick_labelsize : int
        y轴刻度字体大小
    title_size : int
        标题字体大小
    """
    residuals = y_pred - y_true

    plt.figure(figsize=figsize)
    sns.histplot(residuals, bins=bins, kde=True, color=hist_color, alpha=hist_alpha,
                 line_kws={"color": kde_color, "lw": 2})
    plt.axvline(0, color=line_color, linestyle=line_style, lw=line_width)

    plt.title(title, fontsize=title_size, fontweight="bold")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 设置刻度间隔
    if xtick_step is not None:
        ax.xaxis.set_major_locator(MultipleLocator(xtick_step))
    if ytick_step is not None:
        ax.yaxis.set_major_locator(MultipleLocator(ytick_step))

    # 设置刻度字体大小
    ax.tick_params(axis='x', labelsize=xtick_labelsize)
    ax.tick_params(axis='y', labelsize=ytick_labelsize)

    plt.grid(False)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

# import numpy as np
# import pandas as pd

# # 从 CSV 读取真实值和预测值
# # CSV 示例：ID,True,Pred
# df = pd.read_csv("example_residual.csv")

# y_true = df["True"].values
# y_pred = df["Pred"].values

# plot_residual_hist(y_true, y_pred, save_path="residual_hist_example.png")

# ID,True,Pred
# 1,3.0,2.8
# 2,5.0,5.2
# 3,7.0,6.5
# 4,9.0,8.9
# 5,11.0,11.3
# 6,6.5,6.8
# 7,8.2,8.0
# 8,10.1,10.0
