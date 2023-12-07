import logging
from freedictionaryapi.clients.sync_client import DictionaryApiClient
from freedictionaryapi.errors import DictionaryApiNotFoundError
from random_word import RandomWords


def getRandomWord(min_nletters, max_nletters):
    r = RandomWords()
    word = r.get_random_word()
    logging.debug('getRandomWord Parameters: min_nletters = %s, max_nletters = %s.',
                  min_nletters, max_nletters)
    logging.info("getRandomWord returns %s", word)
    while len(word) <= min_nletters or len(word) >= max_nletters:
        word = r.get_random_word()
    return word


def getRandomWordAndDefinitions(min_nletters, max_nletters):
    word = None
    definitions = list()
    with DictionaryApiClient() as client:
        # Return a single random word with at least number of letters
        word = getRandomWord(min_nletters, max_nletters)
        # loop until the choosen word will be in the dict
        while True:
            try:
                parser = client.fetch_parser(word)
                # if we are here is because the word is in the dict
                break
            except DictionaryApiNotFoundError as e:
                logging.info("Word: %s not in dict. Trying again...", word)
                word = getRandomWord(min_nletters, max_nletters)
        # that word is in the dict
        word = parser.word
        for meaning in word.meanings:
            # print(meaning.part_of_speech)
            for definition in meaning.definitions:
                # print(definition.definition)
                definitions.append(definition.definition)
    return word.word, definitions
