def mad_libs():
    print("Let's create a funny story! Please fill in the blanks:\n")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")

    print("\nHere's your story:\n")
    story = f"Yesterday, I went to {place} and saw a {adjective} {noun}. It {verb} {adverb} through the street, and everyone started laughing!"
    print(story)

if __name__ == "__main__":
    mad_libs()
