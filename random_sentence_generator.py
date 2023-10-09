import random


def red(text):
    print("\033[91m {}\033[00m" .format(text))


def cyan(text):
    print("\033[96m {}\033[00m" .format(text))
    return ''


def yellow(text):
    print("\033[93m {}\033[00m" .format(text))


def green(text):
    print("\033[92m {}\033[00m" .format(text))


def purple(text):
    print("\033[95m {}\033[00m" .format(text))


def get_random_word(words):
    return random.choice(words)


names = ["Peter", "Michell", "Jane", "Steve", "George", "Ivan"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Yambol"]
verbs = ["eats", "holds", "sees", "plays with", "brings", "delivers"]
verbs_1 = ["eating", "holding", "seeing", "playing with", "bringing", "delivering"]
nouns = ["stones", "a cake", " an apple", " a laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly", "happily"]
details = ["near the river", "at home", "in the park"]

print("Hello, this is your first random sentence: ")

while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    random_verb_1 = get_random_word(verbs_1)
    sentence_type = random.randint(1, 2)
    question_type = random.randint(1, 2)
    color = random.randint(1, 5)
    if sentence_type == 1:
        if color == 1:
            red(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")
        elif color == 2:
            cyan(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")
        elif color == 3:
            yellow(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")
        elif color == 4:
            green(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")
        elif color == 5:
            purple(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")
    elif sentence_type == 2:
        if question_type == 1:
            if color == 1:
                red(f"Is {random_name} from {random_place} {random_adverb} {random_verb_1} {random_noun}?")
            elif color == 2:
                cyan(f"Is {random_name} from {random_place} {random_adverb} {random_verb_1} {random_noun}?")
            elif color == 3:
                yellow(f"Is {random_name} from {random_place} {random_adverb} {random_verb_1} {random_noun}?")
            elif color == 4:
                green(f"Is {random_name} from {random_place} {random_adverb} {random_verb_1} {random_noun}?")
            elif color == 5:
                purple(f"Is {random_name} from {random_place} {random_adverb} {random_verb_1} {random_noun}?")
        elif question_type == 2:
            if color == 1:
                red(f"Who {random_verb} {random_noun} {random_adverb}?")
            elif color == 2:
                cyan(f"Who {random_verb} {random_noun} {random_adverb}?")
            elif color == 3:
                yellow(f"Who {random_verb} {random_noun} {random_adverb}?")
            elif color == 4:
                green(f"Who {random_verb} {random_noun} {random_adverb}?")
            elif color == 5:
                purple(f"Who {random_verb} {random_noun} {random_adverb}?")
    user_input = input('''Press any button to generate a new sentence, or type in "exit" to quit the generator: ''')
    if user_input.lower() == "exit":
        print("Thanks for playing!")
        exit()
