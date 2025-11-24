import pandas as pd
import matplotlib.pyplot as plt
import re

# 读取数据
df = pd.read_csv("/home/wjl/data/DTI_prj/Arch_Lab/写作图相关代码/FusionSmi_项目图/亲和力相关指标作图/11_spearman_ranking_power_targets/spearman_打分函数_casf2016.csv")  # 替换为你的CSV文件路径
df = df.head(20)  # 只取前20名

# 解析置信区间字符串为数值
def parse_interval(interval_str):
    nums = re.findall(r"[-+]?\d*\.\d+|\d+", interval_str)
    print(nums[0], nums[1])
    # 检查是否有 'xerr' must not contain negative values
    if float(nums[0]) < 0 or float(nums[1]) < 0 or float(nums[1])< float(nums[0]):
        raise ValueError(f"Invalid confidence interval values: {nums[0]}, {nums[1]}")
    return [float(nums[0]), float(nums[1])] if len(nums) == 2 else [None, None]

df[["ci_low", "ci_high"]] = df["90% 置信区间 (Confidence Interval)"].apply(parse_interval).tolist()

# 计算误差范围
df["error_low"] = df["ρ (Spearman)"] - df["ci_low"]
df["error_high"] = df["ci_high"] - df["ρ (Spearman)"]

# 按排名顺序逆序排列（上面名次高）
df = df.iloc[::-1]

# 设置颜色（高亮FusionSmi）
colors = ["#F5A623" if x == "FusionSmi" else "#2B5DA3" for x in df["评分函数 (Scoring Function)"]]

# 绘图
plt.figure(figsize=(5, 6))
plt.barh(df["评分函数 (Scoring Function)"], df["ρ (Spearman)"], xerr=[df["error_low"], df["error_high"]],
         color=colors, ecolor="black", capsize=3)

plt.xlabel("Spearman Correlation Coefficient", fontsize=12)
plt.ylabel("")
plt.xlim(0, 1.0)
plt.tight_layout()
# plt.show()
plt.savefig("/home/wjl/data/DTI_prj/Arch_Lab/写作图相关代码/FusionSmi_项目图/亲和力相关指标作图/11_spearman_ranking_power_targets/2_绘制ranking图65.png", dpi=300)
