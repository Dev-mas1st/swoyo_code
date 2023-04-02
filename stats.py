from string import ascii_letters

def text_stat(filename):
    try:
        cyrillics = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
        latin_cyrillic = ascii_letters +  cyrillics
        bi_letters = "АаЕеКкМмОоТтВвНнРрСсУуХх" + "AaEeKkMOoTBHPpCcyXx"
        
        results = {}
        bi_words = set()

        #opening the txt file
        with open(filename,encoding="utf-8") as file:
            text = file.read()
            words = [i for i in text.split()]
            
        #The number of occurences of each letter
        occurs = {i: text.count(i) for i in latin_cyrillic if text.count(i) > 0}
        for k, v in occurs.items():
            let_stat = [index for index, elem in enumerate(words) if k in elem]
            
            results[k] = (v, len(let_stat))

        #The number of words
        results["word_amount"] = len(words)


        #The number of paragraphs
        results["paragraph_amount"] = len([i for i in text.split("\n") if i != ""])

        #The number of bi words 
        for letter in bi_letters:
            for word in words:
                if letter in word: bi_words.add(word)

        results["bilingual_word_amount"] = len(bi_words)
        
        return results
    except Exception as e:
        return {"error": str(e)}