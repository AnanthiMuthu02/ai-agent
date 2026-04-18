import anthropic
import os
import requests
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Now I am defining the tools thatclaude can use

tools = [
    {
        "name": "search_web",
        "description": "Search  the internet for current information on this topic",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "the search query"
                }
            },
      
            "required": ["query"]
          }
    },
    {
        "name": "calculator",
        "description": "Perform mathematical calculations",
        "input_schema": {

            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate e.g. (50000+70000)/2"
                }
            },
            "required": ["expression"]
        }
    } 
    
    ]



###  functions defining what these tools can do


def search_web(query):
    """search the web using DuckDuckGo"""
    url= "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json", "no_html":1 }
    response = requests.get(url, params=params)
    data = response.json()

    results = [] 
    if data.get("AbstractText"):
        results.append(data["AbstractText"])
    for topic in data.get("RelatedTopiocs", [])[:3]:
        if "Text" in topic:
            results.append(topic["Text"])
    
    return "\n".join(results) if results else "No results found. Try different search."

def calculate(expression):
    """Safely evaluate a mathematical expression"""

    try:

        result = eval(expression, {"__builtins__":{}})
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
    
#__Process tool calls from claude

def process_tool_call(tool_name, tool_input):
    """Run the tool claude choose and run the result"""
    print(f"\n Agent using tool: {tool_name}")
    print(f" input: {tool_input}")


    if tool_name == "search_web":
        result = search_web(tool_input["query"])
    elif tool_name=="calculator":
        result = calculate(tool_input["expression"])
    else:
        result = "Tool not found"

    print(f" Result: {result[:100]}...")
    return result   



def run_agent(goal):
    """the main agent loop - thinks,acts, observes, repeat."""
    print(f"\n Goal: {goal}")
    print("=" * 40)


    messages = [{"role": "user", "content": goal}]


    while True:
        #claude thinks and decides what to do

         response = client.messages.create(
             model = "claude-sonnet-4-6",
             max_tokens=1024,
             tools=tools,
             messages=messages
         )

         # did claude finish? 

         if response.stop_reason == "end_turn":
             for block in response.content:
                 if hasattr(block, "text"):
                     
             #final_answer = response.content[0].text
                    print(f"\n Final Answer: \n {block.text}")
             break
         # claude wants to use a tool

         if response.stop_reason == "tool_use":
            
            messages.append({
                "role" : "assistant",
                "content" : response.content
            })

            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    result = process_tool_call(block.name, block.input)
                    tool_results.append(
                        {
                            "type" : "tool_result",
                            "tool_use_id" : block.id,
                            "content": result
                        }
                    )
            

            messages.append({

                "role":"user",
                "content": tool_results
            })

print("AI agent")
print("-"* 40 )
goal = input("Give me goal to work on: ")
run_agent(goal)