from typing import Annotated
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


llm = init_chat_model("openai:gpt-4.1")


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile()


def stream_graph_updates(user_input: str):
    responses = []
    for event in graph.stream({"messages": [{"role": "system", "content":
                                             "You're a helpfull assistant that will explain a latex equation that the user give at the best of yout capabilities. Don't do follow up questions"},
                                            {"role": "user", "content":
                                             user_input}]}):
        for value in event.values():
            responses.append(value["messages"][-1].content)
    return responses
