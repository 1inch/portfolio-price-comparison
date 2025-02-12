**Analysis of Price Data Discrepancies Between Coingecko and 1inch**

### 1. Introduction
This study analyzes the accuracy of cryptocurrency price data for BTC and ETH obtained from two sources: **Coingecko** (CG) and **1inch**. 1inch uses its own data aggregation algorithms, and the objective of this analysis is to assess how much its prices deviate from those of Coingecko, which is considered a benchmark source.

### 2. Methodology
For each day and for each token (BTC, ETH), we collected values for **opening price (open)** and **closing price (close)**. The data were merged based on token and date, and then absolute and relative deviations were calculated between Coingecko and 1inch values:

#### 2.1 Absolute Deviation Calculation
\[
\text{diff}_{x} = x_{CG} - x_{1inch}
\]
where:
- \( x_{CG} \) — value of the parameter (open, high, low, close) from Coingecko
- \( x_{1inch} \) — value of the parameter from 1inch
- \( \text{diff}_{x} \) — difference between values

#### 2.2 Relative Deviation Calculation (MAPE)
\[
\text{perc\_diff}_{x} = \frac{ |x_{CG} - x_{1inch}| }{ x_{1inch} } \times 100\%
\]
The Mean Absolute Percentage Error (**MAPE**) is calculated as the average of the absolute deviations:
\[
\text{MAPE} = \frac{1}{N} \sum_{i=1}^{N} \frac{ |x_{CG,i} - x_{1inch,i}| }{ x_{1inch,i} } \times 100\%
\]
where \( N \) is the number of dates for each token.

### 3. Results
After analyzing the data, the following average MAPE values were obtained:

#### BTC:
- **Open:** 0.23% ± 0.02%
- **Close:** 0.28% ± 0.02%

#### ETH:
- **Open:** 0.23% ± 0.02%
- **Close:** 0.26% ± 0.02%

### 4. Conclusion
The average price deviation between sources was **0.2-0.3%**, which is within acceptable limits for portfolio analysis. The confidence interval indicates that discrepancies are consistently low. This confirms that 1inch data can be used without significant adjustments.
