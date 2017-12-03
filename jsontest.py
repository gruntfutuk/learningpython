   import requests
   import datetime

def get_event(user_key, event_location , start_date, end_date, event_features, fname):

    data_lst = []  # output
    start_year = int(start_date[0:4])
    start_month = int(start_date[4:6])
    start_day = int(start_date[6:])

    end_year = int(end_date[0:4])
    end_month = int(end_date[4:6])
    end_day = int(end_date[6:])

    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)
    step = datetime.timedelta(days=1)

    while start_date <= end_date:

        date = str(start_date.year)
        if start_date.month < 10:
            date += '0' + str(start_date.month)
        else:
            date += str(start_date.month)

        if start_date.day < 10:
            date += '0' + str(start_date.day)
        else:
            date += str(start_date.day)
        date += "00"
        date += "-" + date

        url = "http://api.eventful.com/json/events/search?"
        url += "&app_key=" + user_key
        url += "&location=" + event_location
        url += "&date=" + date
        url += "&page_size=250"
        url += "&sort_order=popularity"
        url += "&sort_direction=descending"
        url += "&q=music"
        url+= "&c=music"

        data = requests.get(url).json()

        try:
            for i in range(len(data["events"]["event"])):
                data_dict = {}
                for feature in event_features:
                    data_dict[feature] = data["events"]["event"][i][feature]
                data_lst.append(data_dict)
        except:
            pass

        print(data_lst)
        start_date += step


def main():

    user_key = ""
    event_location = "Madrid"
    start_date = "20171012"
    end_date = "20171013"
    event_location = event_location.replace("-", " ")
    start_date = start_date
    end_date = end_date
    event_features = ["latitude", "longitude", "start_time"]
    event_features += ["city_name", "title"]
    event_fname = "events.csv"

    get_event(user_key, event_location, start_date, end_date, event_features, event_fname)


if __name__ == '__main__':
    main()
