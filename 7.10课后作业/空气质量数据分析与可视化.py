import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
rcParams['axes.unicode_minus'] = False

print("===== 空气质量数据分析与可视化 =====")

np.random.seed(42)
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='H')[:8760]

months = dates.month
season_effect = np.where(months.isin([12, 1, 2]), 1.5,
                        np.where(months.isin([3, 4, 5, 9, 10, 11]), 1.0, 0.7))

hour_effect = np.where((dates.hour >= 7) & (dates.hour <= 9), 1.3,
                       np.where((dates.hour >= 18) & (dates.hour <= 20), 1.2, 1.0))

base_pm25 = np.random.normal(40, 20, len(dates)) * season_effect * hour_effect
pm25 = np.clip(base_pm25, 5, 300).round(1)

base_pm10 = pm25 * np.random.uniform(1.2, 1.8, len(dates))
pm10 = np.clip(base_pm10, 10, 400).round(1)

so2 = np.random.normal(10, 5, len(dates))
so2 = np.clip(so2, 2, 50).round(1)

no2 = np.random.normal(30, 15, len(dates)) * season_effect
no2 = np.clip(no2, 5, 150).round(1)

co = np.random.normal(0.8, 0.3, len(dates)) * season_effect
co = np.clip(co, 0.2, 3.0).round(2)

o3 = np.random.normal(60, 30, len(dates)) * (2 - season_effect)
o3 = np.clip(o3, 10, 200).round(1)

aq_data = pd.DataFrame({
    'datetime': dates,
    'PM2.5': pm25,
    'PM10': pm10,
    'SO2': so2,
    'NO2': no2,
    'CO': co,
    'O3': o3
})

aq_data['date'] = aq_data['datetime'].dt.date
aq_data['month'] = aq_data['datetime'].dt.month
aq_data['hour'] = aq_data['datetime'].dt.hour
aq_data['season'] = pd.cut(aq_data['month'], bins=[0, 3, 6, 9, 12], labels=['冬季', '春季', '夏季', '秋季'])

print("1. 数据概览：")
print(f"   数据时间范围：{aq_data['datetime'].min()} 至 {aq_data['datetime'].max()}")
print(f"   数据形状：{aq_data.shape}")
print(f"   基本统计量：")
print(aq_data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].describe())

print("\n2. 时间序列特征分析：")
daily_mean = aq_data.groupby('date')[['PM2.5', 'PM10', 'NO2', 'O3']].mean()
print(f"   PM2.5 日均值范围：{daily_mean['PM2.5'].min():.1f} ~ {daily_mean['PM2.5'].max():.1f}")
print(f"   PM2.5 日均值超过 75 的天数：{(daily_mean['PM2.5'] > 75).sum()}")

hourly_mean = aq_data.groupby('hour')[['PM2.5', 'NO2', 'O3']].mean()
print(f"\n   PM2.5 小时均值最高时段：{hourly_mean['PM2.5'].idxmax()}时")
print(f"   O3 小时均值最高时段：{hourly_mean['O3'].idxmax()}时")

print("\n3. 不同污染物的统计指标和相关性：")
corr_matrix = aq_data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()
print("   相关性矩阵：")
print(corr_matrix.round(2))

print("\n4. 绘制时间序列折线图（PM2.5月度趋势）：")
monthly_mean = aq_data.groupby('month')[['PM2.5', 'PM10']].mean()
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_mean.index, monthly_mean['PM2.5'], marker='o', label='PM2.5', color='#e74c3c')
ax.plot(monthly_mean.index, monthly_mean['PM10'], marker='s', label='PM10', color='#3498db')
ax.set_xlabel('月份')
ax.set_ylabel('浓度 (μg/m³)')
ax.set_title('PM2.5 和 PM10 月度变化趋势')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('pm25_pm10_monthly_trend.png', dpi=150, bbox_inches='tight')
print("   已保存：pm25_pm10_monthly_trend.png")

print("\n5. 绘制柱状图（各季节污染物均值）：")
seasonal_mean = aq_data.groupby('season')[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].mean()
fig, ax = plt.subplots(figsize=(12, 6))
seasonal_mean.plot(kind='bar', ax=ax)
ax.set_xlabel('季节')
ax.set_ylabel('浓度')
ax.set_title('各季节污染物平均浓度')
plt.xticks(rotation=0)
plt.savefig('pollutants_seasonal_bar.png', dpi=150, bbox_inches='tight')
print("   已保存：pollutants_seasonal_bar.png")

print("\n6. 绘制散点图（PM2.5与PM10关系）：")
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(aq_data['PM2.5'], aq_data['PM10'], alpha=0.3, s=10)
z = np.polyfit(aq_data['PM2.5'], aq_data['PM10'], 1)
p = np.poly1d(z)
ax.plot(aq_data['PM2.5'], p(aq_data['PM2.5']), "r--", label=f'拟合线: y={z[0]:.2f}x+{z[1]:.2f}')
ax.set_xlabel('PM2.5 (μg/m³)')
ax.set_ylabel('PM10 (μg/m³)')
ax.set_title('PM2.5 与 PM10 相关性散点图')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('pm25_pm10_scatter.png', dpi=150, bbox_inches='tight')
print("   已保存：pm25_pm10_scatter.png")

print("\n7. 绘制热力图（小时-月份 PM2.5 热力图）：")
pivot_data = aq_data.pivot_table(values='PM2.5', index='hour', columns='month', aggfunc='mean')
fig, ax = plt.subplots(figsize=(12, 8))
im = ax.imshow(pivot_data, cmap='YlOrRd', aspect='auto')
ax.set_xlabel('月份')
ax.set_ylabel('小时')
ax.set_title('PM2.5 小时-月份热力图')
ax.set_xticks(range(12))
ax.set_xticklabels(range(1, 13))
ax.set_yticks(range(24))
ax.set_yticklabels(range(24))
plt.colorbar(im, label='PM2.5 浓度 (μg/m³)')
plt.savefig('pm25_heatmap.png', dpi=150, bbox_inches='tight')
print("   已保存：pm25_heatmap.png")

print("\n8. 绘制小时变化箱线图：")
fig, ax = plt.subplots(figsize=(12, 6))
hourly_data = [aq_data[aq_data['hour'] == h]['PM2.5'] for h in range(24)]
ax.boxplot(hourly_data, labels=range(24))
ax.set_xlabel('小时')
ax.set_ylabel('PM2.5 浓度 (μg/m³)')
ax.set_title('PM2.5 小时变化分布')
plt.savefig('pm25_hourly_boxplot.png', dpi=150, bbox_inches='tight')
print("   已保存：pm25_hourly_boxplot.png")

print("\n9. 绘制双Y轴图（PM2.5与O3对比）：")
summer_data = aq_data[aq_data['season'] == '夏季'].groupby('date')[['PM2.5', 'O3']].mean()
winter_data = aq_data[aq_data['season'] == '冬季'].groupby('date')[['PM2.5', 'O3']].mean()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1_twin = ax1.twinx()
ax1.plot(summer_data.index[:30], summer_data['PM2.5'][:30], 'r-', label='PM2.5')
ax1_twin.plot(summer_data.index[:30], summer_data['O3'][:30], 'b-', label='O3')
ax1.set_xlabel('日期')
ax1.set_ylabel('PM2.5 (μg/m³)', color='r')
ax1_twin.set_ylabel('O3 (μg/m³)', color='b')
ax1.set_title('夏季 PM2.5 与 O3 对比（前30天）')
fig.legend(loc='upper right')

ax2_twin = ax2.twinx()
ax2.plot(winter_data.index[:30], winter_data['PM2.5'][:30], 'r-', label='PM2.5')
ax2_twin.plot(winter_data.index[:30], winter_data['O3'][:30], 'b-', label='O3')
ax2.set_xlabel('日期')
ax2.set_ylabel('PM2.5 (μg/m³)', color='r')
ax2_twin.set_ylabel('O3 (μg/m³)', color='b')
ax2.set_title('冬季 PM2.5 与 O3 对比（前30天）')

plt.tight_layout()
plt.savefig('pm25_o3_seasonal_comparison.png', dpi=150, bbox_inches='tight')
print("   已保存：pm25_o3_seasonal_comparison.png")

print("\n10. 季节变化规律分析：")
season_stats = aq_data.groupby('season')['PM2.5'].agg(['mean', 'median', 'max', 'min'])
print("   PM2.5 季节统计：")
print(season_stats.round(1))

print("\n   结论：")
print("   - PM2.5 冬季浓度最高，夏季最低，呈现明显的季节性变化")
print("   - PM2.5 与 PM10 呈强正相关，说明它们可能有相似的污染源")
print("   - O3 与其他污染物呈负相关，夏季浓度高，冬季浓度低")
print("   - PM2.5 存在明显的早晚高峰，与通勤时段一致")

print("\n===== 空气质量分析完成 =====")
print("共生成 6 张可视化图表")