# one place for strings, functions, and dicts

rss_file_name_twitch = 'libs/feed_twitch.rss'

### call a channel by name for the rss feed - make this into a dict later
twitch_channel = 'xqcow'
# twitch_channel = 'brrrake'
# twitch_channel = 'charlesleclerc'
# twitch_channel = 'GR63'
# twitch_channel = 'landonorris'
# twitch_channel = 'MaxVerstappen'
twitch_channel_list = [
    # 'MaxVerstappen',
    # 'landonorris',
    'brrrake',
    # 'keffals',
    'trashfuturepodcast']

### define RSS data
rss_feed_gen = 'https://twitchrss.appspot.com/vod/'

### define yt items
## yt RSS
rss_feed_gen_yt = 'https://www.youtube.com/feeds/videos.xml?channel_id='
yt_channel_list = {
    'vlogbrothers' : 'UCGaVdbSav8xWuFWTadK6loA',
    'thephilosophytube' : 'UC2PA-AKmVpU6NKCGtZq_rKQ'
}
