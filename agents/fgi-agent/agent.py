import os
from uagents import Agent, Context
from pydantic import BaseModel
import requests
from datetime import datetime
from typing import Optional

agent = Agent()

class FGIRequest(BaseModel):
    limit: Optional[int] = 1

class FearGreedData(BaseModel):
    value: float
    value_classification: str
    timestamp: str

class FGIResponse(BaseModel):
    data: list[FearGreedData]
    status: str
    timestamp: str

def get_fear_and_greed_index(limit: int = 1) -> FGIResponse:
    """Fetch Fear and Greed index data from CoinMarketCap API"""
    url = "https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical"
    api_key = os.getenv("CMC_API_KEY")
    
    headers = {
        "X-CMC_PRO_API_KEY": api_key
    }
    
    params = {
        "limit": limit
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        raw_data = response.json()
        fear_greed_data = []
        
        for entry in raw_data["data"]:
            data = FearGreedData(
                value=entry["value"],
                value_classification=entry["value_classification"],
                timestamp=entry["timestamp"]
            )
            fear_greed_data.append(data)
        
        return FGIResponse(
            data=fear_greed_data,
            status="success",
            timestamp=datetime.utcnow().isoformat()
        )
    else:
        raise Exception(f"Error fetching data: {response.json()['status']['error_message']}")

async def process_response(ctx: Context, msg: FGIRequest) -> FGIResponse:
    """Process the request and return formatted response"""
    fear_greed_data = get_fear_and_greed_index(msg.limit)
    
    for entry in fear_greed_data.data:
        ctx.logger.info(f"Fear and Greed Index: {entry.value}")
        ctx.logger.info(f"Classification: {entry.value_classification}")
        ctx.logger.info(f"Timestamp: {entry.timestamp}")
    
    return fear_greed_data

@agent.on_message(model=FGIRequest)
async def handle_message(ctx: Context, sender: str, msg: FGIRequest):
    """Handle incoming messages requesting Fear and Greed index data"""
    ctx.logger.info(f"Received message from {sender}: FGIRequest for {msg.limit} entries")
    
    response = await process_response(ctx, msg)
    await ctx.send(sender, response)
    
    return response

@agent.on_event("startup")
async def startup(ctx: Context):
    """Initialize agent with a test request"""
    ctx.logger.info(f"Hello, I'm a Fear and Greed Index agent and my address is {ctx.agent.address}.")
    dummy_request = FGIRequest(limit=1)
    await process_response(ctx, dummy_request)

if __name__ == "__main__":
    agent.run()