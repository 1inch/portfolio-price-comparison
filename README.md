**Analysis of Price Data Discrepancies Between Coingecko and 1inch**

### 1. Introduction
This study analyzes the accuracy of cryptocurrency price data for BTC and ETH obtained from two sources: **Coingecko** (CG) and **1inch**. 1inch uses its own data aggregation algorithms, and the objective of this analysis is to assess how much its prices deviate from those of Coingecko, which is considered a benchmark source.

### 2. Methodology
For each day and for each token (BTC, ETH), we collected values for **opening price (open)** and **closing price (close)**. The data were merged based on token and date, and then absolute and relative deviations were calculated between Coingecko and 1inch values:

#### 2.1 Absolute Deviation Calculation
```
diff_x = x_CG - x_1inch
```
where:
- `x_CG` — value of the parameter (open, high, low, close) from Coingecko
- `x_1inch` — value of the parameter from 1inch
- `diff_x` — difference between values

#### 2.2 Relative Deviation Calculation (MAPE)
```
perc_diff_x = abs(x_CG - x_1inch) / x_1inch * 100%
```
The Mean Absolute Percentage Error (**MAPE**) is calculated as the average of the absolute deviations:
```
MAPE = (1/N) * sum(|x_CG,i - x_1inch,i| / x_1inch,i * 100%)
```
where `N` is the number of dates for each token.

### 3. Results
After analyzing the data with **a one-day forward shift** (to reduce discrepancies due to timing differences), the following average MAPE values were obtained:

#### BTC:
- **Open:** 0.23% ± 0.02%
- **Close:** 0.28% ± 0.02%

#### ETH:
- **Open:** 0.23% ± 0.02%
- **Close:** 0.26% ± 0.02%

### 4. Conclusion
The average price deviation between sources was **0.2-0.3%**, which is within acceptable limits for portfolio analysis. The confidence interval indicates that discrepancies are consistently low. This confirms that 1inch data can be used without significant adjustments.
