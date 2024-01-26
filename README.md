
## AIBlogger

It's a simple Python application based on django framework and OLLAMA API to post AI blogging content online.


### Usage

* **Running django application:**
  When running only the django site it will act as a blogpost where users can create accounts and login.
  ```python
  python django_project/manage.py runserver
  ```
* **Running OLLAMA:**
  To run OLLAMA we need to follow the official installation script.
  ```shell
  curl https://ollama.ai/install.sh | sh
  ```
* **Running LLM with OLLAMA:**
  Run below commands to download a specific LLM model, these are the models which are supported by OLLAMA https://ollama.ai/library.
  ```shell
  ollama serve
  ollama run mistral
  ```


This will start the OLLAMA server to fetch the AI generated content.

### Notes

* Mistral is used in the project currently, which can be changed into `llm_prompter.py`.
* "<django_url>/spawn" will generate a new blog and add it to the database.

### Requirements

* Python 3.x
