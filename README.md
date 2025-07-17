[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/celalkhalilov-radio-browser-mcp-badge.png)](https://mseep.ai/app/celalkhalilov-radio-browser-mcp)

# Radio Browser MCP

A Model Context Protocol (MCP) server that provides access to the Radio Browser API, allowing you to search and discover internet radio stations from around the world.

## Features

The Radio Browser MCP provides the following tools:

### 🔧 Available Tools

1. **`get_radio_stats()`**
   - Get comprehensive statistics about the Radio Browser database
   - Returns information about total stations, countries, languages, and more

2. **`get_available_servers()`**
   - Get a list of all available Radio Browser API servers
   - Useful for checking server availability and load balancing

3. **`search_stations_by_country_code(country_code)`**
   - Search radio stations by two-letter country code
   - Examples: 'US', 'DE', 'TR', 'GB', 'FR', 'JP'

4. **`search_stations_by_station_name(name)`**
   - Search radio stations by name or partial name
   - Examples: 'BBC', 'NPR', 'Classic', 'Rock'

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the MCP server:
```bash
python server.py
```

## Usage Examples

### Getting Radio Browser Statistics
```python
# Returns comprehensive stats about the database
stats = await get_radio_stats()
print(f"Total stations: {stats['stations']}")
print(f"Total countries: {stats['countries']}")
```

### Searching Stations by Country
```python
# Find all radio stations in Turkey
stations = await search_stations_by_country_code('TR')
for station in stations[:5]:  # Show first 5
    print(f"{station['name']} - {station['url']}")
```

### Searching Stations by Name
```python
# Find BBC radio stations
bbc_stations = await search_stations_by_station_name('BBC')
for station in bbc_stations:
    print(f"{station['name']} - {station['country']}")
```

## Testing

Run the test script to verify functionality:
```bash
python test_radio_browser.py
```

## API Information

This MCP server uses the Radio Browser API (https://www.radio-browser.info/), which is a free and open-source database of internet radio stations.

### Key Features of Radio Browser API:
- Free to use, no API key required
- Comprehensive database with thousands of stations worldwide
- Real-time data with regular updates
- Multiple server endpoints for reliability
- Rich metadata including genres, languages, countries, and more

## File Structure

- `server.py` - Main MCP server implementation
- `app.py` - Radio Browser API integration functions
- `test_radio_browser.py` - Test suite for functionality verification
- `requirements.txt` - Python dependencies
- `smithery.yaml` - MCP configuration for Smithery

## Error Handling

The MCP server includes robust error handling:
- Automatic server failover if one Radio Browser server is down
- Graceful error messages for network issues
- Fallback to known servers if DNS lookup fails

## Contributing

Feel free to contribute by:
- Adding new search methods (by genre, language, etc.)
- Improving error handling
- Adding more comprehensive tests
- Optimizing performance

## License

This project is open source. The Radio Browser API is also free and open source.
