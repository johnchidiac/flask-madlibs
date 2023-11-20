"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        print(self.template)

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


mad_libs = [
    {
        "title": "The Mysterious Adventure",
        "prompts": ["adjective", "noun", "animal", "object", "plural_noun", "place", "silly_word"],
        "story": "Once upon a time, in a {adjective} kingdom far away, a {noun} decided to go on an adventure. They packed their {noun} and set off into the {adjective} forest. Along the way, they met a {adjective} {animal}. The {animal} gave them a {adjective} {object} that was said to grant {plural_noun}. But to activate it, they first had to find the {adjective} {place} and say the magic words, '{silly_word} {silly_word}!'"
    },
    {
        "title": "The Inventors Big Day",
        "prompts": ["adjective", "noun", "verb", "profession", "event", "fictional_city_name", "name"],
        "story": "In the bustling city of {fictional_city_name}, there lived an inventor named {name}. This inventor was known for their {adjective} inventions. One day, they created a {noun} that could {verb}. The news spread quickly, and soon, a {profession} came to see it. Impressed, the {profession} said, 'This is the most {adjective} thing I've seen! We must show it at the {event}!'"
    },
    {
        "title": "The Space Mission",
        "prompts": ["adjective", "made_up_planet_name", "futuristic_sounding_name", "noun", "verb", "space_creature", "plural_noun", "name"],
        "story": "Captain {name} and their crew were about to embark on a mission to the {adjective} planet of {made_up_planet_name}. Their spaceship, the {futuristic_sounding_name}, was equipped with a {adjective} engine and a {noun} that could {verb}. As they approached the planet, they encountered a {adjective} {space_creature}. The creature asked for {plural_noun} in exchange for the secret of the planet's {adjective} {noun}."
    },
    {
        "title": "The Magical School",
        "prompts": ["adjective", "magical_subject", "last_name", "noun", "animal", "made_up_school_name", "silly_phrase"],
        "story": "In a world where magic is real, there's a school for {adjective} wizards and witches called {made_up_school_name}. The most popular class is {magical_subject}, taught by Professor {last_name}. One day, the students were learning how to turn a {noun} into a {noun}. However, something went wrong, and instead, they turned it into a {adjective} {animal}. To fix it, they needed a {noun} and a spell that goes, '{silly_phrase}!'"
    },
    {
        "title": "The Ultimate Cooking Contest",
        "prompts": ["adjective", "food", "mysterious_ingredient", "kitchen_tool", "name"],
        "story": "Chef {name} was competing in the {adjective} Cooking Contest. Their signature dish was a {adjective} {food}. The secret ingredient was {mysterious_ingredient}. As they started cooking, they realized they forgot their {kitchen_tool}. Luckily, a fellow chef lent them a {adjective} {kitchen_tool}. In the end, the judges called their dish '{adjective} and {adjective}!'"
    }
]


