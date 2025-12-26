import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap_with_colorbar(
    data_dict, 
    row_labels=None, 
    col_labels=None, 
    cmap="coolwarm", 
    annot=True,
    annot_fmt=".3f",
    annot_size=25,
    annot_weight="bold",
    xtick_rotation=30,
    ytick_rotation=0,
    figsize=(8, 8),
    colorbar_figsize=(1, 6),
    heatmap_file="heatmap.png",
    colorbar_file="colorbar.png"
):
    """
    绘制热图和单独的 colorbar，适用于接口调用。
    
    Parameters
    ----------
    data_dict : dict
        字典形式的数据，key为列名，value为列表或数组。
    row_labels : list, optional
        行索引标签。
    col_labels : list, optional
        列索引标签，默认取字典的 key。
    cmap : str
        热图颜色映射。
    annot : bool
        是否在热图上显示数值。
    annot_fmt : str
        数值显示格式。
    annot_size : int
        数值字体大小。
    annot_weight : str
        数值字体粗细。
    xtick_rotation : int
        x轴标签旋转角度。
    ytick_rotation : int
        y轴标签旋转角度。
    figsize : tuple
        热图尺寸。
    colorbar_figsize : tuple
        colorbar 尺寸。
    heatmap_file : str
        热图保存路径。
    colorbar_file : str
        colorbar 保存路径。
    """
    
    # ===== 1. 构建 DataFrame =====
    df = pd.DataFrame(data_dict, index=row_labels)
    
    if col_labels:
        df.columns = col_labels

    # ===== 绘制主热图 =====
    plt.figure(figsize=figsize)
    ax = sns.heatmap(
        df.T,
        annot=annot,
        fmt=annot_fmt,
        cmap=cmap,
        cbar=False,
        annot_kws={"size": annot_size, "weight": annot_weight},
        linewidths=0.5,
        linecolor="gray",
    )

    ax.set_xticklabels(ax.get_xticklabels(), fontsize=annot_size * 0.7, rotation=xtick_rotation)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=annot_size * 0.7, rotation=ytick_rotation)

    plt.tight_layout()
    plt.savefig(heatmap_file, dpi=300, bbox_inches="tight")
    plt.close()

    # ===== 绘制单独 colorbar =====
    fig, ax = plt.subplots(figsize=colorbar_figsize)
    norm = plt.Normalize(vmin=df.values.min(), vmax=df.values.max())
    sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])

    cbar = fig.colorbar(sm, ax=ax)
    cbar.ax.tick_params(labelsize=annot_size * 0.6)
    ax.remove()

    plt.savefig(colorbar_file, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"热图保存为: {heatmap_file}")
    print(f"colorbar保存为: {colorbar_file}")


# ==========================
# 示例调用
# ==========================
if __name__ == "__main__":
    # 示例输入数据
    example_data = {
        "Model_A": [1.23, 1.45, 1.67, 1.89],
        "Model_B": [1.12, 1.34, 1.56, 1.78],
        "Model_C": [1.11, 1.33, 1.55, 1.77],
    }
    row_names = ["Method1", "Method2", "Method3", "Method4"]

    plot_heatmap_with_colorbar(
        data_dict=example_data,
        row_labels=row_names,
        heatmap_file="example_heatmap.png",
        colorbar_file="example_colorbar.png"
    )
