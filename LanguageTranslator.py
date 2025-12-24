import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


os.environ["GOOGLE_API_KEY"] = "AIzaSyD46lLeuP-0V2QsBVpI25jAXfGeDpLAocA"

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.3
)
prompt = PromptTemplate(
    input_variables=["text", "language"],
    template="""
You are a professional multilingual translator.

Translate the following text into {language}.

STRICT RULES:
- Output ONLY the four lines below
- No explanations or extra text

Return the response in EXACTLY this format:
Language: {language}
English: {text}
Translation: <translated text in native script>
Transliteration: <translated text written using English letters>


"""
)


chain = prompt | llm

text = input("Enter text to translate: ")
language = input("Enter target language: ")

response = chain.invoke({
    "text": text,   
    "language": language
})

print("\nResult:")
print(response.content[0]["text"])
