# Fear and Greed Index Agent 📊

![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

## Description

This AI Agent fetches and processes the Crypto Fear and Greed Index from CoinMarketCap, providing insights into market sentiment. The Fear and Greed Index is a valuable tool for understanding market psychology and potential trend changes in the cryptocurrency market.

## Features

- Fetches real-time Fear and Greed Index data
- Provides classification of market sentiment
- Supports historical data retrieval
- Returns structured data using Pydantic models
- Includes timestamp information for each data point

## Input Data Model

```python
class FGIRequest(BaseModel):
    limit: Optional[int] = 1  # Number of historical entries to fetch
```

## Output Data Models

```python
class FearGreedData(BaseModel):
    value: float
    value_classification: str
    timestamp: str

class FGIResponse(BaseModel):
    data: list[FearGreedData]
    status: str
    timestamp: str
```
