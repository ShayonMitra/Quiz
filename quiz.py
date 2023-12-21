from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import streamlit as st
import os
os.environ["OPENAI_API_KEY"] = "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"
def create_the_prompt_template():
	template="""
	You are an expert quiz maker for technical topics.
	Create a quiz with {number}{type} of questions about the following:{topic}
	"""
	prompt = PromptTemplate.from_template(template)
	return prompt 

def create_quiz_chain(prompt_template,llm):
	return LLMChain(llm=llm, prompt=prompt_template)

def main():
	st.title("Quiz Generator")
	st.write("Write something about a topic and this generates a quiz")
	prompt_template = create_the_prompt_template()
	llm = ChatOpenAI()
	chain = create_quiz_chain(prompt_template,llm)
	topic = st.text_area("Enter something about the topic")
	num_questions = st.number_input("Enter the number of questions",min_value=1, max_value=10)
	quiz_type = st.selectbox("Select the type of questions",["multiple-choice","subjective","programming"])
	if st.button("Generate"):
		quiz = chain.run(number=num_questions,type=quiz_type,topic=topic)
		st.write(quiz)


if __name__=="__main__":
	main()