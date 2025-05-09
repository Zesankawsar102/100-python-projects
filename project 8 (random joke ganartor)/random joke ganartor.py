import pyjokes
def random_joke():
    joke = pyjokes.get_joke()
    print(f"Here's a joke for you : {joke}")
if __name__ == "__main__":
    random_joke()