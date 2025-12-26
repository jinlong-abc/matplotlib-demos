import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import pearsonr, spearmanr

def plot_metrics_radar(csv_path, length_col, true_col, pred_col, figsize=(6,6), save_path="metrics_radar.png"):
    """
    根据蛋白长度分组绘制预测指标雷达图。

    参数:
    ----------
    csv_path : str
        CSV 文件路径，必须包含蛋白长度、真实值和预测值列。
    length_col : str
        CSV 中蛋白长度列名。
    true_col : str
        CSV 中真实值列名。
    pred_col : str
        CSV 中预测值列名。
    figsize : tuple, default (6,6)
        图形尺寸。
    save_path : str, default "metrics_radar.png"
        保存文件路径。

    返回:
    -------
    metrics_norm_df : pd.DataFrame
        标准化后的指标数据，按蛋白长度分组。
    """

    # ===============================
    # 读取数据
    # ===============================
    df = pd.read_csv(csv_path)

    # ===============================
    # 计算评估指标函数
    # ===============================
    def calc_metrics(y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
        mae = np.mean(np.abs(y_true - y_pred))
        pearson = pearsonr(y_true, y_pred)[0]
        spearman = spearmanr(y_true, y_pred)[0]
        r2 = pearson ** 2
        ci = 0.5 * (pearson + spearman)
        return {"RMSE": rmse, "MAE": mae, "Pearson": pearson, "Spearman": spearman, "R2": r2, "CI": ci}

    # ===============================
    # 按蛋白长度分组
    # ===============================
    bins = [0, 300, 600, 900, np.inf]
    labels_len = ["<300", "300-600", "600-900", ">900"]
    df["Length_Group"] = pd.cut(df[length_col], bins=bins, labels=labels_len, right=False)

    metrics_list = []
    for group_label in labels_len:
        group = df[df["Length_Group"] == group_label]
        if group.empty:
            continue
        metrics_cat = calc_metrics(group[true_col], group[pred_col])
        metrics_cat["Length_Group"] = group_label
        metrics_list.append(metrics_cat)

    metrics_df = pd.DataFrame(metrics_list)

    # ===============================
    # 标准化相关性指标
    # ===============================
    labels = ["Pearson", "Spearman", "R2", "CI"]
    normalized_data = []
    for _, row in metrics_df.iterrows():
        values = [np.clip(row[label], 0, 1) for label in labels]
        normalized_data.append(values)

    metrics_norm_df = pd.DataFrame(normalized_data, columns=labels, index=metrics_df["Length_Group"])

    # ===============================
    # 绘制雷达图
    # ===============================
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    color_palette = ['#ED949A', '#B2A3DD', '#96CCEA', '#A4DDD3']
    current_colors = {g: color_palette[i % len(color_palette)] for i, g in enumerate(labels_len)}

    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(polar=True))

    # 同心圆刻度
    radii_levels = np.arange(0.2, 1.01, 0.2)
    for r in radii_levels:
        ax.plot(np.linspace(0, 2*np.pi, 200), [r]*200, linestyle='--', color='gray', linewidth=0.8, alpha=0.8)
        ax.text(np.pi/2, r, f"{r:.1f}", fontsize=9, color='black', ha='center', va='bottom', fontfamily='Times New Roman')

    # 绘制每个长度区间
    for group_label in metrics_norm_df.index:
        data = metrics_norm_df.loc[group_label].tolist()
        data += data[:1]
        color = current_colors[group_label]
        ax.plot(angles, data, color=color, linewidth=1.8, label=group_label, zorder=2)
        ax.fill(angles, data, color=color, alpha=0.15, zorder=1)
        ax.scatter(angles[:-1], metrics_norm_df.loc[group_label], color=color, s=40, zorder=3)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=11, fontfamily='Times New Roman', weight='bold', color='black')

    ax.set_ylim(0, 1.1)
    ax.spines['polar'].set_visible(False)
    ax.grid(False)
    ax.set_yticklabels([])

    # 最外层边框
    ax.plot(np.linspace(0, 2*np.pi, 200), [1]*200, color='black', linewidth=1.2)

    # 图例
    group_patches = [mpatches.Patch(color=current_colors[g], alpha=0.6, label=g) for g in metrics_norm_df.index]
    fig.legend(handles=group_patches,
               loc='lower center', bbox_to_anchor=(0.5, 0.015),
               frameon=False, ncol=2,
               prop={'family': 'Times New Roman', 'weight': 'bold', 'size': 12})

    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.15)
    plt.savefig(save_path, dpi=600)
    # plt.show()

    return metrics_norm_df

# metrics_norm_df = plot_metrics_radar(
#     csv_path="example_data.csv",
#     length_col="Protein_Len",
#     true_col="True",
#     pred_col="Pred_fp",
#     figsize=(6,6),
#     save_path="metrics_radar_example.png"
# )

# print(metrics_norm_df)

# Protein_Len,True,Pred_fp
# 150,0.85,0.80
# 210,0.90,0.88
# 400,0.75,0.78
# 500,0.60,0.65
# 700,0.50,0.55
# 850,0.70,0.68
# 1000,0.95,0.92
# 1200,0.80,0.82
