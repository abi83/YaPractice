# Calculator settings
allow_over_limit = False
over_limit_action = 'wrn'
# 'wrn' option allows to make new record with alert
# 'err' option runs RunTimeError if over limit

# Record.comment settings

max_length = 50

too_long_comment_action = 'cut'
# 'cut' option cuts input_comment to max_length limit silently. Default
# 'wrn' option cuts input_comment to max_length limit with a message
# 'ign' option ignores max_length limit
# 'err' option raises ValueError

# Record.date settings

input_date_possibility = 30

incredible_date_action = 'sln'
# 'sln' option sets incredible_date as today silently(default)
# 'wrn' option sets incredible_date as today with a warning message
# 'err' option raises ValueError if input_date not in allowed period
