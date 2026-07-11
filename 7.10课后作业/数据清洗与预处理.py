import pandas as pd
import numpy as np

print("===== 数据清洗与预处理 - Titanic数据集 =====")

titanic = pd.DataFrame({
    'PassengerId': range(1, 101),
    'Survived': np.random.randint(0, 2, 100),
    'Pclass': np.random.randint(1, 4, 100),
    'Name': [f'乘客{i}' for i in range(1, 101)],
    'Sex': np.random.choice(['male', 'female'], 100),
    'Age': np.random.randint(1, 80, 100).astype(float),
    'SibSp': np.random.randint(0, 5, 100),
    'Parch': np.random.randint(0, 5, 100),
    'Ticket': [f'T{i:04d}' for i in range(1, 101)],
    'Fare': np.random.uniform(5, 500, 100).round(2),
    'Cabin': np.random.choice([f'{c}{n}' for c in 'ABCDEFG' for n in range(1, 21)] + [np.nan], 100),
    'Embarked': np.random.choice(['S', 'C', 'Q', np.nan], 100, p=[0.6, 0.25, 0.12, 0.03])
})

np.random.seed(42)
age_mask = np.random.choice([True, False], 100, p=[0.15, 0.85])
titanic.loc[age_mask, 'Age'] = np.nan

fare_mask = np.random.choice([True, False], 100, p=[0.05, 0.95])
titanic.loc[fare_mask, 'Fare'] = np.nan

titanic = pd.concat([titanic, titanic.iloc[10:15], titanic.iloc[20:23]], ignore_index=True)

print("1. 原始数据概览：")
print(f"   数据形状：{titanic.shape}")
print(f"   缺失值统计：")
print(titanic.isnull().sum())

print("\n2. 识别重复记录：")
duplicate_count = titanic.duplicated().sum()
print(f"   重复记录数：{duplicate_count}")
titanic_clean = titanic.drop_duplicates()
print(f"   去重后数据形状：{titanic_clean.shape}")

print("\n3. 缺失值处理 - 方法对比：")

titanic_method1 = titanic_clean.dropna(subset=['Embarked'])
print(f"   方法1（删除法）- 删除 Embarked 缺失行：{titanic_method1.shape}")

titanic_method2 = titanic_clean.copy()
titanic_method2['Embarked'] = titanic_method2['Embarked'].fillna(titanic_method2['Embarked'].mode()[0])
print(f"   方法2（众数填充）- Embarked 填充众数：{titanic_method2['Embarked'].isnull().sum()} 个缺失")

titanic_method3 = titanic_clean.copy()
titanic_method3['Fare'] = titanic_method3['Fare'].fillna(titanic_method3['Fare'].mean())
print(f"   方法3（均值填充）- Fare 填充均值：{titanic_method3['Fare'].isnull().sum()} 个缺失")

titanic_method4 = titanic_clean.copy()
age_median = titanic_method4.groupby(['Sex', 'Pclass'])['Age'].transform('median')
titanic_method4['Age'] = titanic_method4['Age'].fillna(age_median)
print(f"   方法4（分组中位数填充）- Age 按性别和舱位分组填充：{titanic_method4['Age'].isnull().sum()} 个缺失")

def knn_impute(df, cols, k=5):
    df_copy = df.copy()
    for col in cols:
        if df_copy[col].isnull().sum() == 0:
            continue
        numeric_cols = df_copy.select_dtypes(include=[np.number]).columns.tolist()
        if col in numeric_cols:
            numeric_cols.remove(col)
        if not numeric_cols:
            df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
            continue
        complete_data = df_copy[df_copy[col].notnull()]
        missing_data = df_copy[df_copy[col].isnull()]
        for idx in missing_data.index:
            distances = np.sqrt(((complete_data[numeric_cols] - missing_data.loc[idx, numeric_cols])**2).sum(axis=1))
            nearest = distances.sort_values().head(k)
            df_copy.loc[idx, col] = complete_data.loc[nearest.index, col].mean()
    return df_copy

titanic_method5 = knn_impute(titanic_clean.copy(), ['Age', 'Fare'], k=5)
print(f"   方法5（KNN插值）- Age和Fare使用KNN插值：{titanic_method5[['Age', 'Fare']].isnull().sum().sum()} 个缺失")

print("\n4. 使用最佳策略完成清洗：")
titanic_final = titanic_clean.copy()
titanic_final['Embarked'] = titanic_final['Embarked'].fillna(titanic_final['Embarked'].mode()[0])
titanic_final['Fare'] = titanic_final['Fare'].fillna(titanic_final['Fare'].mean())
age_median = titanic_final.groupby(['Sex', 'Pclass'])['Age'].transform('median')
titanic_final['Age'] = titanic_final['Age'].fillna(age_median)
titanic_final['Cabin'] = titanic_final['Cabin'].fillna('Unknown')
print(f"   清洗后缺失值统计：")
print(titanic_final.isnull().sum())

print("\n5. 数据类型转换和格式标准化：")
titanic_final['Survived'] = titanic_final['Survived'].astype('category')
titanic_final['Pclass'] = titanic_final['Pclass'].astype('category')
titanic_final['Sex'] = titanic_final['Sex'].astype('category')
titanic_final['Embarked'] = titanic_final['Embarked'].astype('category')
titanic_final['Age'] = titanic_final['Age'].round(1)
titanic_final['Fare'] = titanic_final['Fare'].round(2)
print(f"   数据类型：")
print(titanic_final.dtypes)

print("\n6. 特征工程 - 创建衍生特征：")
titanic_final['FamilySize'] = titanic_final['SibSp'] + titanic_final['Parch'] + 1
titanic_final['IsAlone'] = (titanic_final['FamilySize'] == 1).astype(int)
titanic_final['AgeGroup'] = pd.cut(titanic_final['Age'], bins=[0, 12, 18, 60, 100], labels=['儿童', '青少年', '成人', '老人'])
titanic_final['FarePerPerson'] = titanic_final['Fare'] / titanic_final['FamilySize']
print(f"   新增特征后数据形状：{titanic_final.shape}")
print(f"   前5行数据：")
print(titanic_final.head())

print("\n7. 异常值检测与处理：")
fare_iqr = titanic_final['Fare'].quantile(0.75) - titanic_final['Fare'].quantile(0.25)
fare_upper = titanic_final['Fare'].quantile(0.75) + 1.5 * fare_iqr
fare_outliers = titanic_final[titanic_final['Fare'] > fare_upper]
print(f"   Fare 异常值数量：{len(fare_outliers)}")
print(f"   异常值处理：将超过上界的值替换为上界")
titanic_final.loc[titanic_final['Fare'] > fare_upper, 'Fare'] = fare_upper

age_iqr = titanic_final['Age'].quantile(0.75) - titanic_final['Age'].quantile(0.25)
age_upper = titanic_final['Age'].quantile(0.75) + 1.5 * age_iqr
age_lower = titanic_final['Age'].quantile(0.25) - 1.5 * age_iqr
age_outliers = titanic_final[(titanic_final['Age'] > age_upper) | (titanic_final['Age'] < age_lower)]
print(f"   Age 异常值数量：{len(age_outliers)}")

print("\n8. 数据标准化：")
numerical_features = ['Age', 'Fare', 'FamilySize', 'FarePerPerson']
for col in numerical_features:
    mean_val = titanic_final[col].mean()
    std_val = titanic_final[col].std()
    titanic_final[col] = (titanic_final[col] - mean_val) / std_val
print(f"   标准化后前5行数值特征：")
print(titanic_final[numerical_features].head())

print("\n===== 数据清洗完成 =====")
print(f"原始数据：{titanic.shape}")
print(f"清洗后数据：{titanic_final.shape}")
print(f"清洗后缺失值总数：{titanic_final.isnull().sum().sum()}")
titanic_final.to_csv('titanic_cleaned.csv', index=False, encoding='utf-8')
print("清洗后数据已保存为 titanic_cleaned.csv")