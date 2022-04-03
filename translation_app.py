import streamlit as st


from deep_translator import GoogleTranslator
st.header('Text 2 Translate')

st.sidebar.header('Text 2 Translate')



def getList(dict):
    return dict.keys()


input_text = st.text_input("",value="Type your text in here")

land_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am',
'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 
'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 
'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 
'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 
'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 
'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 
'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 
'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 
'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'korean': 'ko', 
'kurdish': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 
'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 
'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 
'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 
'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 
'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 
'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 
'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'turkmen': 'tk', 
'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 
'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}




langs = getList(land_dict)

output_langs = st.sidebar.selectbox("Choose your output lang",langs,index=26)

#adding option download the text



if len(input_text) == 0:
    input_text = "Hey how are you doing? why don't you type something and have fun"


if len(input_text) > 5000:

    input_text1 = input_text[:4999]
    st.warning("You are going over 5000 words my friend! (Suggest me ways to process it :)")
    input_text = input_text1

trns = translated = GoogleTranslator(source='auto', target=output_langs).translate(input_text)


#write_in_new = st.checkbox('Save as  text file')



text_contents = trns
st.download_button('Download the Text',data =  text_contents,file_name = 'translated.txt')


st.subheader(trns)