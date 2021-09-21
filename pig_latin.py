class PigLatin:
    def __init__(self, text):
        pig_latin_builder = ''
        vowel = 'aeiou'
        separated_text = text.split()
        for word in separated_text:
            word_body = word[1:]
            first_letter = word[:1]
            if first_letter.lower() in vowel:
                if first_letter.islower():
                    first_letter = 'w'
                else:
                    first_letter = 'W'
            pig_latin_builder += f"{word_body}-{first_letter}ay "
        self.pig_latin = pig_latin_builder[:-1]


def test_pig_latin():
    """
    Using pytest, this would run in a separate file and verify PigLatin 
    functionality
    """
    text_examples = [('pig', 'ig-pay'), 
                      ('pig latin', 'ig-pay atin-lay'),
                      ('Pig Latin', 'ig-Pay atin-Lay'), 
                      ('artichoke Adam', 'rtichoke-way dam-Way'), ('', '')]
    for example in text_examples:
        test_latin = PigLatin(example[0])
        assert test_latin.pig_latin == example[1]
        
        
if __name__ == '__main__':
    test_pig_latin()
    goodbye = PigLatin('Have a great day!')
    print(goodbye.pig_latin)
