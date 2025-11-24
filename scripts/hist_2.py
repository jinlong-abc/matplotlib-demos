import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# ===============================
# 数据部分
# ===============================
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
    # "mediumseagreen"（草绿色，#3CB371）
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
methods = [
    "Pafnucy", "OnionNet", "IGN", "SIGN",
    "SMINA", "GNINA", "dMASIF", "TankBind",
    "GraphDTA", "TransCPI", "MolTrans", "DrugBAN",
    "DGraphDTA", "WGNN-DTA", "STAMP-DPI", "PSICHIC", "FusionSmi", "FusionSmi*", "FusionSmi**"
]

rmse_2020 = [1.565, 1.377, 1.392, 1.295, 
            2.078, 1.553, 1.528, 1.402, 
            1.568, 1.582, 1.616, 1.436,
            1.582, 1.691, 1.579, 1.336, 1.253, 1.182, 1.167]

rmse_err = [0.023, 0.040, 0.020, 0.010, 0.008, 0.017, 0.030, 0.021, 0.036, 0.034
            , 0.037, 0.007, 0.034, 0.020, 0.026, 0.031, 0.021, 0.0029, 0.033]

colors_bars = [
    "pink", "pink", "pink", "pink",
    "mediumseagreen", "mediumseagreen", "mediumseagreen", "mediumseagreen",
    "skyblue", "skyblue", "skyblue", "skyblue",
    "skyblue", "skyblue", "skyblue", "skyblue", "darkorange", "orange", "navajowhite"
]

# ===============================
# 可调节参数
# ===============================
figsize = (7, 4)        # 图像大小
bar_color = "skyblue"    # 柱子填充颜色
highlight_color = "orange" # 最佳柱子颜色
bar_width = 0.65       # 柱子宽度
rotation = 90         # x轴标签旋转角度
font_size = 14        # 坐标轴字体大小
x_font_size = 12      # x轴标签字体大小
# fontname = "Arial"    # x轴标签字体名称
fontname = "DejaVu Sans"    # x轴标签字体名称
y_font_size = 12      # y轴标签字体大小
title_font_size = 16  # 标题字体大小
ylabel = ""           # y轴标签
title = ""            # 图标题 
grid = False          # 是否显示网格
show_values = False    # 是否在柱子上显示数值标签
value_font_size = 13  # 数值标签字体大小

# 柱子边框
edgecolor = "black"   # 边框颜色（"none" 去掉边框线）
edgewidth = 1.2       # 边框线宽度

# 坐标范围
xlim = None           # x轴范围 (None表示自动)
ylim = (1.1, 2.1)     # y轴范围 (None表示自动)

# 刻度间隔设置
y_tick_step = 0.2   # y 轴刻度间隔
x_tick_step = 1     # x 轴刻度间隔（通常 = 1，方法一个一个排）

# 轴边框可见性
show_top_spine = False     # 是否显示上边框
show_right_spine = False   # 是否显示右边框
show_bottom_spine = True   # 是否显示下边框
show_left_spine = True     # 是否显示左边框

# 每个方法字体颜色（方法名 -> 颜色）
# method_colors = {
#     "Pafnucy": "red",
#     "OnionNet": "blue",
#     "IGN": "green",
#     "SIGN": "purple",
#     "SMINA": "orange",
#     "GNINA": "brown",
#     "dMASIF": "teal",
#     "TankBind": "navy",
#     "GraphDTA": "magenta",
#     "TransCPI": "darkred",
#     "MolTrans": "gold",
#     "DrugBAN": "darkgreen",
#     "DGraphDTA": "black",
#     "WGNN-DTA": "gray",
#     "STAMP-DPI": "pink",
#     "PSICHIC": "cyan"
# }
# 每个方法字体颜色
# method_colors = {
#     "Pafnucy": "pink",
#     "OnionNet": "pink",
#     "IGN": "pink",
#     "SIGN": "pink",
#     "SMINA": "gray",
#     "GNINA": "gray",
#     "dMASIF": "gray",
#     "TankBind": "gray",
#     "GraphDTA": "black",
#     "TransCPI": "black",
#     "MolTrans": "black",
#     "DrugBAN": "black",
#     "DGraphDTA": "black",
#     "WGNN-DTA": "black",
#     "STAMP-DPI": "black",
#     "PSICHIC": "black",
#     "FusionSmi": "black"
# }

# 保存设置
save_path = "rmse_without_decoder9.png"
dpi = 300         # 保存分辨率

# ===============================
# 绘图部分
# ===============================
x = np.arange(len(methods))
fig, ax = plt.subplots(figsize=figsize)

# 柱状图
bars = ax.bar(
    x, rmse_2020, 
    width=bar_width, 
    color=colors_bars, 
    edgecolor=edgecolor, 
    linewidth=edgewidth,
    yerr=rmse_err,       # 加误差棒
    capsize=4            # 误差棒两端的小横线
)

# 高亮最佳
best_idx = np.argmin(rmse_2020)
bars[best_idx].set_color(highlight_color)

# 数值标签
if show_values:
    for i, val in enumerate(rmse_2020):
        ax.text(i, val + 0.02, f"{val:.3f}", ha="center", va="bottom",
                fontsize=value_font_size)

# 坐标轴设置
ax.set_xticks(x)
ax.set_xticklabels(methods, rotation=rotation, ha="right", fontsize=font_size, fontname=fontname)

# 强制清除可能的缓存
plt.draw()

# 设置坐标轴刻度标签字体大小（新增部分）
ax.tick_params(axis='y', labelsize=y_font_size)  # 纵坐标数值字体大小
ax.tick_params(axis='x', labelsize=x_font_size)  # 横坐标标签字体大小

# # 修正后的标签颜色设置 - 通过文本内容匹配而不是索引
# for label in ax.get_xticklabels():
#     text = label.get_text()
#     if text in method_colors:
#         label.set_color(method_colors[text])
#         # 强制设置颜色属性
#         label.set_color(method_colors[text])

# 再次强制刷新
plt.draw()

ax.set_ylabel(ylabel, fontsize=font_size)
ax.set_title(title, fontsize=title_font_size)

# 坐标范围
if xlim is not None:
    ax.set_xlim(xlim)
if ylim is not None:
    ax.set_ylim(ylim)

# 设置刻度间隔
ax.yaxis.set_major_locator(MultipleLocator(y_tick_step))
ax.xaxis.set_major_locator(MultipleLocator(x_tick_step))

# 网格
if grid:
    ax.grid(axis="y", linestyle="--", alpha=0.7)

# 边框可见性
ax.spines["top"].set_visible(show_top_spine)
ax.spines["right"].set_visible(show_right_spine)
ax.spines["bottom"].set_visible(show_bottom_spine)
ax.spines["left"].set_visible(show_left_spine)

plt.tight_layout()
# plt.show()

# 保存前再次确保颜色正确
# for label in ax.get_xticklabels():
#     text = label.get_text()
#     if text in method_colors:
#         label.set_color(method_colors[text])

# 保存
fig.savefig(save_path, dpi=dpi)