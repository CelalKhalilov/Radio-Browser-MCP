#!/usr/bin/env python3
"""
Test script for Radio Browser MCP functionality
"""

from app import (
    get_radiobrowser_base_urls,
    get_radiobrowser_stats,
    search_stations_by_country,
    search_stations_by_name
)
import json


def test_get_servers():
    """Test getting available Radio Browser servers"""
    print("Testing get_radiobrowser_base_urls()...")
    try:
        servers = get_radiobrowser_base_urls()
        print(f"Found {len(servers)} servers:")
        for server in servers:
            print(f"  - {server}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def test_get_stats():
    """Test getting Radio Browser statistics"""
    print("\nTesting get_radiobrowser_stats()...")
    try:
        stats = get_radiobrowser_stats()
        if "error" in stats:
            print(f"Error: {stats['error']}")
            return False
        
        print("Radio Browser Statistics:")
        print(json.dumps(stats, indent=2))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def test_search_by_country():
    """Test searching stations by country"""
    print("\nTesting search_stations_by_country('US')...")
    try:
        stations = search_stations_by_country('US')
        if isinstance(stations, dict) and "error" in stations:
            print(f"Error: {stations['error']}")
            return False
        
        print(f"Found {len(stations)} stations in US")
        if len(stations) > 0:
            print("First 3 stations:")
            for i, station in enumerate(stations[:3]):
                print(f"  {i+1}. {station.get('name', 'Unknown')} - {station.get('url', 'No URL')}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def test_search_by_name():
    """Test searching stations by name"""
    print("\nTesting search_stations_by_name('BBC')...")
    try:
        stations = search_stations_by_name('BBC')
        if isinstance(stations, dict) and "error" in stations:
            print(f"Error: {stations['error']}")
            return False
        
        print(f"Found {len(stations)} stations matching 'BBC'")
        if len(stations) > 0:
            print("First 3 stations:")
            for i, station in enumerate(stations[:3]):
                print(f"  {i+1}. {station.get('name', 'Unknown')} - {station.get('country', 'Unknown Country')}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    """Run all tests"""
    print("Radio Browser MCP Test Suite")
    print("=" * 40)
    
    tests = [
        test_get_servers,
        test_get_stats,
        test_search_by_country,
        test_search_by_name
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✅ All tests passed! Radio Browser MCP is working correctly.")
    else:
        print("❌ Some tests failed. Please check the errors above.")


if __name__ == "__main__":
    main()
