messages = ['ammar', 'osman', 'ali', 'alim']
sent_messages = []

def show_messages(txt):
    for message in messages:
        print(f" Showing {message.title()}")


def send_messages(messages, sent_messages):
    while messages:
        for message in messages:
            name = messages.pop()
            sent_messages.append(name)
            # print(sent_messages)





show_messages(messages)
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)