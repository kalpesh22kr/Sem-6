pairs = [
    ["what is your name?", "My name is Simp_Chatbot."],
    ["hi","Hello!"],
    ["hello","Hello!"],
    ["how are you?", "I'm doing well, thank you!"],
    ["what is the weather today?", "You can check the weather forecast online."],
    ["bye", "Goodbye!"],
    ["what is the capital of India?", "The capital of India is New Delhi."],
    ["how many states are there in India?", "India consists of 28 states and 8 Union territories."],
    ["what is the currency of India?", "The currency of India is the Indian Rupee (INR)."],
    ["when is Independence Day celebrated in India?", "Independence Day is celebrated on August 15th."],
    ["what is the national animal of India?", "The national animal of India is the Bengal Tiger."],
    ["what is the national flower of India?", "The national flower of India is the Lotus."],
    ["what is the national language of India?", "India doesn't have a national language, but Hindi is the official language."],
    ["can you tell me about the major festivals celebrated in India?", "Sure, some major festivals in India include Diwali, Holi, Eid, and Christmas."],
    ["how is Diwali celebrated in India?", "Diwali, the festival of lights, is celebrated by lighting oil lamps, decorating homes, and exchanging sweets."],
    ["what are some famous tourist attractions in India?", "Some famous tourist attractions in India are the Taj Mahal, Jaipur, Goa beaches, and Kerala backwaters."],
    ["what is the literacy rate in India?", "The literacy rate in India is approximately 74%. (As per recent statistics)"],
    ["how is the education system structured in India?", "The education system in India consists of primary, secondary, and higher education levels, with various boards and universities."],
    ["what are some traditional Indian cuisines?", "Some traditional Indian cuisines include biryani, dosa, butter chicken, and paneer tikka."]
]

def simple_chatbot():
    print("Hi, I'm a simple chatbot. Ask me anything!!")
    while True:
        user_input = input("You: ").lower()  
        found = False
        for question, answer in pairs:
            if user_input == question.lower():  
                print("Bot:", answer)
                found = True
                break
        if user_input == "bye":
            break
        elif not found:
            print("Bot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    simple_chatbot()

'''
Output:
PS D:\Ayush\College\Sem VI\Lab\AI\Codes> python -u "d:\Ayush\College\Sem VI\Lab\AI\Codes\Assignment_5\chatbot.py"
Hi, I'm a simple chatbot. Ask me anything!!
You: Hi                 
Bot: Hello!
You: What is your name?
Bot: My name is Simp_Chatbot.
You: What is the Capital of India?
Bot: The capital of India is New Delhi.
You: How many States In India?
Bot: I'm sorry, I didn't understand that.
You: How many States are there in India?
Bot: India consists of 28 states and 8 Union territories.
You: when is Independence Day celebrated in India?
Bot: Independence Day is celebrated on August 15th.
You: what is the national language of India?
Bot: India doesn't have a national language, but Hindi is the official language.
You: Bye
Bot: Goodbye!
'''