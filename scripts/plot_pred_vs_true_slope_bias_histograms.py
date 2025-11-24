import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import math
import matplotlib.cm as cm

def plot_pred_vs_true(y_true, y_pred, categories):
    # 可调参数
    scatter_alpha = 1 # 1 表示完全不透明
    scatter_size = 80
    scatter_edgecolor = "#D09191"
    scatter_linewidth = 0.6
    line_color = "#ED3434"
    line_style = "--"
    line_width = 2
    reg_color = "#040404"
    reg_width = 2 # 拟合线宽度
    font_size = 16
    xtick_labelsize = 23
    ytick_labelsize = 23
    histx_ytick_labelsize = 23
    histy_xtick_labelsize = 23
    title_size = 16
    bbox_style = dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.8, edgecolor="gray")
    his_bar_color = "#E4AE87"
    his_bar_alpha = 1
    # his_bar_width = 1.5
    his_bar_width = 0.8

    # 创建图和网格布局
    fig = plt.figure(figsize=(8, 8))
    gs = GridSpec(4, 4, figure=fig)
    ax_scatter = fig.add_subplot(gs[1:4, 0:3])
    ax_histx = fig.add_subplot(gs[0, 0:3], sharex=ax_scatter)
    ax_histy = fig.add_subplot(gs[1:4, 3], sharey=ax_scatter)

    # -------- 按类别绘制散点图 --------
    unique_classes = sorted(list(set(categories)))
    colors = cm.get_cmap("Paired", len(unique_classes))  # 可换为 "tab10", "Paired" 等
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
            # label=f"{cls}",
        )

    # 基础范围
    min_val_raw = min(y_true.min(), y_pred.min())
    max_val_raw = max(y_true.max(), y_pred.max())
    min_val = math.floor(min_val_raw)
    max_val = math.ceil(max_val_raw)
    x_line = np.linspace(min_val, max_val, 100)

    # 理想线 y = x
    # ax_scatter.plot(x_line, x_line, line_style, color=line_color, lw=line_width, label="Ideal (y = x)")
    ax_scatter.plot(x_line, x_line, line_style, color=line_color, lw=line_width)

    # 添加最小二乘拟合线
    a, b = np.polyfit(y_true, y_pred, 1)
    y_fit = a * x_line + b
    # ax_scatter.plot(x_line, y_fit, color=reg_color, lw=reg_width, label=f"Fit line (y={a:.2f}x+{b:.2f})")
    ax_scatter.plot(x_line, y_fit, color=reg_color, lw=reg_width)

    # 计算夹角
    ideal_angle = np.pi / 4
    fit_angle = np.arctan(a)
    delta_angle = np.degrees(abs(fit_angle - ideal_angle))

    # 上方直方图
    ax_histx.hist(y_true, bins=30, color=his_bar_color, alpha=his_bar_alpha, linewidth=his_bar_width, edgecolor='black')
    ax_histx.spines['top'].set_visible(False)
    ax_histx.spines['right'].set_visible(False)
    ax_histx.tick_params(axis='y', labelsize=histx_ytick_labelsize)

    # 右侧直方图
    ax_histy.hist(y_pred, bins=30, orientation="horizontal", color=his_bar_color, alpha=his_bar_alpha, linewidth=his_bar_width, edgecolor='black')
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

    # 添加夹角文本标注
    # ax_scatter.text(min_val + (max_val - min_val)*0.05, max_val - (max_val - min_val)*0.1,
    #          f"Angle Δθ = {delta_angle:.2f}°", fontsize=14, bbox=bbox_style)

    plt.savefig("pred_vs_true_with_class_Paired_23.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    label_list = []
    pred_list = []
    class_list = []

    # 从 CSV 读取真实值与类别
    # ID,True,Pred,Category
    with open('/home/wjl/data/DTI_prj/Arch_Lab/写作图相关代码/FusionSmi_项目图/亲和力相关指标作图/casf2016_285_protein_class.csv', 'r') as f:
        next(f)
        for line in f:
            line = line.strip().split(',')
            label_list.append(float(line[1]))  # 第2列是 label
            class_list.append(line[-1])        # 最后一列是分类
            pred_list.append(float(line[2]))   # 第3列是 pred

    # === 数字到类别名映射 ===
    class_map = {
        "1": "Kinase",
        "2": "Enzyme",
        "3": "Nuclear Receptor",
        "4": "Ion Channel",
        "5": "Other"
    }

    # 将数字替换为对应类别名
    class_list = [class_map.get(str(c), str(c)) for c in class_list]

    label = np.array(label_list, dtype=float)
    pred = np.array(pred_list, dtype=float)
    plot_pred_vs_true(label, pred, class_list)

# 激酶：1
# Enzyme：2
# Nuclear Receptor：3
# Ion Channel：4
# Other：5