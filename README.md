# RaiPay Chatbot README

This README provides instructions on how to use the RaiPay Chatbot. The RaiPay Chatbot is a Python CLI that allows you to interact
with a chatbot designed to answer questions related to the RaiPay APP.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Examples](#examples)


---

## 1. Prerequisites <a name="prerequisites"></a>

Before using the RaiPay Chatbot, make sure you have the following prerequisites installed on your system:

- Python 3.10: The code is written in Python 3, so you need Python installed on your machine. You can download Python
  from [python.org](https://www.python.org/downloads/).

---

## 2. Installation <a name="installation"></a>

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you have downloaded or cloned the code.

3. Create a virtual environment (recommended):

 ```bash
   python -m venv venv
  ```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

5. Install the required Python packages:

```bash
pip install -r requirements.txt
```

6. Configurate the env file

    - Rename `.env.ex` to `.env` and add the env variables (e.g. **OPENAI_API_KEY**)

## 3. Usage <a name="usage"></a>

To use the RaiPay Chatbot, follow these steps:

1. Open a terminal or command prompt

2. Ensure you are in the project directory with the virtual environment activated.

3. Run the chatbot script with optional arguments:

```bash
python main.py 
```

- or run the chatbot script with optional arguments:

```bash
python main.py --max_tokens <max_tokens> --temperature <temperature> --verbose <verbose>
```
- --max_tokens: (Optional) Change the number of output tokens. If not specified, it defaults to **None**.

- --temperature: (Optional) Change the temperature number. If not specified, it defaults to **0**.

- --verbose: (Optional) Makes the Chatbot/Agent verbose. If not specified, it defaults to **False**.

4. Once the Chatbot is running, you can interact with it by typing questions. To exit the chat, simply type "exit.":

```text
     RaiPay chatbot is ready. How can I help you?
     Type 'exit' to quit.
     Ask a question:
```

## 4. Examples <a name="examples"></a>

 - Examples of success and failure tries are present in [Sucess and Failure examples](Sucess-Failure-Examples.md)

---
