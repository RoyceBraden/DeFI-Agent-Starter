# Setting Up Agents on Agentverse

This guide walks you through setting up agents on [Agentverse](https://agentverse.ai).

## Directory Structure

Ensure your project has the following structure:

```
agents/
├── coin-info-agent/
└── fgi-agent/
```

## Configuration

1. **Set Up API Key**

   - For the **FGI (Fear Greed Index) Agent**, update the `.env` file inside `fgi-agent/`.
   - Replace `CMC_API_KEY` with your API key:
     ```
     CMC_API_KEY=your_api_key_here
     ```

2. **Run the Agents**

   - Start both `coin-info-agent` and `fgi-agent` following the instructions provided in their respective directories.

3. **Update `main.py`**
   - After launching the agents, check the logs for their assigned addresses.
   - Replace the placeholder agent addresses in `main.py` with the actual addresses.

## Need Help?

For more details, visit the [Agentverse Documentation](https://fetch.ai/docs/concepts/agent-services/agentverse-intro).
