import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import math
import matplotlib.cm as cm

def plot_pred_vs_true(y_true, y_pred, categories, save_path="pred_vs_true.png"):
    """
    绘制预测值 vs 真实值散点图，按类别上色，带上下和右侧边际直方图。

    参数
    ----------
    y_true : np.ndarray
        真实值数组。
    y_pred : np.ndarray
        预测值数组。
    categories : list or np.ndarray
        样本类别标签（可为数字或字符串）。
    save_path : str
        保存图像路径。
    """
    # 可调参数
    scatter_alpha = 1
    scatter_size = 80
    scatter_edgecolor = "#D09191"
    scatter_linewidth = 0.6
    line_color = "#ED3434"
    line_style = "--"
    line_width = 2
    reg_color = "#040404"
    reg_width = 2
    his_bar_color = "#E4AE87"
    his_bar_alpha = 1
    his_bar_width = 0.8
    xtick_labelsize = 23
    ytick_labelsize = 23
    histx_ytick_labelsize = 23
    histy_xtick_labelsize = 23

    # 创建图和网格布局
    fig = plt.figure(figsize=(8, 8))
    gs = GridSpec(4, 4, figure=fig)
    ax_scatter = fig.add_subplot(gs[1:4, 0:3])
    ax_histx = fig.add_subplot(gs[0, 0:3], sharex=ax_scatter)
    ax_histy = fig.add_subplot(gs[1:4, 3], sharey=ax_scatter)

    # 按类别绘制散点
    unique_classes = sorted(list(set(categories)))
    colors = cm.get_cmap("Paired", len(unique_classes))
    for i, cls in enumerate(unique_classes):
        mask = np.array(categories) == cls
        ax_scatter.scatter(
            y_true[mask],
            y_pred[mask],
            alpha=scatter_alpha,
            s=scatter_size,
            edgecolor=scatter_edgecolor,
            linewidth=scatter_linewidth,
            color=colors(i),
            label=f"{cls}"
        )

    # 范围和理想线
    min_val = math.floor(min(y_true.min(), y_pred.min()))
    max_val = math.ceil(max(y_true.max(), y_pred.max()))
    x_line = np.linspace(min_val, max_val, 100)
    ax_scatter.plot(x_line, x_line, line_style, color=line_color, lw=line_width)

    # 拟合线
    a, b = np.polyfit(y_true, y_pred, 1)
    y_fit = a * x_line + b
    ax_scatter.plot(x_line, y_fit, color=reg_color, lw=reg_width)

    # 上方直方图
    ax_histx.hist(y_true, bins=30, color=his_bar_color, alpha=his_bar_alpha,
                  linewidth=his_bar_width, edgecolor='black')
    ax_histx.spines['top'].set_visible(False)
    ax_histx.spines['right'].set_visible(False)
    ax_histx.tick_params(axis='y', labelsize=histx_ytick_labelsize)

    # 右侧直方图
    ax_histy.hist(y_pred, bins=30, orientation="horizontal",
                  color=his_bar_color, alpha=his_bar_alpha,
                  linewidth=his_bar_width, edgecolor='black')
    ax_histy.spines['top'].set_visible(False)
    ax_histy.spines['right'].set_visible(False)
    ax_histy.tick_params(axis='x', labelsize=histy_xtick_labelsize)

    # 主图修饰
    ax_scatter.legend(fontsize=12, frameon=False)
    ax_scatter.tick_params(axis='x', labelsize=xtick_labelsize)
    ax_scatter.tick_params(axis='y', labelsize=ytick_labelsize)
    ax_scatter.spines['top'].set_visible(False)
    ax_scatter.spines['right'].set_visible(False)
    ax_scatter.set_xlim(min_val, max_val)
    ax_scatter.set_ylim(min_val, max_val)

    plt.setp(ax_histx.get_xticklabels(), visible=False)
    plt.setp(ax_histy.get_yticklabels(), visible=False)

    fig.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

# import numpy as np
# import pandas as pd

# # 从 CSV 读取数据
# # CSV 格式：ID,True,Pred,Category
# df = pd.read_csv("example_pred_vs_true.csv")

# # 数值列
# y_true = df["True"].values
# y_pred = df["Pred"].values
# categories = df["Category"].values

# plot_pred_vs_true(y_true, y_pred, categories, save_path="pred_vs_true_example.png")

# ID,True,Pred,Category
# 1,8.5,8.2,1
# 2,9.0,8.8,2
# 3,7.5,7.8,3
# 4,6.0,6.5,4
# 5,5.0,5.5,5
# 6,7.0,6.8,1
# 7,9.5,9.2,2
# 8,8.0,8.2,3
