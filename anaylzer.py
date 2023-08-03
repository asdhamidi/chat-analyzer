import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from wordcloud import WordCloud, STOPWORDS


def create():
    words, MD_time, MD_date, MD_len, name_data = get_data()
    print("Data collected.\nVisualizing...")
    visualize_time(MD_time)
    visualize_date(MD_date)
    len_visualize(MD_len)
    name_visualize(sorted(name_data.items(), key=lambda x: x[1], reverse=True))
    create_word_cloud(words)


def create_word_cloud(words):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=800, height=800, background_color='white',
                          stopwords=stopwords, min_font_size=10).generate(words)
    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


def visualize_time(data):
    # For plotting a plot graph of total messages each day
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(7)
    plt.bar([r for r in data], [data[r]
            for r in data], color='maroon', width=.5)
    plt.ylabel("Number of Messages")
    plt.xlabel("Time of the day->")
    plt.title("Number of Messages over time")
    # plt.savefig("Messages Stats Time.png", dpi=1+500)
    plt.show()


def visualize_date(data):
    # For plotting a plot graph of total messages each day
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(7)
    plt.bar([r for r in data], [data[r] for r in data], color="green")
    plt.ylabel("Number of Messages")
    plt.xlabel("Week->")
    plt.title("Number of Messages over time")
    # plt.savefig("Messages Stats Date.png", dpi=1+500)
    plt.show()


def len_visualize(data):
    # creating the bar plot
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(7)
    plt.bar([r for r in data], [data[r] for r in data], color='blue')
    plt.ylabel("Occurence")
    plt.xlabel("Length of messages->")
    plt.title("Length of Messages vs Occurences")
    # plt.savefig("Messages Length Stats Date.png", dpi=1+500)
    plt.show()


def name_visualize(data):
    # creating the bar plot
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(7)
    plt.bar([r[0] for r in data][:10], [r[1]
            for r in data][:10], color='maroon', width=0.4)
    plt.xticks(np.arange(10), [(r[0]).split(" ")[0] for r in data][:10], color='green',
               rotation=90, fontweight='bold', fontsize='7', horizontalalignment='right')
    plt.ylabel("Number of Messages")
    plt.xlabel("People")
    plt.title("Number of Messages sent by each person")
    # plt.savefig("People Stats.png", dpi=1+500)
    plt.show()


def get_data():
    f = open("data2.txt", "r", encoding="utf8")

    message_time_data = {}
    message_date_data = {}
    message_len_data = {}
    name_data = {}
    words = ""

    print("Gathering data from chat records...")
    data = f.readline()

    while data != "":
        try:
            data = data.split("-")
            details = data[0].strip().split(",")
            name = (data[1].split(":"))[0].strip()
            msg = (data[1].split(":"))[1].strip()
            msg_len = len(msg)

            timedata = details[1].strip()
            datedata = details[0].strip()

            date = datetime.strptime(datedata, "%d/%m/%Y").month
            time = datetime.strptime(timedata, "%I:%M %p").hour
        except:
            data = f.readline()
            continue

        if name not in name_data:
            name_data[name] = 1
        else:
            name_data[name] += 1

        if time in message_time_data:
            message_time_data[time] += 1
        else:
            message_time_data[time] = 1

        if date in message_date_data:
            message_date_data[date] += 1
        else:
            message_date_data[date] = 1

        if 0 < msg_len <= 100 and msg != "<Media omitted>":
            if msg_len in message_len_data:
                message_len_data[msg_len] += 1
            else:
                message_len_data[msg_len] = 1

        for w in msg.split():
            w = w.lower()
            if w not in ["<media", "omitted>", "m", "h"]:
                w = w.strip(".")
                words += " "+w+" "

        data = f.readline()

    return words, message_time_data, message_date_data, message_len_data, name_data


create()
