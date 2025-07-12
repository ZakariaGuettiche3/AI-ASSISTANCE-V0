from langchain_core.messages import HumanMessage
from langchain_fireworks import ChatFireworks
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()



@tool
def calc(a: float , b: float) -> str:
    """Useful for calculation"""
    return f"the sum of {a}+{b} is {a+b}"

def start():
    model = ChatFireworks(model="accounts/fireworks/models/llama4-maverick-instruct-basic")

    tools = [calc]

    agent = create_react_agent(model,tools)
    
    print('How can i help you today!!!')

    while True:
        inp = input("\n me: ").strip()
        print("\n Agent: ", end="")
        
        for chunck in agent.stream(
            {"messages": [HumanMessage(content=inp)]}
        ):
            if "agent" in chunck and "messages" in chunck["agent"]:
               for message in chunck["agent"]["messages"]:
                
                   print(message.content, end='')
                   

        print()

if __name__ == "__main__":
    start()

