def main():


    playlist = ["Boston", "Dracula", "I Knew You", "Hate That I Made You Love Me", "Risk It All"]

    print("---")

    playlist.append("Be By You")
    print(playlist)

    print("---")

    playlist.insert(0, "Bohemian Rhaspody")
    print(playlist)

    print("---")

    playlist.pop(4)
    print(playlist)

    print("---")

    print(playlist.index("Risk It All"))
    print("Number of songs in the playlist:",len(playlist))

    print("---")

    playlist.reverse()
    print(playlist)




if __name__ == "__main__":
    main()
