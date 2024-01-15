import sys
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Ollama




def create_blog_post (AI_character, hobbies):
    llm = Ollama(base_url='http://localhost:11434',
        model="mistral")
    
    prompt = PromptTemplate(
        input_variables = ["AI_blogger", "likes"],
        template="""
        You are a professional blogger on the internet that is always providing useful information to the public from their past experiences.

        Your name is : {AI_blogger}
        Post a random blog regarding the topics and dont put these topics directly in the post title - topic : {likes}

        The blog should be well structured and must be complete.
        Strictly give output as
        title: put the blog title here
        context: put blog context here
        """,
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(AI_blogger=AI_character, likes=hobbies)
    return response



#AI_character = "Michael"
#hobbies = ["video games", "live steams", "anime"]
#hobbies = "video games"
#response = create_blog_post(AI_character, hobbies)

#pattern_title = re.compile(r'[tT]itle\s?:\s?.*')
#pattern_context = re.compile(r'[cC]ontext\s?:\s?.*', re.DOTALL)

#title = pattern_title.search(response)

#context = pattern_context.search(response)

#print(title[0])
#print("################")
#print(context[0])

print("###OLLAMA is running and loaded successfully to django application!###")
