import re
import pandas as pd


def preprocess(data):
    pattern = r"\[\d{1,2}/\d{1,2}/\d{1,2}, \d{1,2}:\d{1,2}:\d{1,2} [AP]M\] "
    
    message = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    
    new = []
    for les in message:
        cl = les.strip('\n')
        if cl:
            new.append(cl)

    message = new

    ls = []
    for les in dates:
        cl = les.strip('[] \u202f')
        if cl:
            ls.append(cl)

    dates = ls
    
    df = pd.DataFrame({"user_message": message, "date": dates})
    df['date'] = pd.to_datetime(df["date"], format="%d/%m/%y, %I:%M:%S %p")

    user = []
    msg = []
    reg = r'^([^:]+):\s'

    for l in df['user_message']:
        match = re.match(reg, l)
        if match:
            user.append(match.group(1))
            msg.append(l[len(match.group(0)):])
        else:
            user.append('group notification')
            msg.append(l)

    df['user'] = user
    df['message'] = msg
    df.drop(columns=['user_message'], inplace=True)
    
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day_name'] = df['date'].dt.day_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for h in df[['day_name', 'hour']]['hour']:
        if h == 23:
            period.append(str(h) + "-" + str('00'))
        elif h == 0:
            period.append(str('00') + "-" + str(h + 1))
        else:
            period.append(str(h) + "-" + str(h + 1))

    df['period'] = period
    return df
