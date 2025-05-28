#!/usr/bin/env python3
"""
Example usage of Radio Browser MCP
This script demonstrates how to use the Radio Browser MCP tools
"""

import asyncio
import sys
import os

# Add the current directory to the path so we can import our server
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import (
    get_radio_stats,
    get_available_servers,
    search_stations_by_country_code,
    search_stations_by_station_name
)


async def demo_radio_browser_mcp():
    """Demonstrate Radio Browser MCP functionality"""
    
    print("🎵 Radio Browser MCP Demo")
    print("=" * 50)
    
    # 1. Get Radio Browser statistics
    print("\n📊 Getting Radio Browser Statistics...")
    stats = await get_radio_stats()
    if "error" not in stats:
        print(f"   📻 Total Stations: {stats.get('stations', 'N/A'):,}")
        print(f"   🌍 Countries: {stats.get('countries', 'N/A')}")
        print(f"   🗣️ Languages: {stats.get('languages', 'N/A')}")
        print(f"   👆 Clicks Last Hour: {stats.get('clicks_last_hour', 'N/A'):,}")
    else:
        print(f"   ❌ Error: {stats['error']}")
    
    # 2. Get available servers
    print("\n🌐 Getting Available Servers...")
    servers = await get_available_servers()
    if "error" not in servers:
        print(f"   Found {len(servers.get('servers', []))} servers:")
        for i, server in enumerate(servers.get('servers', [])[:3], 1):
            print(f"   {i}. {server}")
        if len(servers.get('servers', [])) > 3:
            print(f"   ... and {len(servers['servers']) - 3} more")
    else:
        print(f"   ❌ Error: {servers['error']}")
    
    # 3. Search stations by country (Turkey)
    print("\n🇹🇷 Searching Turkish Radio Stations...")
    tr_stations = await search_stations_by_country_code('TR')
    if isinstance(tr_stations, list) and len(tr_stations) > 0:
        print(f"   Found {len(tr_stations)} Turkish stations")
        print("   Top 5 Turkish stations:")
        for i, station in enumerate(tr_stations[:5], 1):
            name = station.get('name', 'Unknown')
            url = station.get('url', 'No URL')
            print(f"   {i}. {name}")
            print(f"      🔗 {url}")
    else:
        print(f"   ❌ No Turkish stations found or error occurred")
    
    # 4. Search stations by name (BBC)
    print("\n🎙️ Searching BBC Radio Stations...")
    bbc_stations = await search_stations_by_station_name('BBC')
    if isinstance(bbc_stations, list) and len(bbc_stations) > 0:
        print(f"   Found {len(bbc_stations)} BBC stations")
        print("   Top 5 BBC stations:")
        for i, station in enumerate(bbc_stations[:5], 1):
            name = station.get('name', 'Unknown')
            country = station.get('country', 'Unknown')
            print(f"   {i}. {name} ({country})")
    else:
        print(f"   ❌ No BBC stations found or error occurred")
    
    # 5. Search for rock music stations
    print("\n🎸 Searching Rock Music Stations...")
    rock_stations = await search_stations_by_station_name('Rock')
    if isinstance(rock_stations, list) and len(rock_stations) > 0:
        print(f"   Found {len(rock_stations)} rock stations")
        print("   Top 3 rock stations:")
        for i, station in enumerate(rock_stations[:3], 1):
            name = station.get('name', 'Unknown')
            country = station.get('country', 'Unknown')
            tags = station.get('tags', '')
            print(f"   {i}. {name} ({country})")
            if tags:
                print(f"      🏷️ Tags: {tags}")
    else:
        print(f"   ❌ No rock stations found or error occurred")
    
    print("\n✅ Demo completed!")
    print("\n💡 You can now use these tools in your MCP-enabled applications!")


if __name__ == "__main__":
    asyncio.run(demo_radio_browser_mcp())
