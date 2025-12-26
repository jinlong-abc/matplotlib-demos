import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ============================
# 0. 定义 4PL 模型
# ============================
def four_pl(x, a, b, c, d):
    """四参数逻辑回归 (4PL)"""
    return d + (a - d) / (1 + (x / c)**b)

# ============================
# 1. 绘图函数
# ============================
def plot_cetsa_curve(
    temps,            # 实际温度数组，用于拟合
    con_raw,          # CON 原始强度
    met_raw,          # MET 原始强度
    x_ticks=None,     # 横坐标刻度显示数组（默认与 temps 一致）
    save_path=None    # 保存路径，如果不保存则显示
):
    """
    绘制 CETSA 曲线并拟合 4PL 模型
    返回拟合参数和 Tm
    """

    # 归一化
    CON = con_raw / con_raw[0]
    MET = met_raw / met_raw[0]

    # 拟合 4PL
    popt_CON, _ = curve_fit(four_pl, temps, CON, maxfev=50000)
    popt_MET, _ = curve_fit(four_pl, temps, MET, maxfev=50000)

    # 平滑曲线
    x_fit = np.linspace(temps.min(), temps.max(), 300)
    CON_fit = four_pl(x_fit, *popt_CON)
    MET_fit = four_pl(x_fit, *popt_MET)

    # ============================
    # 绘图参数
    # ============================
    scatter_params_con = {"s": 100, "marker": "s", "linewidth": 4, "alpha": 0.9}
    scatter_params_met = {"s": 100, "marker": "o", "linewidth": 4, "alpha": 0.9}
    line_params = {"linewidth": 5, "linestyle": "-"}
    color_CON = "#83CBEB"
    color_MET = "#FFDA67"
    label_fontsize = 28
    tick_fontsize = 28
    title_fontsize = 16
    legend_fontsize = 12
    spine_width = 3

    # ============================
    # 绘图
    # ============================
    plt.figure(figsize=(8, 6))

    # 原始数据点
    plt.scatter(temps, CON, label="CON raw", color=color_CON, **scatter_params_con)
    plt.scatter(temps, MET, label="MET raw", color=color_MET, **scatter_params_met)

    # 拟合曲线
    plt.plot(x_fit, CON_fit, label="CON - 4PL", color=color_CON, **line_params)
    plt.plot(x_fit, MET_fit, label="MET - 4PL", color=color_MET, **line_params)

    # 坐标轴刻度
    if x_ticks is None:
        x_ticks = temps
    plt.xticks(x_ticks, [str(int(t)) for t in x_ticks], fontsize=tick_fontsize)
    plt.yticks(fontsize=tick_fontsize)
    plt.xlabel("Temperature (°C)", fontsize=label_fontsize)
    plt.ylabel("Normalized Intensity", fontsize=label_fontsize)
    plt.title("CETSA Curve Fitting: 4PL", fontsize=title_fontsize)

    # 网格
    plt.grid(False)

    # 边框样式
    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_linewidth(spine_width)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 图例
    plt.legend(fontsize=legend_fontsize)

    # 保存或显示
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
        plt.close()
    else:
        plt.show()

    # 输出 Tm
    Tm_results = {"CON_Tm": popt_CON[2], "MET_Tm": popt_MET[2]}
    return popt_CON, popt_MET, Tm_results

# ============================
# 2. 示例调用
# ============================
if __name__ == "__main__":
    # 示例数据
    temps = np.array([38, 40, 43, 45, 47, 54, 57, 59, 60])
    x_ticks = temps  # 可以自定义显示的横坐标
    CON_raw = np.array([293580, 280040, 259618, 47553, 34466, 37239, 41036, 31975, 31000])
    MET_raw = np.array([240820, 262222, 210937, 39188, 31055, 34927, 34314, 31662, 30000])

    popt_CON, popt_MET, Tm_results = plot_cetsa_curve(
        temps, CON_raw, MET_raw, x_ticks=x_ticks, save_path="CETSA_Curve.png"
    )

    print("===== Tm Results =====")
    print(f"CON - 4PL Tm: {Tm_results['CON_Tm']:.3f}")
    print(f"MET - 4PL Tm: {Tm_results['MET_Tm']:.3f}")
