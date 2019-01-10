# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
import sys
from you_get import common as youget
from you_get import json_output as json_output_
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory
import xbmc
from urllib.parse import quote,unquote


ADDON = xbmcaddon.Addon()
plugin = routing.Plugin()

@plugin.route('/')
def index():
    addDirectoryItem(plugin.handle, plugin.url_for(
        show_category, quote("https://www.bilibili.com/video/av38301694",safe='')), ListItem("FeiLong"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(
        show_category, quote("https://www.bilibili.com/video/av39523414",safe='')), ListItem("bilibili"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(
        show_category, quote("https://v.youku.com/v_show/id_XNDAwNDI2MDkwMA==.html?spm=a2h1n.8251846.0.0",safe='')), ListItem("youku"), True)
    endOfDirectory(plugin.handle)


@plugin.route('/category/<category_id>')
def show_category(category_id):
    print('cate=>', category_id)
    playVideo(unquote(category_id))

def download_urls(
    urls, title, ext, total_size, output_dir='.', refer=None, merge=True,
    faker=False, headers={}, **kwargs
):
    assert urls
    print(urls)
    url = urls[0]
    for key, value in headers.items():
        print (key,' => ',value)
        if key != "User-Agent":
            url = "%s|%s=%s" % (url,key,quote(value,safe=''))

    playUrl(url)
    return

def playUrl(video_url):
    print ('url => %s' % video_url)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    li = ListItem(path=video_url)
    li.setInfo( type="video", infoLabels={ "Path" : video_url } )
    playlist.add(url=video_url, listitem=li)
    xbmc.Player().play(playlist)

def test_main(**kwargs):
    youget.script_main(youget.any_download, youget.any_download_playlist, **kwargs)

def playVideo(url):
    # test_main()
    extra = {}
    # URLs = ['https://www.youtube.com/watch?v=AnwQAWmGgek']
    # URLs = ['https://www.bilibili.com/video/av38301694']
    URLs = [url]
    # youget.set_socks_proxy("feilong-server.lan:10080")
    youget.download_urls = download_urls
    youget.download_main(
        youget.any_download, youget.any_download_playlist,
        # URLs, args.playlist,
        URLs, False,
        # output_dir=args.output_dir, merge=not args.no_merge,
        output_dir='/tmp/', merge=True,
        info_only=False, json_output=False,
        # password=args.password,
        **extra
    )

def run():
    plugin.run()
