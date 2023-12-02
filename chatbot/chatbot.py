import logging

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               MessagesPlaceholder,
                               SystemMessagePromptTemplate)
from personas import is_persona_prompt

logging.basicConfig(level=logging.ERROR)
# LLM
llm = ChatOpenAI(max_tokens=200, temperature=0.9)

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


personas_memory = ConversationBufferMemory(memory_key="personas_chat_history", return_messages=True)
personas_system_message = f"""Your job is to determine if the user asks you to take a persona or role in your response. It might ask you that you are an animal, person or something else. If it indeed asks you for you to take a persona, return the role that its ask you to take only. Otherwise return "NONE". for example if the user says: pretend to be a pirate then you should return pirate"""
personas_prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(personas_system_message),
            MessagesPlaceholder(variable_name="personas_chat_history"),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )
llm = ChatOpenAI(max_tokens=200, temperature=0.9)
conversation_personas = LLMChain(llm=llm, prompt=personas_prompt, verbose=False, memory=personas_memory)
personas_list = []
def is_persona_prompt(user_prompt: str):
    """ Takes user's input and prints whether the input asks the model 
    to take on a specific persona (pirate, greek god)"""
    response = conversation_personas({"question": user_prompt})["text"]
    if response == 'NONE':
        return
    else:
        personas_list.append(response)
        
print(f"Welcome to the door-to-door {field_of_work} salesperson expert chatbot!")
print("Type 'history' to see the conversation history.")
print("Press ctrl-c or ctrl-d on the keyboard to exit.")
print("")

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input("> ")
        is_persona_prompt(user_input)
        if user_input == "history":
            for m in conversation.memory.chat_memory.messages:
                print(m.content)
            continue
        elif user_input == "personas":
            for p in personas_list:
                print(p)
            continue
        print("Processing...")

        bot_response = conversation({"question": user_input})
        print(bot_response["text"])

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
            break


