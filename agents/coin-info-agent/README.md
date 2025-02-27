![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

**Description**: This AI Agent retrieves current information related to a crypto token/coin.

**Input Data Model**

```
class CoinRequest(BaseModel):
    coin_id: str
```

**Output Data Model**

```
class CoinResponse(BaseModel):
    name: str
    symbol: str
    current_price: float
    market_cap: float
    total_volume: float
    price_change_24h: float
```
