import pandas as pd
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sklearn.model_selection import train_test_split
from sentence_transformers import SentenceTransformer, util

data = pd.read_csv("train_data.csv")

def clean_text(text):
    import re
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
data['Question'] = data['Question'].apply(clean_text)
data['Answer'] = data['Answer'].apply(clean_text)



train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)



embeddings = SentenceTransformerEmbeddings()

train_question_embeddings = embeddings.embed_documents(train_data['Question'])
train_answer_embeddings = embeddings.embed_documents(train_data['Answer'])


text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)

def analyze_answer(user_answer, reference_answer, comments):
    user_chunks = text_splitter.split_text(user_answer)
    reference_chunks = text_splitter.split_text(reference_answer)
    user_embeddings = embeddings.embed_documents(user_chunks)
    reference_embeddings = embeddings.embed_documents(reference_chunks)
    similar_chunks = []
    for ref_chunk, ref_embedding in zip(reference_chunks, reference_embeddings):
            for user_chunk, user_embedding in zip(user_chunks, user_embeddings):
                similarity = util.cos_sim(user_embedding, ref_embedding)[0][0]
                if similarity > 0.6:
                    similar_chunks.append(user_chunk)
                    break
    covered_information = " ".join(similar_chunks)
    if len(similar_chunks) > 0.8 * len(reference_chunks):
        feedback = "Верно!"
    else:
        feedback = "Не совсем точно."
        return feedback


for i, row in test_data.iterrows():
    question = row['Question']
    reference_answer = row['Answer']
    comments = row['Comment']
    user_answer = input(f"Вопрос: {question}\nВаш ответ: ")
    feedback = analyze_answer(user_answer, reference_answer, comments)
    print(feedback)
    if feedback == "Не совсем точно":
        print(comments)