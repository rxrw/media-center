"""
Searcharr
Sonarr, Radarr & Readarr Telegram Bot
By Todd Roberts
https://github.com/toddrob99/searcharr
"""

# Searcharr Bot
searcharr_password = "wai31415926"  # Used to authenticate as a regular user to add series/movies
searcharr_admin_password = "wai3.1415926"  # Used to authenticate as admin to manage users
searcharr_language = "en-us"  # yml file in the lang folder
searcharr_start_command_aliases = ["start"]  # Override /start command
searcharr_help_command_aliases = ["help"]  # Override /help command
searcharr_users_command_aliases = ["users"]  # Override /users command

# Telegram
tgram_token = "6165107628:AAGGdTgsDY_mPOFn71iS03sMyCHXSGGMemM"  # Telegram Bot Token

# Sonarr
sonarr_enabled = True
sonarr_url = "http://sonarr:8989"  # http://192.168.0.100:8989
sonarr_api_key = "70145d5007334979857603875a944e78"
sonarr_quality_profile_id = ["Any"]  # can be name or id value - include multiple to allow the user to choose
sonarr_add_monitored = True
sonarr_search_on_add = True
sonarr_tag_with_username = True
sonarr_forced_tags = ["searcharr"]  # e.g. ["searcharr", "friends-and-family"] - leave empty for none
sonarr_allow_user_to_select_tags = True
sonarr_user_selectable_tags = []  # e.g. ["custom-tag-1", "custom-tag-2"] - leave empty to let user choose from all tags in Sonarr
sonarr_series_command_aliases = ["series"]  # e.g. ["series", "tv", "t"]
sonarr_series_paths = []  # e.g. ["/tv", "/anime"] - can be full path or id value - leave empty to enable all
sonarr_season_monitor_prompt = False  # False - always monitor all seasons; True - prompt user to select from All, First, or Latest season(s)

# Radarr
radarr_enabled = True
radarr_url = "http://radarr:7878"  # http://192.168.0.100:7878
radarr_api_key = "0beb3a37212844478672db9d29261ee3"
radarr_quality_profile_id = ["Any"]  # can be name or id value - include multiple to allow the user to choose
radarr_add_monitored = True
radarr_search_on_add = True
radarr_tag_with_username = True
radarr_forced_tags = ["searcharr"]  # e.g. ["searcharr", "friends-and-family"] - leave empty for none
radarr_allow_user_to_select_tags = True
radarr_user_selectable_tags = []  # e.g. ["custom-tag-1", "custom-tag-2"] - leave empty to let user choose from all tags in Radarr
radarr_min_availability = "announced"  # options: "announced", "inCinemas", "released"
radarr_movie_command_aliases = ["movie"]  # e.g. ["movie", "mv", "m"]
radarr_movie_paths = []  # e.g. ["/movies", "/other-movies"] - can be full path or id value - leave empty to enable all

# Readarr
readarr_enabled = False
readarr_url = "http://readarr:8787"  # http://192.168.0.100:8787
readarr_api_key = "dcaa1d3755ee40a6958d66916052e3ef"
readarr_quality_profile_id = ["eBook", "Spoken"]  # can be name or id value - include multiple to allow the user to choose
readarr_metadata_profile_id = ["Standard"]  # can be name or id value - include multiple to allow the user to choose
readarr_add_monitored = True
readarr_search_on_add = True
readarr_tag_with_username = True
readarr_forced_tags = ["searcharr"]  # e.g. ["searcharr", "friends-and-family"] - leave empty for none
readarr_allow_user_to_select_tags = True
readarr_user_selectable_tags = []  # e.g. ["custom-tag-1", "custom-tag-2"] - leave empty to let user choose from all tags in Readarr
readarr_book_command_aliases = ["book"]  # e.g. ["book", "bk", "b"]
readarr_book_paths = []  # e.g. ["/books", "/other-books"] - can be full path or id value - leave empty to enable all
