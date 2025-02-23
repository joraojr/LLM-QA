from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain.agents import AgentExecutor, create_tool_calling_agent

from dotenv import load_dotenv

from .functions.check_loan import LoanCheckTool


class Chatbot:

    def __init__(self, max_tokens, temperature, agent, verbose):
        load_dotenv()
        self.is_agent = agent
        self.history = {
            "chat_history": [],
        }

        self.conversation_chat = self.load_assets(max_tokens, temperature, verbose)


    def query(self, question):
        answer = self.conversation_chat.invoke(
            {
                'input': question,
                'messages': self.history.get("chat_history")
            }
        )

        if self.is_agent:
            output = answer.get("output")
        else:
            output = answer.content

        self.history.get("chat_history").append(HumanMessage(content=question))
        self.history.get("chat_history").append(AIMessage(content=output))

        return output

    def load_assets(self, max_tokens, temperature, verbose):
        conversation_chat = self.get_conversation_chain(max_tokens, temperature, verbose)

        return conversation_chat

    def get_conversation_chain(self, max_tokens=None, temperature=0, agent=False, verbose=False):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    You are a financial advisor chatbot for Česká Spořitelna. Your task is to notify clients and help them with upcoming loan payments. 
                    
                    You check if there is any loan open to the client. You inform the due in X days ONLY IF it exists. If a client asks about a loan, use the function check_loan.
                                        
                    You communicate with the client via the official chat channel of Česká Spořitelna, e.g., WhatsApp, Telegram, or the Banking app. You ALWAYS keep the number of words in your text in mind.
                    
                    You are professional and maintain the client's privacy.
                    
                    Your tone is compassionate, supportive, and solution-oriented.
                    
                    You ALWAYS craft a dialogue where:
                        - You ALWAYS gently inform the client of the impending installment.
                        - You ALWAYS express empathy for their financial challenges.
                        - You provide clear, step-by-step instructions on how to proceed with the payment.
                        - You offer supportive advice on managing finances to avoid future issues.
                        - You encourage the client to reach out for further assistance if needed.
                                        
                    You NEVER answer questions not related to the Česká Spořitelna and refuse it politely.
                    
                    You ALWAYS forward the user to a human agent if you cannot help the user.
 
                    """
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            max_tokens=max_tokens,
            temperature=temperature,
        )

        if self.is_agent:
            tools = [LoanCheckTool()]
            agent = create_tool_calling_agent(llm, tools, prompt)
            agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=verbose)

        else:
            agent_executor = prompt | llm

        return agent_executor
