import docx2txt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import everygrams
import re

nltk.download('stopwords')
nltk.download('punkt')

# you may read the database from a csv file or some other database
SKILLS_DB = [
    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'english',
]

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None

def extract_skills(input_text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_text.lower())

    # remove the stop words and punctuations
    filtered_tokens = [w for w in word_tokens if w.isalpha() and w not in stop_words]

    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, everygrams(filtered_tokens, 2, 3)))

    # we create a set to keep the results in.
    found_skills = set()

    # we search for each token in our skills database
    for token in filtered_tokens:
        for skill in SKILLS_DB:
            if re.search(r'\b{}\b'.format(re.escape(token)), skill):
                found_skills.add(skill)

    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        for skill in SKILLS_DB:
            if re.search(r'\b{}\b'.format(re.escape(ngram)), skill):
                found_skills.add(skill)

    return found_skills

if __name__ == '__main__':
    text = extract_text_from_docx('./ResumeData.docx')
    skills = extract_skills(text)

    print(skills)
