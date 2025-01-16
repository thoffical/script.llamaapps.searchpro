import xbmc
import xbmcgui
import xbmcaddon
import json

# Get the addon settings
addon = xbmcaddon.Addon()
search_movies = addon.getSetting("search_movies") == "true"
search_tvshows = addon.getSetting("search_tvshows") == "true"
search_music = addon.getSetting("search_music") == "true"
search_videos = addon.getSetting("search_videos") == "true"
search_addons = addon.getSetting("search_addons") == "true"

def search(query):
    results = []
    if search_movies:
        results.extend(search_movies(query))
    if search_tvshows:
        results.extend(search_tvshows(query))
    if search_music:
        results.extend(search_music(query))
    if search_videos:
        results.extend(search_videos(query))
    if search_addons:
        results.extend(search_addons(query))
    return results

def search_movies(query):
    # Search movies
    xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovies", "params": {"filter": {"field": "title", "operator": "contains", "value": "%s"}}}' % query)
    response = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovies", "params": {"filter": {"field": "title", "operator": "contains", "value": "%s"}}}' % query)
    response = json.loads(response)
    results = []
    for movie in response["result"]["movies"]:
        results.append({"label": movie["title"], "type": "movie", "id": movie["movieid"]})
    return results

def search_tvshows(query):
    # Search TV shows
    xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShows", "params": {"filter": {"field": "title", "operator": "contains", "value": "%s"}}}' % query)
    response = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShows", "params": {"filter": {"field": "title", "operator": "contains", "value": "%s"}}}' % query)
    response = json.loads(response)
    results = []
    for tvshow in response["result"]["tvshows"]:
        results.append({"label": tvshow["title"], "type": "tvshow", "id": tvshow["tvshowid"]})
    return results

def search_music(query):
    # Search music
    xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "AudioLibrary.GetSongs", "params": {"filter": {"field": "title", "operator": "contains", "value": "%s"}}}' % query)
    response = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "AudioLibrary.GetSongs", "params": {"filter": {"field": "title", "operator": "contains", "value": "%s"}}}' % query)
    response = json.loads(response)
    results = []
    for song in response["result"]["songs"]:
        results.append({"label": song["title"], "type
