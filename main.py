import wordcloud_creator as w

running = True

with open("./input.txt", "w") as file:
        file.write("")

while running:
    i = input("Copy your text, which will be used for building a wordcloud and paste your txt conten with right click and use the paste option. By the way: your data will be only visible for you!\nText:")

    with open("./input.txt", "a") as file:
        file.write(i)

    w.create_wordcloud()

    print("Now you can download the png image, look by the show files.")

