# plugin.common.youget
> warning: python3 only!

## info
this is a video parse plugin,you can easy use this plugin to play the video which you-get supported.

## kodi plugin dev demo

```
def playUrl(video_url):
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    li = xbmcgui.ListItem(path=video_url)
    li.setInfo( type="video", infoLabels={ "Path" : video_url } )
    playlist.add(url=video_url, listitem=li)
    xbmc.Player().play(playlist)

playUrl("plugin://plugin.common.youget/play/" + quote("https://www.bilibili.com/video/av38301694",safe=''))
```
Don't forget add `requires` in your `addon.xml`
