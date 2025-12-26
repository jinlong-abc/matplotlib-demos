import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

def plot_bar_chart(
    methods,
    values,
    errors=None,
    colors=None,
    highlight_idx=None,
    figsize=(7, 4),
    bar_width=0.65,
    rotation=90,
    fontname="DejaVu Sans",
    font_size=14,
    x_font_size=12,
    y_font_size=12,
    title_font_size=16,
    ylabel="",
    title="",
    ylim=None,
    y_tick_step=None,
    show_values=False,
    value_font_size=13,
    edgecolor="black",
    edgewidth=1.2,
    show_top_spine=False,
    show_right_spine=False,
    show_bottom_spine=True,
    show_left_spine=True,
    grid=False,
    save_path=None,
    dpi=300
):
    """
    绘制带误差棒的柱状图
    
    参数:
    ----------
    methods : list[str]  
        x轴标签（方法名称列表）
    values : list[float]  
        每个方法对应的数值
    errors : list[float], optional  
        误差棒大小
    colors : list[str], optional  
        每个柱子的颜色
    highlight_idx : int, optional  
        需要高亮的柱子索引
    figsize : tuple, optional  
        图像大小
    bar_width : float, optional  
        柱子宽度
    rotation : int, optional  
        x轴标签旋转角度
    fontname : str, optional  
        x轴标签字体
    font_size, x_font_size, y_font_size, title_font_size : int  
        各字体大小
    ylabel, title : str  
        坐标轴和标题
    ylim : tuple, optional  
        y轴范围
    y_tick_step : float, optional  
        y轴刻度间隔
    show_values : bool, optional  
        是否显示柱子数值
    value_font_size : int  
        显示数值字体大小
    edgecolor, edgewidth : str/float  
        柱子边框颜色和宽度
    show_top_spine, show_right_spine, show_bottom_spine, show_left_spine : bool  
        边框可见性
    grid : bool  
        是否显示网格
    save_path : str, optional  
        保存路径
    dpi : int  
        保存分辨率
    """
    x = np.arange(len(methods))
    fig, ax = plt.subplots(figsize=figsize)

    # 绘制柱状图
    bars = ax.bar(
        x, values, 
        width=bar_width, 
        color=colors, 
        edgecolor=edgecolor, 
        linewidth=edgewidth,
        yerr=errors,
        capsize=4
    )

    # 高亮柱子
    if highlight_idx is not None and 0 <= highlight_idx < len(values):
        bars[highlight_idx].set_color("orange")

    # 显示数值
    if show_values:
        for i, val in enumerate(values):
            ax.text(i, val + 0.02, f"{val:.3f}", ha="center", va="bottom",
                    fontsize=value_font_size)

    # x轴
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=rotation, ha="right", fontsize=x_font_size, fontname=fontname)

    # y轴字体
    ax.tick_params(axis='y', labelsize=y_font_size)
    
    # 坐标轴标签与标题
    ax.set_ylabel(ylabel, fontsize=font_size)
    ax.set_title(title, fontsize=title_font_size)

    # 坐标范围
    if ylim is not None:
        ax.set_ylim(ylim)
    
    # y轴刻度间隔
    if y_tick_step is not None:
        ax.yaxis.set_major_locator(MultipleLocator(y_tick_step))
    
    # 网格
    if grid:
        ax.grid(axis="y", linestyle="--", alpha=0.7)

    # 边框可见性
    ax.spines["top"].set_visible(show_top_spine)
    ax.spines["right"].set_visible(show_right_spine)
    ax.spines["bottom"].set_visible(show_bottom_spine)
    ax.spines["left"].set_visible(show_left_spine)

    plt.tight_layout()

    # 保存
    if save_path is not None:
        fig.savefig(save_path, dpi=dpi)
    plt.show()


# methods = ["Pafnucy", "OnionNet", "IGN", "SIGN", "SMINA"]
# rmse_2020 = [1.565, 1.377, 1.392, 1.295, 2.078]
# rmse_err = [0.023, 0.040, 0.020, 0.010, 0.008]
# colors_bars = ["pink", "pink", "pink", "pink", "mediumseagreen"]

# # 找到最佳方法的索引（RMSE最小值）
# best_idx = np.argmin(rmse_2020)

# plot_bar_chart(
#     methods=methods,
#     values=rmse_2020,
#     errors=rmse_err,
#     colors=colors_bars,
#     highlight_idx=best_idx,
#     figsize=(8, 5),
#     ylim=(1.1, 2.2),
#     y_tick_step=0.2,
#     rotation=45,
#     show_values=True,
#     title="RMSE of Different Methods",
#     ylabel="RMSE",
#     save_path="rmse_plot.png"
# )
