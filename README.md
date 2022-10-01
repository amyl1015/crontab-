# crontab-

# Cronttab
This is my crontab schdule. As you can see the logs files show the cron jobs work. 
'''
* * * * * /Users/amyliu/Documents/HHA-507/hha-venv/bin/python3 /Users/amyliu/Documents/GitHub/crontab-/app.py >> /Users/amyliu/Documents/GitHub/crontab-/myjob2.log 2> /Users/amyliu/Documents/GitHub/crontab-/myjob1.log 


0 22 * * SUN /Users/amyliu/Documents/HHA-507/hha-venv/bin/python3 /Users/amyliu/Documents/GitHub/crontab-/app.py >> /Users/amyliu/Documents/GitHub/crontab-/myjob.log 2> /Users/amyliu/Documents/GitHub/crontab-/myjob1.log 
 

0 12 * * * /Users/amyliu/Documents/HHA-507/hha-venv/bin/python3 /Users/amyliu/Documents/GitHub/crontab-/app.py >2>&1

59 23 1 */3 * /Users/amyliu/Documents/HHA-507/hha-venv/bin/python3 /Users/amyliu/Documents/GitHub/crontab-/app.py >2>&1
'''
