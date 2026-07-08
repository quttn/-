import numpy as np


def stock_returns():
    print("=" * 60)
    print("任务1：股票收益率计算")
    print("=" * 60)
    
    prices = np.array([100, 102, 105, 103, 107])
    print(f"股价数组: {prices}")
    
    returns = np.log(prices[1:] / prices[:-1])
    print(f"每日对数收益率: {returns.round(4)}")
    
    simple_returns = np.diff(prices) / prices[:-1]
    print(f"每日简单收益率: {simple_returns.round(4)}")
    
    print("\n公式解析：")
    print("对数收益率 = log(prices[t] / prices[t-1])")
    print("简单收益率 = (prices[t] - prices[t-1]) / prices[t-1]")
    print()


def moving_average():
    print("=" * 60)
    print("任务2：移动平均线")
    print("=" * 60)
    
    np.random.seed(42)
    prices = np.cumsum(np.random.randn(100) * 2 + 1) + 100
    print(f"生成100个交易日的随机股价数据")
    print(f"股价范围: {prices.min():.2f} - {prices.max():.2f}")
    print()
    
    window5 = 5
    window20 = 20
    
    ma5_conv = np.convolve(prices, np.ones(window5)/window5, mode='valid')
    ma20_conv = np.convolve(prices, np.ones(window20)/window20, mode='valid')
    
    cumsum = np.concatenate([[0], np.cumsum(prices)])
    ma5_cumsum = (cumsum[window5:] - cumsum[:-window5]) / window5
    ma20_cumsum = (cumsum[window20:] - cumsum[:-window20]) / window20
    
    print(f"5日移动平均线（np.convolve）: 长度 = {len(ma5_conv)}")
    print(f"  前5个值: {ma5_conv[:5].round(2)}")
    print(f"  后5个值: {ma5_conv[-5:].round(2)}")
    print()
    
    print(f"5日移动平均线（np.cumsum）: 长度 = {len(ma5_cumsum)}")
    print(f"  前5个值: {ma5_cumsum[:5].round(2)}")
    print()
    
    print(f"20日移动平均线（np.convolve）: 长度 = {len(ma20_conv)}")
    print(f"  前5个值: {ma20_conv[:5].round(2)}")
    print(f"  后5个值: {ma20_conv[-5:].round(2)}")
    print()
    
    print("验证两种方法结果一致:", np.allclose(ma5_conv, ma5_cumsum))
    print()
    
    print("技巧说明：")
    print("np.convolve(arr, ones(n)/n, mode='valid') - 卷积方式计算MA")
    print("np.cumsum 方式: (cumsum[n:] - cumsum[:-n]) / n - 更高效")
    print()


def risk_analysis():
    print("=" * 60)
    print("任务3：风险分析")
    print("=" * 60)
    
    np.random.seed(42)
    n_stocks = 1000
    n_trading_days = 252
    returns = np.random.randn(n_stocks, n_trading_days) * 0.01
    
    print(f"收益率数据形状: {returns.shape}")
    print(f"  {n_stocks} 支股票 × {n_trading_days} 个交易日")
    print()
    
    daily_std = np.std(returns, axis=1)
    annualized_volatility = daily_std * np.sqrt(252)
    
    print("年化波动率统计：")
    print(f"  平均值: {annualized_volatility.mean():.4f}")
    print(f"  最小值: {annualized_volatility.min():.4f}")
    print(f"  最大值: {annualized_volatility.max():.4f}")
    print(f"  中位数: {np.median(annualized_volatility):.4f}")
    print()
    
    corr_matrix = np.corrcoef(returns)
    
    print("相关系数矩阵统计：")
    print(f"  矩阵形状: {corr_matrix.shape}")
    print(f"  对角线（自相关）: {corr_matrix[0, 0]:.2f}（应为1）")
    print(f"  相关系数范围: [{corr_matrix.min():.4f}, {corr_matrix.max():.4f}]")
    print(f"  平均相关系数: {corr_matrix.mean():.4f}")
    print()
    
    print("关键知识点：")
    print("年化波动率 = 日标准差 × sqrt(252)")
    print("相关系数矩阵: np.corrcoef(returns) - 行向量输入")
    print("对角线为1（自身完全相关），其他值范围[-1, 1]")
    print()


if __name__ == '__main__':
    stock_returns()
    moving_average()
    risk_analysis()
    
    print("=" * 60)
    print("所有金融数据分析任务完成！")
    print("=" * 60)