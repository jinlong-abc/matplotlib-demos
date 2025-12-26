import pandas as pd
import matplotlib.pyplot as plt
import re

def plot_spearman_ranking(csv_path, save_path="ranking_bar.png", highlight_name="FusionSmi",
                           figsize=(5,6), bar_color="#2B5DA3", highlight_color="#F5A623",
                           ecolor="black", capsize=3, xlabel="Spearman Correlation Coefficient"):
    """
    绘制带置信区间的水平条形图，突出显示指定评分函数。

    参数
    ----------
    csv_path : str
        CSV文件路径，需包含列 ["评分函数 (Scoring Function)", "ρ (Spearman)", "90% 置信区间 (Confidence Interval)"]
    save_path : str
        保存图片路径
    highlight_name : str
        要高亮显示的评分函数名称
    figsize : tuple
        图像大小
    bar_color : str
        默认条形颜色
    highlight_color : str
        高亮条形颜色
    ecolor : str
        误差条颜色
    capsize : float
        误差条帽宽度
    xlabel : str
        x轴标签
    """
    df = pd.read_csv(csv_path)
    df = df.head(20)  # 只取前20名

    # 解析置信区间字符串
    def parse_interval(interval_str):
        nums = re.findall(r"[-+]?\d*\.\d+|\d+", interval_str)
        if float(nums[0]) < 0 or float(nums[1]) < 0 or float(nums[1]) < float(nums[0]):
            raise ValueError(f"Invalid confidence interval values: {nums[0]}, {nums[1]}")
        return [float(nums[0]), float(nums[1])] if len(nums) == 2 else [None, None]

    df[["ci_low", "ci_high"]] = df["90% 置信区间 (Confidence Interval)"].apply(parse_interval).tolist()

    # 计算误差
    df["error_low"] = df["ρ (Spearman)"] - df["ci_low"]
    df["error_high"] = df["ci_high"] - df["ρ (Spearman)"]

    # 按排名顺序逆序排列
    df = df.iloc[::-1]

    # 设置颜色
    colors = [highlight_color if x == highlight_name else bar_color for x in df["评分函数 (Scoring Function)"]]

    # 绘图
    plt.figure(figsize=figsize)
    plt.barh(df["评分函数 (Scoring Function)"], df["ρ (Spearman)"],
             xerr=[df["error_low"], df["error_high"]],
             color=colors, ecolor=ecolor, capsize=capsize)

    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel("")
    plt.xlim(0, 1.0)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

# csv_path = "example_spearman.csv"
# plot_spearman_ranking(csv_path, save_path="ranking_bar_example.png", highlight_name="FusionSmi")

# 评分函数 (Scoring Function),ρ (Spearman),90% 置信区间 (Confidence Interval)
# FusionSmi,0.78,"0.70-0.85"
# Vina,0.72,"0.63-0.80"
# Glide,0.68,"0.60-0.75"
# Gold,0.64,"0.55-0.72"
# ChemScore,0.60,"0.50-0.69"
# XScore,0.58,"0.48-0.67"
# Autodock,0.55,"0.45-0.63"
# PLP,0.52,"0.42-0.60"
