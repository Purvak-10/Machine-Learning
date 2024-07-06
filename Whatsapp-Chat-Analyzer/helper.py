from urlextract import URLExtract
import pandas as pd
from collections import Counter
import emoji

extractor = URLExtract()


def fetch_stats(selected_user, df):

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    word = []
    for msg in df['message']:
        word.extend(msg.split())

    num_media_messages = df[df['message'].str.contains("image omitted|video omitted|sticker omitted|GIF omitted|This message was deleted.|document omitted",
                                                       case=False, na=False)].shape[0]

    links = []
    for link in df['message']:
        links.extend(extractor.find_urls(link))

    return num_messages, len(word), num_media_messages, len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts()/df.shape[0])*100, 2).reset_index().rename(
        columns={'user': 'name', 'count': 'percent'})

    return x, df


def most_common_words(selected_user, df):

    f = open("stop-words.txt", "r")
    stop_words = f.read()

    if selected_user != 'overall':
        df = df[df["user"] == selected_user]

    temp = df[df['user'] != 'group notification']

    temp = temp[~temp['message'].str.contains('image omitted|video omitted|sticker omitted|GIF omitted|This message was deleted.|document omitted',
                                              case=False, na=False)]

    words = []
    for msg in temp['message']:
        for word in msg.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))

    return most_common_df


def emoji_helper(selected_user, df):
    if selected_user != 'overall':
        df = df[df["user"] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c['emoji'] for c in emoji.emoji_list(message)])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df


def monthly_timeline(selected_user, df):
    if selected_user != 'overall':
        df = df[df["user"] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline


def daily_timeline(selected_user, df):
    if selected_user != 'overall':
        df = df[df["user"] == selected_user]

    df['only_date'] = df['date'].dt.date
    daily_time = df.groupby(['only_date']).count()['message'].reset_index()

    return daily_time


def week_activity_map(selected_user, df):
    if selected_user != 'overall':
        df = df[df["user"] == selected_user]

    return df['day_name'].value_counts()


def month_activity_map(selected_user, df):
    if selected_user != 'overall':
        df = df[df["user"] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user, df):
    if selected_user != 'overall':
        df = df[df["user"] == selected_user]

    activity_heat = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return activity_heat
