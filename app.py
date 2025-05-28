import socket
import random
import urllib
import urllib.request
import json


def get_radiobrowser_base_urls():
    """
    Get all base urls of all currently available radiobrowser servers

    Returns:
    list: a list of strings
    """
    hosts = []
    try:
        # get all hosts from DNS
        ips = socket.getaddrinfo('all.api.radio-browser.info',
                                 80, 0, 0, socket.IPPROTO_TCP)
        for ip_tupple in ips:
            ip = ip_tupple[4][0]

            # do a reverse lookup on every one of the ips to have a nice name for it
            host_addr = socket.gethostbyaddr(ip)
            # add the name to a list if not already in there
            if host_addr[0] not in hosts:
                hosts.append(host_addr[0])

        # sort list of names
        hosts.sort()
        # add "https://" in front to make it an url
        return list(map(lambda x: "https://" + x, hosts))
    except Exception as e:
        print(f"Error getting radio browser URLs: {e}")
        # Fallback to known servers
        return ["https://de1.api.radio-browser.info", "https://nl1.api.radio-browser.info"]


def download_uri(uri, param):
    """
    Download file with the correct headers set

    Returns:
    a string result
    """
    param_encoded = None
    if param is not None:
        param_encoded = json.dumps(param).encode('utf-8')
        print('Request to ' + uri + ' Params: ' + ','.join(param.keys()) if isinstance(param, dict) else str(param))
    else:
        print('Request to ' + uri)

    req = urllib.request.Request(uri, param_encoded)
    req.add_header('User-Agent', 'RadioBrowserMCP/1.0.0')
    req.add_header('Content-Type', 'application/json')

    try:
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        return data
    except Exception as e:
        print(f"Error downloading from {uri}: {e}")
        raise


def download_radiobrowser(path, param):
    """
    Download file with relative url from a random api server.
    Retry with other api servers if failed.

    Returns:
    a string result
    """
    servers = get_radiobrowser_base_urls()
    random.shuffle(servers)

    for i, server_base in enumerate(servers):
        print('Random server: ' + server_base + ' Try: ' + str(i))
        uri = server_base + path

        try:
            data = download_uri(uri, param)
            return data
        except Exception as e:
            print("Unable to download from api url: " + uri, e)
            if i == len(servers) - 1:  # Last server, re-raise the exception
                raise
            continue

    raise Exception("All radio browser servers failed")


def get_radiobrowser_stats():
    """
    Get Radio Browser statistics

    Returns:
    dict: Statistics about the Radio Browser database
    """
    try:
        stats = download_radiobrowser("/json/stats", None)
        return json.loads(stats)
    except Exception as e:
        return {"error": f"Failed to retrieve stats: {str(e)}"}


def search_stations_by_country(country_code):
    """
    Search radio stations by country code

    Args:
    country_code (str): Two-letter country code (e.g., 'US', 'DE', 'TR')

    Returns:
    list: List of radio stations in the specified country
    """
    try:
        stations = download_radiobrowser(f"/json/stations/bycountrycodeexact/{country_code}", None)
        return json.loads(stations)
    except Exception as e:
        return {"error": f"Failed to retrieve stations for country {country_code}: {str(e)}"}


def search_stations_by_name(name):
    """
    Search radio stations by name

    Args:
    name (str): Name or partial name of the radio station

    Returns:
    list: List of radio stations matching the search term
    """
    try:
        stations = download_radiobrowser("/json/stations/search", {"name": name})
        return json.loads(stations)
    except Exception as e:
        return {"error": f"Failed to search stations by name '{name}': {str(e)}"}
