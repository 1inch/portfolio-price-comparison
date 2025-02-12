import pandas as pd

# Load data
coingecko_file = "data_coingecko.xlsx"
one_inch_file = "data_1inch.xlsx"

# Read data
df_cg = pd.read_excel(coingecko_file)
df_1inch = pd.read_excel(one_inch_file)

# Merge data on token and date
df_merged = pd.merge(df_cg, df_1inch, on=['symbol', 'dt'], suffixes=('_cg', '_1inch'))

# Calculate absolute and percentage deviations
price_columns = ['open', 'high', 'low', 'close']
for col in price_columns:
    df_merged[f'diff_{col}'] = df_merged[f'{col}_cg'] - df_merged[f'{col}_1inch']
    df_merged[f'perc_diff_{col}'] = abs(df_merged[f'diff_{col}']) / df_merged[f'{col}_1inch'] * 100

# Function to calculate MAPE and confidence interval
def mape_confidence_interval(series):
    mean_mape = series.mean()
    conf_interval = 1.96 * series.std() / (len(series) ** 0.5)
    return mean_mape, conf_interval

# Compute MAPE and confidence intervals
mape_results = df_merged.groupby('symbol').agg(
    mape_open=('perc_diff_open', lambda x: mape_confidence_interval(x)),
    mape_close=('perc_diff_close', lambda x: mape_confidence_interval(x))
)

# Unpack tuple values into separate columns
mape_results[['mape_open_value', 'mape_open_ci']] = pd.DataFrame(mape_results['mape_open'].tolist(), index=mape_results.index)
mape_results[['mape_close_value', 'mape_close_ci']] = pd.DataFrame(mape_results['mape_close'].tolist(), index=mape_results.index)
mape_results = mape_results.drop(columns=['mape_open', 'mape_close'])

# Print results
print(mape_results)
