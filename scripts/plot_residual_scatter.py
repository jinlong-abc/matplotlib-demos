import numpy as np
import matplotlib.pyplot as plt

def plot_residual_scatter(y_true, y_pred):
    residuals = y_pred - y_true

    # 可调参数
    scatter_color = "#72B6A1"  # 散点颜色（如："royalblue", "orange", "green", "deepskyblue", "crimson"）
    scatter_alpha = 0.7
    scatter_size = 40
    scatter_edgecolor = "k"
    scatter_linewidth = 0.6
    line_color = "#D47B3B" 
    line_style = "--"
    line_width = 2
    font_size = 14
    title_size = 16
    xtick_labelsize = 18          # x轴刻度数字大小（如：10, 12, 14, 16）
    ytick_labelsize = 18          # y轴刻度数字大小（如：10, 12, 14, 16）

    plt.figure(figsize=(7, 6))
    plt.scatter(y_true, residuals, alpha=scatter_alpha, s=scatter_size,
                edgecolor=scatter_edgecolor, linewidth=scatter_linewidth,
                color=scatter_color)
    plt.axhline(0, color=line_color, linestyle=line_style, lw=line_width)

    # plt.xlabel("True values", fontsize=font_size)
    # plt.ylabel("Residuals", fontsize=font_size)
    # plt.title("Residual Plot", fontsize=title_size, fontweight="bold")
    
    # 设置坐标轴刻度数字大小
    plt.tick_params(axis='x', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', labelsize=ytick_labelsize)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.grid(False)  # 关闭网格。注意：plt.grid(False) 即可完全关闭背景网格，若要显示可用 plt.grid(True, linestyle="--", alpha=0.5)
    # plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("residual_scatter4.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    # y_true = np.array([3, 5, 7, 9, 11])
    # y_pred = np.array([2.8, 5.2, 6.5, 8.9, 11.3])
    # plot_residual_scatter(y_true, y_pred)
    label_list = []
    # ID,UniProt,Assay Result,pInteraction,Normal SMILES,SMILES,FusionSmi,Mapped_SMILES,IntSeq,Sequence
    with open('/home/wjl/data/DTI_prj/Arch_Lab/写作图相关代码/FusionSmi_项目图/亲和力相关指标作图/raw_data/FusionSmi/1024_test.csv', 'r') as f:
        next(f)  # 跳过标题行
        for line in f:
            line = line.strip().split(',')
            label_list.append(float(line[3]))  # 第4列是label

    # 从日志文件提取预测值
    pred_list = []
    with open("/home/wjl/data/DTI_prj/Arch_Lab/写作图相关代码/FusionSmi_项目图/亲和力相关指标作图/raw_data/FusionSmi/test_evalue_log_1024_1.txt", "r") as f:  # 这里替换成你的日志文件路径
        for line in f:
            if "Predicted affinity:" in line:
                import re
                value = float(re.findall(r"[-+]?\d*\.\d+|\d+", line)[0])
                # ===调试===
                # print(f"Extracted predicted value: {value}")
                pred_list.append(value)
    
    label = np.array(label_list, dtype=float).reshape(-1)
    pred = np.array(pred_list, dtype=float).reshape(-1)
    plot_residual_scatter(label, pred)