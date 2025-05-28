from mcp.server.fastmcp import FastMCP
from app import (
    get_radiobrowser_base_urls,
    get_radiobrowser_stats,
    search_stations_by_country,
    search_stations_by_name
)

# Initialize MCP server
mcp = FastMCP("radio-browser-mcp")

@mcp.tool()
async def get_radio_stats() -> dict:
    """
    Get Radio Browser statistics including total number of stations, countries, and other metrics.

    Returns:
        dict: Statistics about the Radio Browser database
    """
    result = get_radiobrowser_stats()
    return result

@mcp.tool()
async def get_available_servers() -> list:
    """
    Get list of all available Radio Browser API servers.

    Returns:
        list: List of Radio Browser server URLs
    """
    try:
        servers = get_radiobrowser_base_urls()
        return {"servers": servers}
    except Exception as e:
        return {"error": f"Failed to retrieve servers: {str(e)}"}

@mcp.tool()
async def search_stations_by_country_code(country_code: str) -> list:
    """
    Search radio stations by country code.

    Args:
        country_code (str): Two-letter country code (e.g., 'US', 'DE', 'TR', 'GB', 'FR')

    Returns:
        list: List of radio stations in the specified country
    """
    result = search_stations_by_country(country_code.upper())
    return result

@mcp.tool()
async def search_stations_by_station_name(name: str) -> list:
    """
    Search radio stations by name or partial name.

    Args:
        name (str): Name or partial name of the radio station to search for

    Returns:
        list: List of radio stations matching the search term
    """
    result = search_stations_by_name(name)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")