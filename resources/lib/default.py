# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import xbmcplugin
import os
from xbmcaddon import Addon

addon = Addon('script.idealkooks.searchpro')

def get_setting(id, default=None):
    """Helper function to retrieve settings from settings.xml."""
    return addon.getSetting(id) if addon.getSetting(id) else default

def search_files(search_term, search_dirs, file_extensions):
    """Search files in given directories."""
    results = []
    for dir in search_dirs:
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(tuple(file_extensions)):
                    file_path = os.path.join(root, file)
                    if search_term.lower() in file.lower():
                        results.append(file_path)
    return results

def search_addons(search_term, addon_dirs):
    """Search installed addons."""
    results = []
    for addon_dir in addon_dirs:
        addon_path = os.path.join(xbmc.translatePath('special://home/addons'), addon_dir)
        if os.path.isdir(addon_path):
            for root, dirs, files in os.walk(addon_path):
                for file in files:
                    if search_term.lower() in file.lower():
                        results.append(os.path.join(root, file))
    return results

def show_results(results):
    """Display the search results in Kodi."""
    if results:
        for result in results:
            list_item = xbmcgui.ListItem(label=result)
            xbmcplugin.addDirectoryItem(handle=addon.getAddonInfo('id'), url=result, listitem=list_item)
        xbmcplugin.endOfDirectory(addon.getAddonInfo('id'))
    else:
        xbmcgui.Dialog().notification('Search Complete', 'No results found.')

def main():
    search_term = xbmcgui.Dialog().input('Enter Search Term')
    if not search_term:
        xbmcgui.Dialog().notification('Error', 'No search term entered.')
        return

    # Retrieve settings
    search_files_enabled = get_setting('search_files', 'true') == 'true'
    search_addons_enabled = get_setting('search_addons', 'true') == 'true'
    file_extensions = get_setting('file_extensions', 'txt,log,xml').split(',')
    addon_dirs = get_setting('addon_directories', 'scripts,plugins').split(',')
    
    results = []

    if search_files_enabled:
        search_dirs = [xbmc.translatePath('special://home/'), xbmc.translatePath('special://profile/')]  # Common Kodi directories
        results.extend(search_files(search_term, search_dirs, file_extensions))
    
    if search_addons_enabled:
        results.extend(search_addons(search_term, addon_dirs))

    show_results(results)

if __name__ == '__main__':
    main()
