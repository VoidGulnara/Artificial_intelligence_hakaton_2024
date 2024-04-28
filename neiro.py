import pandas as pd
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



train_data = data[data['Correctness'] == 1]  
test_data = train_test_split(train_data, test_size=0.2, random_state=42)[1]



model_name = 'all-MiniLM-L6-v2' 
embedder = SentenceTransformer(model_name)



def split_text(text, chunk_size=200, chunk_overlap=50):
    chunks = []
    for i in range(0, len(text), chunk_size - chunk_overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks



def analyze_answer(user_answer, reference_answer, comments):
    user_chunks = split_text(user_answer)
    reference_chunks = split_text(reference_answer)

    user_embeddings = embedder.encode(user_chunks)
    reference_embeddings = embedder.encode(reference_chunks)

    similar_chunks = []
    for ref_chunk, ref_embedding in zip(reference_chunks, reference_embeddings):
        for user_chunk, user_embedding in zip(user_chunks, user_embeddings):
            similarity = util.cos_sim(user_embedding, ref_embedding)[0][0]

            # Check if the reference chunk belongs to a correct answer
            corresponding_row = train_data[(train_data['Question'] == question) & (train_data['Answer'] == ref_chunk)]
            is_correct_reference = not corresponding_row.empty and corresponding_row['Correctness'].values[0] == 1

            if similarity > 0.67 and is_correct_reference:
                similar_chunks.append(user_chunk)
                break

    covered_information = " ".join(similar_chunks)
    if len(similar_chunks) > 0.8 * len(reference_chunks):
        feedback = "Верно!"
    else:

        incorrect_matches = train_data[(train_data['Correctness'] == 0) & (train_data['Question'] == question)]
        for incorrect_answer in incorrect_matches['Answer']:
            incorrect_chunks = split_text(incorrect_answer)
            incorrect_embeddings = embedder.encode(incorrect_chunks)
            for user_chunk, user_embedding in zip(user_chunks, user_embeddings):
                for inc_chunk, inc_embedding in zip(incorrect_chunks, incorrect_embeddings):
                    similarity = util.cos_sim(user_embedding, inc_embedding)[0][0]
                    if similarity > 0.67:
                        feedback = "Неверно, ответ похож на ранее помеченный как некорректный."
                        return feedback  

        feedback = "Не совсем точно"  
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
