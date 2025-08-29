import PyPDF2
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def resume_historial(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    texto = "".join([page.extract_text() for page in reader.pages])
    
    prompt = ChatPromptTemplate.from_template(
        "Resume este historial médico en 3 puntos clave:\n\n{texto}"
    )
    chain = prompt | llm
    return chain.invoke({"texto": texto}).content
