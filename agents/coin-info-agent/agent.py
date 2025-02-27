import os
from uagents import Agent, Context
from pydantic import BaseModel
import requests

agent = Agent()

class CoinRequest(BaseModel):
    coin_id: str

class CoinResponse(BaseModel):
    name: str
    symbol: str
    current_price: float
    market_cap: float
    total_volume: float
    price_change_24h: float

def get_crypto_info(coin_id: str) -> CoinResponse:
    """Fetch cryptocurrency information from CoinGecko API"""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        return Response(
            name=data['name'],
            symbol=data['symbol'].upper(),
            current_price=data['market_data']['current_price']['usd'],
            market_cap=data['market_data']['market_cap']['usd'],
            total_volume=data['market_data']['total_volume']['usd'],
            price_change_24h=data['market_data']['price_change_percentage_24h']
        )
    else:
        raise Exception(f"Failed to get crypto info: {response.text}")

async def process_response(ctx: Context, msg: CoinRequest) -> CoinResponse:
    """Process the crypto request and return formatted response"""
    crypto_data = get_crypto_info(msg.coin_id)
    ctx.logger.info(f"Crypto data: {crypto_data}")
    return crypto_data

@agent.on_message(model=CoinRequest)
async def handle_message(ctx: Context, sender: str, msg: CoinRequest):
    """Handle incoming messages requesting crypto information"""
    ctx.logger.info(f"{msg}")
    ctx.logger.info(f"Received message from {sender}: {msg.coin_id}")
    
    response = await process_response(ctx, msg)
    '''
    response = CoinResponse(
        name="test",
        symbol="TEST",
        current_price=3.9,
        market_cap=1.0,
        total_volume=1.0,
        price_change_24h=1.0
    )
    '''
    
    await ctx.send(sender, response)
    
    return response

@agent.on_event("startup")
async def startup(ctx: Context):
    """Initialize agent with a test request for Bitcoin data"""
    ctx.logger.info(f"Hello, I'm a crypto agent and my address is {ctx.agent.address}.")
    #dummy_request = Request(coin_id="bitcoin")
    #await process_response(ctx, dummy_request)

if __name__ == "__main__":
    agent.run()