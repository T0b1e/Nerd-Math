import random

quotes = (
"“Be yourself; everyone else is already taken.” ― Oscar Wilde",
"“Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.”― Albert Einstein",
"“So many books, so little time.” ― Frank Zappa",
"“A room without books is like a body without a soul.” ― Marcus Tullius Cicero",
"“Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.”"
)

def generate_quotes():
    q = random.choices(quotes)
    print(q)
    return q