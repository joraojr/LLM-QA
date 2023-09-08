import argparse

from qa.raipaychatbot import RaiPayChatbot


def start_chat(max_tokens, temperature, verbose):
    print("Loading the model...")
    chatbot = RaiPayChatbot(max_tokens, temperature, verbose)
    print("Completed.\n")
    print("RaiPay QA bot is ready. How can I help you?")
    print("Type 'exit' to quit.")

    while True:
        question = input("Ask a question: ")
        if question.lower() == "exit":
            break
        answer = chatbot.query(question)
        print("Answer:", answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Raiffeisen Chatbot variables")

    parser.add_argument('--max_tokens', type=int, default=None, help='Change the number of output tokens (default: None)')
    parser.add_argument('--temperature', type=float, default=0, help='Change the temperature number (default: 0)')
    parser.add_argument('--verbose', type=bool, default=False, help='Makes the Chatbot/Agent verbose (default: False)')

    args = parser.parse_args()

    start_chat(args.max_tokens, args.temperature, args.verbose)
