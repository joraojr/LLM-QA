import argparse

from qa.chatbot import Chatbot


def start_chat(max_tokens, temperature, agent, verbose):
    print("Starting the chatbot ...")
    chatbot = Chatbot(max_tokens, temperature, agent, verbose)
    print("Completed.\n")
    print("The chatbot is ready. How can I help you?")
    print("Type 'exit' to quit.")

    while True:
        question = input("Ask a question: ")
        if question.lower() == "exit":
            break
        answer = chatbot.query(question)
        print("Answer:", answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chatbot variables")

    parser.add_argument('--max_tokens', type=int, default=None, help='Change the number of output tokens (default: None)')
    parser.add_argument('--temperature', type=float, default=0, help='Change the temperature number (default: 0)')
    parser.add_argument('--agent', type=bool, default=False, help='Use the Agent version (default: False)', action=argparse.BooleanOptionalAction)
    parser.add_argument('--verbose', type=bool, default=False, help='Makes the Chatbot/Agent verbose (default: False)',
                        action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    start_chat(args.max_tokens, args.temperature, args.agent, args.verbose)
