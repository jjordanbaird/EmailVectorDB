# Email Parser and Vector Database Loader
This Python application demonstrates how to parse emails from a specified Gmail account, specifically emails from the TLDR newsletter, and load them into a vector database (Weaviate) for improved search capabilities. 

It uses OpenAI GPT-3.5 to help parse ambiguous parts of the email and provides parallelism for better performance. The application utilizes Docker for easy deployment.

## Requirements
- Python 3.9+
- Docker
- Docker Compose
- OpenAI API key
- Gmail account

## Installation

Required Packages:
```
pip install -r requirements.txt
docker-compose build
docker-compose up -d
```
## Configuration
1. Create a .env file in the project root directory with the following contents:
```
OPENAI_API_KEY=your_openai_api_key
EMAIL_ADDRESS=your_email_address
EMAIL_PASSWORD=your_email_password
```
Replace your_openai_api_key, your_email_address, and your_email_password with your OpenAI API key, Gmail address, and Gmail password, respectively.
2. Configure the docker-compose.yaml file as needed, including setting the desired ports and volume mappings.

## Usage
```
./load_data.sh
```
This script will:
- Fetch new emails from the specified Gmail account
- Use OpenAI GPT-3.5 to parse ambiguous parts of the email, with parallelism for better performance
- Create a Weaviate newsletter schema
- Load the parsed data into Weaviate

The parsed emails will be loaded into the Weaviate vector database, enabling improved search capabilities.


## Example Searches
I have included an example Jupyter Notebook, example_searches.ipynb, which demonstrates various search queries and their results when run against the Weaviate database. The notebook contains real-world examples that showcase the power of the vector search enabled by loading parsed email data into Weaviate.

Here is a sample query and its results from the notebook:

Query:
```
run_query("framework for dealing with llm prompts")
```

Results:
```
[
 {
  "header": "MODEL-TUNING VIA PROMPTS: IMPROVING ADVERSARIAL ROBUSTNESS IN NLP (15 MINUTE READ)",
  "links": ["https://arxiv.org/abs/2303.07320?utm_source=tldrai"],
  "received_date": "2023-03-15T13:13:19Z",
  "text_content": "The MVP method demonstrates surprising gains in adversarial robustness, improving performance against adversarial word-level synonym substitutions by an average of 8% over standard methods, and even outperforming state-of-art defenses by 3.5%. By modifying the input with a prompt template instead of modifying the model by appending an MLP head, MVP achieves better results in downstream tasks while maintaining clean accuracy."
 },
 {
  "header": "AN EXAMPLE OF LLM PROMPTING FOR PROGRAMMING (12 MINUTE READ)",
  "links": ["https://martinfowler.com/articles/2023-chatgpt-xu-hao.html?utm_source=tldrnewsletter"],
  "received_date": "2023-04-19T10:59:59Z",
  "text_content": "This article gives examples of how to use ChatGPT to produce useful self-tested code. The prompt starts by setting the context for the application and how the code should be structured. Most of the prompt is setting out the design guidelines the code should follow. The prompt ensures that ChatGPT generates useful information about the problem first before it generates any code. Using this structure, ChatGPT can be more informed of its task and generate better responses."
 },
 {
  "header": "MLC LLM (GITHUB REPO)",
  "links": ["https://github.com/mlc-ai/mlc-llm?utm_source=tldrnewsletter"],
  "received_date": "2023-05-01T11:01:29Z",
  "text_content": "MLC LLM can run any language model natively on a diverse set of hardware backends, enabling anyone to develop, optimize, and deploy AI models natively on many devices."
 }
 ...
]
```






