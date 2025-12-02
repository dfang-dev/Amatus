# imports ChatOllama class
from langchain_ollama import ChatOllama

# creates the model using locally installed model type
llm = ChatOllama(model="phi4-mini")

# sends "hello" to the model for a response, stores then prints
result = llm.invoke(input="hello")
print(result)