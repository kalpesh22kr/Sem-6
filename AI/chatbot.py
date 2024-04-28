from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.) investments|invest (.)",
        ["Sure, what type of investment are you interested in? (e.g., stocks, bonds, real estate)"]
    ],
    [
        r"(.*) stocks?",
        ["Stocks can be a good investment option for long-term growth. Some popular stocks include Apple, Amazon, and Google."]
    ],
    [
        r"(.*) bonds?",
        ["Bonds are considered safer investments than stocks. You can consider government bonds or corporate bonds for fixed income."]
    ],
    [
        r"(.*) real estate?",
        ["Real estate can be a lucrative investment option for building wealth over time. You can explore residential or commercial properties."]
    ],
    [
        r"(.*) mutual funds?",
        ["Mutual funds offer diversification and are managed by professionals. You can choose from equity funds, debt funds, or balanced funds."]
    ],
    [
        r"(.*) ETFs?",
        ["ETFs (Exchange-Traded Funds) are similar to mutual funds but trade like stocks. You can consider ETFs for diversification and low fees."]
    ],
    [
        r"(.*) commodities?",
        ["Commodities like gold, silver, and oil can be considered as alternative investments for portfolio diversification."]
    ],
    [
        r"(.*) cryptocurrencies?",
        ["Cryptocurrencies like Bitcoin and Ethereum have gained popularity but are highly volatile. Only invest what you can afford to lose."]
    ],
    [
        r"(.*) created?",
        ["I was made by a computer programmer."]
    ],
    [
        r"Hi|Hello|Hey|hi|hello",
        ["Hey there!", "Hello! How can I assist you today?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day."]
    ]
]

def chat():
    print("Hello! I'm here to assist you with investment suggestions. Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if _name_ == "_main_":
    chat()
