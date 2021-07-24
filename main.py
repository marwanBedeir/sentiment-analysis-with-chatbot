import bot

if __name__ == '__main__':  # for test
    while True:
        message = input()
        stat, reply = bot.chat(1, message)
        if stat == 0:
            print(reply)
            print('\n')
        else:
            print('Error')

