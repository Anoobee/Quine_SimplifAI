from transformers import pipeline

path = '/usr/src/app/backend/my_awesome_english_to_nepali_tst'
pipe = pipeline("text2text-generation", model=path)

def nepali_translator(text):
    return pipe(text)[0]['generated_text']


# sample_text = "Are you gay?"


# translated_text = translate_text(sample_text)