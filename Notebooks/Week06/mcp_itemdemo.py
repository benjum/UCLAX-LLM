from mcp.server.fastmcp import FastMCP
import subprocess
from requests import get
from langchain_community.tools import DuckDuckGoSearchResults

mcp = FastMCP("mcp_server")
duckduck_client = DuckDuckGoSearchResults()

# MCP Tool for searching web
@mcp.tool(
    name="duckduck",
    description="A web search engine. Use this to as a search engine for general queries."
)
def web_search(query):
    results = duckduck_client.run(query)
    return results
    

# MCP Resource for README on langchain-mcp-adapters
# The resource requires a uri: A string defining the resource's unique identifier (e.g., data://config, weather://{city}
@mcp.resource(
    uri="github://langchain-ai/langchain-mcp-adapters/blob/main/README.md",
    name="langchain-mcp-adapters README",
    description="Resource for accessing langchain-ai/langchain-mcp-adapters/README.md file"
)
def github_file():
    url = f"https://raw.githubusercontent.com/langchain-ai/langchain-mcp-adapters/refs/heads/main/README.md"
    try:
        resp = get(url)
        return resp.text
    except Exception as e:
        return f"Error: {str(e)}"


# MCP Prompt template
@mcp.prompt(
    name="langchain-ai prompt",
    description="Analyze data from a langchain-ai repo file with comprehensive insights"
)
def prompt():
    return """
    You are a helpful assistant that answers user questions about LangChain, LangGraph and LangSmith.

    You can use the following tools/resources to answer user questions:
    - web_search: Search the web for information
    - github_file: Access the langchain-ai repo files

    If the user asks a question that is not related to LangChain, LangGraph or LangSmith, you should say "I'm sorry, I can only answer questions about LangChain, LangGraph and LangSmith."

    You may try multiple tool and resource calls to answer the user's question.

    You may also ask clarifying questions to the user to better understand their question.
    """


if __name__ == "__main__":
    mcp.run(transport="stdio")
