
import gradio as gr
from operator import itemgetter
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough


# langchain imports
from langchain.llms import HuggingFaceTextGenInference

def call_llm():

    llm = HuggingFaceTextGenInference(
        inference_server_url="http://tgi",
        max_new_tokens=1800,
        top_k=15,
        top_p=0.95,
        typical_p=0.95,
        temperature=.7,
        repetition_penalty=1.03,
        streaming=True
    )
    return llm   

# Initialize chat model
llm = call_llm()

# Define a prompt template
template = """[INST] You are a helpful AI assistant. You will answer user requests to the best of your abilities. Only answer the specific request and stop generating.[/INST]
"""

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

# Create conversation history store
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

chain = (
    RunnablePassthrough.assign(
        history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
    )
    | chat_prompt
    | llm
)

# chain = LLMChain(llm=llm, memory=memory, verbose=True, prompt=chat_prompt)


def stream_response(input, history):
    if input is not None:
        partial_message = ""
        # ChatInterface struggles with rendering stream
        # make the call to the bot
        for response in chain.stream({"input": input}):
            partial_message += response
            yield partial_message 

gr.ChatInterface(stream_response, analytics_enabled=False).queue(default_concurrency_limit=None).launch(debug=True, server_name='0.0.0.0', server_port=7000, share=False)