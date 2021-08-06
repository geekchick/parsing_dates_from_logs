# Parsing Dates from Logs

In this code we will look at this small server log finding the first and last system shutdown events:

INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.

The time between these two events are calculated. 
First extract the timestamps from the log entries and convert them to datetime objects. 
Then use datetime.timedelta to calculate the time difference between them.

Assume the logs are sorted in ascending order. 
