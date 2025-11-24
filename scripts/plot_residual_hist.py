import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_residual_hist(y_true, y_pred):
    residuals = y_pred - y_true
    # "royalblue"（宝蓝色）
    # "orange"（橙色）
    # "green"（绿色）
    # "deepskyblue"（深天蓝色）
    # "crimson"（猩红色）
    # "red"（红色）
    # "black"（黑色）
    # "gray"（灰色）
    # "purple"（紫色）
    # "gold"（金色）
    # "teal"（蓝绿色）
    # "pink"（粉色）
    # "navy"（藏青色）
    # "olive"（橄榄色）
    # "brown"（棕色）
    # "cyan"（青色）
    # "magenta"（品红色）
    # "lime"（酸橙色/亮绿色）
    # "coral"（珊瑚色）
    # "skyblue"（天蓝色）
    # "orchid"（兰花紫）
    # "darkorange"（深橙色）
    # "coral"（珊瑚色，偏橙红）
    # "tomato"（番茄色，偏橙红）
    # "sandybrown"（沙棕色，浅橙棕）
    # "peru"（秘鲁色，橙棕）
    # "gold"（金色，偏黄橙）
    # "chocolate"（巧克力色，深橙棕）
    # "lightsalmon"（浅鲑红，橙粉色）
    # "peachpuff"（桃色，淡橙）
    # "bisque"（米色，淡橙黄）
    # "navajowhite"（纳瓦白，淡橙黄）
    # "moccasin"（鹿皮色，淡橙黄）
    # "wheat"（小麦色，浅橙黄）
    # 可调参数（部分参数当前未用到，便于后续统一风格和扩展）
    hist_color = "royalblue"   # 直方图颜色
    hist_alpha = 0.6           # 直方图透明度
    bins = 40                  # 直方图分箱数
    kde_color = "peachpuff"       # KDE曲线颜色
    kde_linewidth = 2          # KDE曲线线宽
    # 散点相关参数（本图未用到，便于统一风格）
    scatter_color = "orange"  # 散点颜色
    scatter_alpha = 0.7        # 散点透明度
    scatter_size = 70          # 散点大小
    scatter_edgecolor = "w"   # 散点边缘颜色
    scatter_linewidth = 0.6    # 散点边缘线宽
    # 线条相关参数
    line_color = "gray"        # 中心线/理想线颜色
    line_style = "--"          # 中心线/理想线线型
    line_width = 2             # 中心线/理想线线宽
    # 字体与坐标轴
    font_size = 16             # 坐标轴标签文字大小
    xtick_labelsize = 18       # x轴刻度数字大小
    ytick_labelsize = 18       # y轴刻度数字大小
    title_size = 16            # 标题字体大小
    bbox_style = dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.8, edgecolor="gray")  # 文本框样式
    # 坐标轴范围与刻度
    xlim = None                # x轴显示范围
    ylim = None                # y轴显示范围
    xtick_step = 3             # x轴刻度间隔
    ytick_step = 9             # y轴刻度间隔

    plt.figure(figsize=(7, 6))
    sns.histplot(residuals, bins=bins, kde=True, color=hist_color, alpha=hist_alpha,
                 line_kws={"color": kde_color, "lw": kde_linewidth})
    # sns.histplot(residuals, bins=bins, color=hist_color, alpha=hist_alpha, kde=False)
    # sns.kdeplot(residuals, color=kde_color, linewidth=kde_linewidth)
    plt.axvline(0, color=line_color, linestyle=line_style, lw=line_width)

    # plt.xlabel("Residuals", fontsize=font_size)
    # plt.ylabel("Count", fontsize=font_size)
    plt.title("Residual Distribution", fontsize=title_size, fontweight="bold")

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # 设置坐标轴范围
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    # 设置刻度间隔
    if xtick_step is not None:
        from matplotlib.ticker import MultipleLocator
        ax.xaxis.set_major_locator(MultipleLocator(xtick_step))
    if ytick_step is not None:
        from matplotlib.ticker import MultipleLocator
        ax.yaxis.set_major_locator(MultipleLocator(ytick_step))
    # 设置刻度字体大小
    ax.tick_params(axis='x', labelsize=xtick_labelsize)
    ax.tick_params(axis='y', labelsize=ytick_labelsize)
   
    plt.grid(False)  # 关闭网格。注意：plt.grid(False) 即可完全关闭背景网格，若要显示可用 plt.grid(True, linestyle="--", alpha=0.5)
    # plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("residual_hist7.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    # y_true = np.array([3, 5, 7, 9, 11])
    # y_pred = np.array([2.8, 5.2, 6.5, 8.9, 11.3])
    # plot_residual_hist(y_true, y_pred)
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
    plot_residual_hist(label, pred)
