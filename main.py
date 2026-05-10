from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
from langchain.chat_models import init_chat_model
os.environ["GOOGLE_API_KEY"] = "AIzaSyDz-4UewjmIYueGG__jor16coRL62Y1Gpg"
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    print(f"Tool called: {city}")
    return f"It's always sunny in {city}!"
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

agent = create_deep_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant. Always use tools.", 
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "what is the weather in sf"
            }
        ]
    }
)

print(response["messages"][-1].content)
print(response)