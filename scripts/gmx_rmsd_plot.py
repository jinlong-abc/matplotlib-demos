import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# =========================================================
# 🧩【函数区】—— 可复用绘图工具
# =========================================================

def read_xvg(filepath: str) -> pd.DataFrame:
    """
    读取 GROMACS .xvg 文件，忽略注释行
    返回 DataFrame: columns=['Time (ns)', 'RMSD (nm)']
    """
    time, rmsd = [], []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith(('#', '@')) or not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                time.append(float(parts[0]))
                rmsd.append(float(parts[1]))
    return pd.DataFrame({'Time (ns)': time, 'RMSD (nm)': rmsd})


def plot_rmsd(
    df: pd.DataFrame,
    config: dict = None
):
    """
    绘制 RMSD 曲线
    df: DataFrame，包含 'Time (ns)' 和 'RMSD (nm)'
    config: dict，绘图参数，支持覆盖默认值
    """
    # ------------------------
    # 默认参数
    # ------------------------
    default_config = {
        # Seaborn 风格
        "plot_style": "whitegrid",
        "plot_context": "talk",
        "font_scale": 1.2,
        # 图尺寸
        "figsize": (8, 4),
        "dpi": 300,
        # 线条
        "line_color": "#BDBFC0",
        "line_width": 2.5,
        "smooth_color": "#E67E22",
        "smooth_window": 10,
        "show_smooth": False,
        # 坐标轴 & 标题
        "show_title": False,
        "title_text": "Protein-Ligand RMSD Over Time",
        "title_fontsize": 18,
        "xlabel_text": "Time (ns)",
        "ylabel_text": "RMSD (nm)",
        "label_fontsize": 14,
        # 网格
        "show_grid": False,
        "grid_style": "--",
        "grid_alpha": 0.3,
        # 边框
        "spine_color": "#191818",
        "spine_width": 1.5,
        "show_top_spine": False,
        "show_right_spine": False,
        "show_bottom_spine": True,
        "show_left_spine": True,
        # 刻度
        "tick_labelsize": 23,
        "tick_length": 5,
        "tick_width": 1.5,
        "tick_direction": "out",
        "tick_color": "#333333",
        "tick_labelweight": "normal",
        # Y轴范围
        "ylim_auto": False,
        "ylim_range": (4.5, 5.5),
        # 保存/显示
        "save_fig": True,
        "output_file": "rmsd_plot.png",
        "show_fig": False
    }

    # 更新默认参数
    if config:
        default_config.update(config)
    cfg = default_config

    # ------------------------
    # Seaborn & Figure 设置
    # ------------------------
    sns.set_theme(style=cfg["plot_style"], context=cfg["plot_context"], font_scale=cfg["font_scale"])
    plt.figure(figsize=cfg["figsize"])

    # 主曲线
    sns.lineplot(
        data=df,
        x="Time (ns)",
        y="RMSD (nm)",
        color=cfg["line_color"],
        linewidth=cfg["line_width"],
        label="RMSD"
    )

    # 平滑曲线
    if cfg["show_smooth"]:
        df["Smooth"] = df["RMSD (nm)"].rolling(window=cfg["smooth_window"], center=True).mean()
        sns.lineplot(
            data=df,
            x="Time (ns)",
            y="Smooth",
            color=cfg["smooth_color"],
            linewidth=2.0,
            label=f"Smoothed ({cfg['smooth_window']}-pt)"
        )

    # 标题与坐标轴
    if cfg["show_title"]:
        plt.title(cfg["title_text"], fontsize=cfg["title_fontsize"], weight='bold', pad=15)
    plt.xlabel(cfg["xlabel_text"], fontsize=cfg["label_fontsize"])
    plt.ylabel(cfg["ylabel_text"], fontsize=cfg["label_fontsize"])

    # Y轴范围
    if not cfg["ylim_auto"]:
        plt.ylim(cfg["ylim_range"])
    else:
        plt.ylim(0, df["RMSD (nm)"].max() * 1.1)

    # 网格
    plt.grid(cfg["show_grid"], linestyle=cfg["grid_style"], alpha=cfg["grid_alpha"])

    # ------------------------
    # 坐标轴细节
    # ------------------------
    ax = plt.gca()

    # 边框
    for spine_name, spine in ax.spines.items():
        spine.set_visible({
            "top": cfg["show_top_spine"],
            "right": cfg["show_right_spine"],
            "bottom": cfg["show_bottom_spine"],
            "left": cfg["show_left_spine"]
        }[spine_name])
        spine.set_color(cfg["spine_color"])
        spine.set_linewidth(cfg["spine_width"])

    # 刻度
    ax.tick_params(
        axis="both",
        which="major",
        direction=cfg["tick_direction"],
        length=cfg["tick_length"],
        width=cfg["tick_width"],
        colors=cfg["tick_color"],
        labelsize=cfg["tick_labelsize"]
    )
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontweight(cfg["tick_labelweight"])

    plt.tight_layout()
    plt.legend(frameon=False)

    # 保存/显示
    if cfg["save_fig"]:
        plt.savefig(cfg["output_file"], dpi=cfg["dpi"], bbox_inches="tight")
    if cfg["show_fig"]:
        plt.show()


# =========================================================
# 🔹【示例调用】
# =========================================================
if __name__ == "__main__":
    file_path = "/home/./rmsd_protein.xvg"
    df = read_xvg(file_path)

    # 可自定义绘图参数
    custom_config = {
        "show_smooth": True,
        "smooth_window": 20,
        "ylim_auto": True,
        "output_file": "rmsd_plot_ACTN4_2.png",
        "show_fig": True
    }

    plot_rmsd(df, custom_config)
