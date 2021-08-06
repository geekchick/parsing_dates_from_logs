from datetime import datetime
 
class ServerLog:
    def read_file(self, filename):
        """
        This function takes a logfile.txt, opens it and reads each line in the file
        """
        with open(filename, "r") as reader:
            loglines =  reader.readlines()
 
        return loglines
 
 
 
    def get_events(self, filename, keyword: str) -> list :
        """
        This function finds the first and last Shutdown initiated event in 
        the logfile.txt and returns a list of the two events
        """
        get_logs = self.read_file(filename)
 
        for event in get_logs:
            if keyword in event:
                first_shutdown_event = event
                break
 
        for event in get_logs[::-1]:
            if keyword in event:
                last_shutdown_event = event
                break
 
 
        return [first_shutdown_event, last_shutdown_event]
 
 
    def get_entries(self, filename, keyword: str) -> str:
        """
        This function loops through the two Shutdown initiated events and 
        converts each to a string. It then searches for the timestamp in 
        the string and adds each to a list. Next, it converts each timestamp
        to a datetime object. Lastly, it returns the first and last entry
        in the file. 
        """
        list_of_shutdown_events = []
        get_shutdown_events = self.get_events(filename, keyword)
 
        for entry in get_shutdown_events:
            string_entry = str(entry)
 
            begin_date_time = string_entry.find(" ", 0)
            end_date_time = string_entry.find(" ", begin_date_time + 1)
            get_date_time = string_entry[begin_date_time + 1:end_date_time]
 
            list_of_shutdown_events.append(get_date_time)
 
        conversion_first_entry = datetime.strptime(list_of_shutdown_events[0], "%Y-%m-%dT%H:%M:%S") 
        conversion_last_entry = datetime.strptime(list_of_shutdown_events[-1], "%Y-%m-%dT%H:%M:%S") 
 
        return conversion_first_entry, conversion_last_entry
 
 
 
    def main(self, filename, keyword: str) -> int:
        """
        This function calculates the timedelta between the two Shutdown initiated events
        """
        first_server_log, last_server_log = self.get_entries(filename, keyword)
        time_between_events = last_server_log - first_server_log
 
        return time_between_events
 
    
if __name__ == "__main__":
    server_log = ServerLog()
    print(server_log.main("logfile.txt", "supybot Shutdown initiated"))