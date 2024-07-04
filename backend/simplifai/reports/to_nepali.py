from transformers import pipeline

path_docker = '/usr/src/app/backend/my_awesome_english_to_nepali_tst'
path ='/home/an00b/Anup2024/Vivkea/Quine_SimplifAI/backend/my_awesome_english_to_nepali_tst'
pipe = pipeline("text2text-generation", model=path_docker   )

def nepali_translator(text):
    return pipe(text)[0]['generated_text']


# sample_text = "Are you gay?"


# translated_text = translate_text(sample_text)