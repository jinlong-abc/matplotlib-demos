import numpy as np
import matplotlib.pyplot as plt

def plot_sorted_curve(y_true, y_pred, save_path="sorted_curve.png",
                      true_color="#D47B3B", pred_color="#72B6A1",
                      true_marker="o", pred_marker="s",
                      true_linewidth=2, pred_linewidth=1,
                      true_markersize=2, pred_markersize=2,
                      figsize=(8,6), title="Sorted True vs Predicted",
                      xtick_labelsize=18, ytick_labelsize=18):
    """
    绘制按真实值排序后的真实值与预测值曲线。

    参数
    ----------
    y_true : np.ndarray
        真实值数组
    y_pred : np.ndarray
        预测值数组
    save_path : str
        保存图像路径
    true_color : str
        真实值曲线颜色
    pred_color : str
        预测值曲线颜色
    true_marker : str
        真实值曲线标记
    pred_marker : str
        预测值曲线标记
    true_linewidth : float
        真实值曲线线宽
    pred_linewidth : float
        预测值曲线线宽
    true_markersize : float
        真实值曲线标记大小
    pred_markersize : float
        预测值曲线标记大小
    figsize : tuple
        图像大小
    title : str
        图标题
    xtick_labelsize : int
        x轴刻度字体大小
    ytick_labelsize : int
        y轴刻度字体大小
    """
    sorted_idx = np.argsort(y_true)

    plt.figure(figsize=figsize)
    plt.plot(y_true[sorted_idx], label="True", marker=true_marker, color=true_color,
             lw=true_linewidth, markersize=true_markersize)
    plt.plot(y_pred[sorted_idx], label="Pred", marker=pred_marker, color=pred_color,
             lw=pred_linewidth, markersize=pred_markersize)

    plt.title(title, fontsize=16, fontweight="bold")
    plt.tick_params(axis='x', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', labelsize=ytick_labelsize)
    plt.legend()

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.grid(False)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

# import numpy as np
# import pandas as pd

# # 示例 CSV：ID,True,Pred
# df = pd.read_csv("example_sorted_curve.csv")

# y_true = df["True"].values
# y_pred = df["Pred"].values

# plot_sorted_curve(y_true, y_pred, save_path="sorted_curve_example.png")

# ID,True,Pred
# 1,3.0,2.8
# 2,5.0,5.2
# 3,7.0,6.5
# 4,9.0,8.9
# 5,11.0,11.3
# 6,6.5,6.8
# 7,8.2,8.0
# 8,10.1,10.0
