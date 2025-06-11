def mad_lib():
    print("***Let's play Madlibs!*** ")
    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_adjective = input("Give me a funny adjective: ")
    random_object = input("Give me a random object: ")
    animal = input("Give me a animal: ")
    action_verb = input("Give me an action verb: ")
    funny_exclamation = input("Give me an  funny exclamation: ")

    story = f"""
    Once upon a time, {name} was walking through {place} when they stumbled upon a {funny_adjective} {random_object}.
    Suddenly, a wild {animal} appeared and started to {action_verb} uncontrollably!
    "{funny_exclamation}!" shouted {name}, as they tried to escape.
    And thus began the most unexpected adventure of their life.
    """

    print("\n Here is your Mad Libs story")
    print(story)

if __name__ == "__main__":
    mad_lib()