# myFirstAgent

This is my first project exploring AI agents using LangChain and LangGraph. As a beginner in AI development, I'm building intelligent agents that can perform tasks autonomously. The project includes LangChain-based agents for general tasks and Discord management, as well as LangGraph examples for state management with memory and database persistence.

## Features

### First Agent (first_agent.py)
A basic AI agent with the following tools:
- **get_weather(city)**: Returns a mock weather response for any city.
- **print_message(message)**: Prints a message to the console.

Example usage: Ask the agent to print the weather in a city.

### Discord Manager (discord_manager.py)
An AI agent for managing Discord server channels with these tools:
- **get_guild_channels()**: Retrieves all channels in the guild.
- **create_channel(name, parent_id="", position=0)**: Creates a text channel with optional category and position.
- **modify_channel(channel_id, name=None, parent_id=None, position=None)**: Modifies channel properties.
- **create_category(name, position=0)**: Creates a category channel.
- **create_forum(name, position=0)**: Creates a forum channel.
- **create_public_thread(parent_id, name, position=0)**: Creates a public thread in a channel.
- **read_channel_messages(channel_id, limit=10)**: Retrieves recent messages from a channel.

Example usage: Restructure a Discord server into a travel group by renaming and organizing channels.

## LangGraph State Management

Examples demonstrating state persistence in LangGraph agents:

### State Memory (state_memory.py)
Uses in-memory checkpointing to maintain state across invocations within the same session.

### State Database (state_db.py)
Uses PostgreSQL for persistent state storage, allowing state to survive across sessions and restarts.

## Setup

1. Clone this repository.
2. Install dependencies:
   ```
   pip install langchain langchain-xai langchain-anthropic langgraph psycopg2-binary requests python-dotenv
   ```
3. Set API keys:
   - For first_agent.py: `export ANTHROPIC_API_KEY=your_anthropic_api_key`
   - For discord_manager.py: `export XAI_API_KEY=your_xai_api_key`
   - For state_db.py: `export POSTGRES_DB_URI=your_postgresql_connection_string`
4. For discord_manager.py:
   - Set your Discord bot token in the `DISCORD_BOT_TOKEN` environment variable (via .env or export).
   - Set your guild ID in the `DISCORD_GUILD_ID` environment variable.
   - Ensure your bot has the necessary permissions (MANAGE_CHANNELS, VIEW_CHANNEL, READ_MESSAGE_HISTORY, etc.).

## Running

- Run First Agent: `python langchain/first_agent.py`
- Run Discord Manager: `python langchain/discord_manager.py`
- Run State Memory Example: `python langgraph/state_memory.py`
- Run State Database Example: `python langgraph/state_db.py` (requires PostgreSQL setup)

## Notes

- This is a learning project, so code may not be production-ready.
- Be cautious with Discord API calls, especially deletions.
- Requires valid API keys for Anthropic, XAI, and PostgreSQL for full functionality.
- The LangGraph examples demonstrate basic state management concepts.

## What I've Learned

Through this project, I've gained hands-on experience with:

- **LangChain**: Building agents with tools and chains for real-world interactions.
- **LangGraph**: Implementing stateful workflows with checkpoints for memory and persistence.
- **API Integrations**: Connecting agents to external services like Discord and databases.
- **Best Practices**: Environment variable management, error handling, and modular code structure.

This is just the beginning of my AI journey, and I'm excited to build more complex agents!

This is just the beginning of my AI journey, and I'm excited to build more complex agents!

## License

MIT License