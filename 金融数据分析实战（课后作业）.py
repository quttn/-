import numpy as np
import matplotlib.pyplot as plt


def generate_stock_data():
    np.random.seed(42)
    n_days = 252
    base_price = 100
    returns = np.random.randn(n_days) * 0.01 + 0.0005
    prices = base_price * np.cumprod(1 + returns)
    return prices, returns


def stock_price_analysis():
    print("=" * 60)
    print("任务1：股票价格数据分析")
    print("=" * 60)
    
    prices, returns = generate_stock_data()
    
    print(f"数据长度: {len(prices)} 个交易日")
    print(f"开盘价: {prices[0]:.2f}")
    print(f"收盘价: {prices[-1]:.2f}")
    print(f"最高价: {prices.max():.2f}")
    print(f"最低价: {prices.min():.2f}")
    print(f"价格波动范围: {prices.max() - prices.min():.2f}")
    
    cumulative_return = (prices[-1] - prices[0]) / prices[0] * 100
    print(f"累计收益率: {cumulative_return:.2f}%")
    
    plt.figure(figsize=(12, 6))
    plt.plot(prices, label='收盘价', color='blue')
    plt.title('股票价格走势')
    plt.xlabel('交易日')
    plt.ylabel('价格')
    plt.legend()
    plt.grid(True)
    plt.savefig('股票价格走势.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("已保存: 股票价格走势.png")
    print()
    
    return prices, returns


def calculate_returns(prices):
    print("=" * 60)
    print("任务2：收益率计算")
    print("=" * 60)
    
    log_returns = np.log(prices[1:] / prices[:-1])
    simple_returns = np.diff(prices) / prices[:-1]
    
    print(f"对数收益率统计：")
    print(f"  均值: {log_returns.mean():.4f}")
    print(f"  标准差: {log_returns.std():.4f}")
    print(f"  最大值: {log_returns.max():.4f}")
    print(f"  最小值: {log_returns.min():.4f}")
    
    print(f"\n简单收益率统计：")
    print(f"  均值: {simple_returns.mean():.4f}")
    print(f"  标准差: {simple_returns.std():.4f}")
    
    annualized_return = log_returns.mean() * 252
    annualized_volatility = log_returns.std() * np.sqrt(252)
    sharpe_ratio = annualized_return / annualized_volatility
    
    print(f"\n年化指标：")
    print(f"  年化收益率: {annualized_return * 100:.2f}%")
    print(f"  年化波动率: {annualized_volatility * 100:.2f}%")
    print(f"  夏普比率: {sharpe_ratio:.2f}")
    
    plt.figure(figsize=(12, 6))
    plt.hist(log_returns, bins=50, edgecolor='black', alpha=0.7)
    plt.title('对数收益率分布')
    plt.xlabel('收益率')
    plt.ylabel('频率')
    plt.grid(True)
    plt.savefig('收益率分布图.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("已保存: 收益率分布图.png")
    print()
    
    return log_returns


def moving_average_analysis(prices):
    print("=" * 60)
    print("任务3：移动平均线计算")
    print("=" * 60)
    
    windows = [5, 10, 20, 60]
    
    ma_results = {}
    for window in windows:
        cumsum = np.concatenate([[0], np.cumsum(prices)])
        ma = (cumsum[window:] - cumsum[:-window]) / window
        ma_results[window] = ma
        print(f"{window}日移动平均线: 长度={len(ma)}, 均值={ma.mean():.2f}")
    
    plt.figure(figsize=(12, 6))
    plt.plot(prices, label='收盘价', color='gray', alpha=0.5)
    colors = ['red', 'blue', 'green', 'orange']
    for i, (window, ma) in enumerate(ma_results.items()):
        plt.plot(range(window-1, len(prices)), ma, label=f'{window}日均线', color=colors[i])
    
    plt.title('股票价格与移动平均线')
    plt.xlabel('交易日')
    plt.ylabel('价格')
    plt.legend()
    plt.grid(True)
    plt.savefig('移动平均线.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("已保存: 移动平均线.png")
    print()


def portfolio_risk_analysis():
    print("=" * 60)
    print("任务4：投资组合风险分析")
    print("=" * 60)
    
    np.random.seed(42)
    n_stocks = 5
    n_days = 252
    
    stock_names = ['股票A', '股票B', '股票C', '股票D', '股票E']
    returns = np.random.randn(n_stocks, n_days) * 0.01
    returns[0] += 0.001
    returns[1] += 0.0008
    returns[2] -= 0.0002
    returns[3] += 0.0005
    returns[4] += 0.0003
    
    print(f"收益率数据: {n_stocks} 支股票 × {n_days} 个交易日")
    print()
    
    print("各股票年化指标：")
    for i in range(n_stocks):
        annual_return = returns[i].mean() * 252 * 100
        annual_vol = returns[i].std() * np.sqrt(252) * 100
        print(f"  {stock_names[i]}: 收益率={annual_return:.2f}%, 波动率={annual_vol:.2f}%")
    
    print("\n协方差矩阵：")
    cov_matrix = np.cov(returns)
    print(cov_matrix.round(4))
    
    print("\n相关系数矩阵：")
    corr_matrix = np.corrcoef(returns)
    print(corr_matrix.round(4))
    
    weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
    portfolio_return = np.sum(weights * returns.mean(axis=1)) * 252 * 100
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252) * 100
    portfolio_sharpe = (np.sum(weights * returns.mean(axis=1)) * 252) / (np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252))
    
    print(f"\n等权重投资组合：")
    print(f"  组合收益率: {portfolio_return:.2f}%")
    print(f"  组合波动率: {portfolio_volatility:.2f}%")
    print(f"  夏普比率: {portfolio_sharpe:.2f}")
    
    plt.figure(figsize=(8, 6))
    plt.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar(label='相关系数')
    plt.xticks(range(n_stocks), stock_names)
    plt.yticks(range(n_stocks), stock_names)
    for i in range(n_stocks):
        for j in range(n_stocks):
            plt.text(j, i, f'{corr_matrix[i, j]:.2f}', ha='center', va='center', color='white')
    plt.title('股票相关系数热力图')
    plt.savefig('相关系数热力图.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("已保存: 相关系数热力图.png")
    print()


def main():
    prices, _ = stock_price_analysis()
    calculate_returns(prices)
    moving_average_analysis(prices)
    portfolio_risk_analysis()
    
    print("=" * 60)
    print("金融数据分析实战完成！")
    print("生成的可视化图表：")
    print("  - 股票价格走势.png")
    print("  - 收益率分布图.png")
    print("  - 移动平均线.png")
    print("  - 相关系数热力图.png")
    print("=" * 60)


if __name__ == '__main__':
    main()