import logging

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               MessagesPlaceholder,
                               SystemMessagePromptTemplate)

logging.basicConfig(level=logging.INFO)
# LLM
llm = ChatOpenAI(max_tokens=150, temperature=0.9)

# Prompt
field_of_work = input("Please enter your field of work: \n")
experience = input("Please enter your years of experience: \n")

system_message = f"You are a door-to-door salesperson expert in {field_of_work}. You are teaching someone with {experience} years of experience how to be an effective door-to-door salesperson."

prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(system_message),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)

# Notice that we `return_messages=True` to fit into the MessagesPlaceholder
# Notice that `"chat_history"` aligns with the MessagesPlaceholder name
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = LLMChain(llm=llm, prompt=prompt, verbose=False, memory=memory)

print(f"Welcome to the door-to-door {field_of_work} salesperson expert chatbot!")
print("Type 'history' to see the conversation history.")
print("Press ctrl-c or ctrl-d on the keyboard to exit.")
print("")

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input("> ")
        if user_input == "history":
            for m in conversation.memory.chat_memory.messages:
                print(m.content)
            continue

        print("Processing...")

        bot_response = conversation({"question": user_input})
        print(bot_response["text"])

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
            break


