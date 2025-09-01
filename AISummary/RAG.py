from langchain_community.vectorstores import FAISS
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_ollama import OllamaEmbeddings
import json

class RAG:
    def __init__(self, model="llama3.2", vectorDb=FAISS, outputCount=1):
        self.model = model
        self.vectorDb = vectorDb
        self.outputCount = outputCount

    def readFile(self, filename):
        jsonFile = open(filename, 'r')
        content = json.load(jsonFile)
        jsonFile.close()
        return content

    def getRelatedContent(self, inputText, exampleFilename):
        exampleSelector = SemanticSimilarityExampleSelector.from_examples(
            self.readFile(exampleFilename),
            OllamaEmbeddings(model=self.model),
            self.vectorDb,
            k=self.outputCount,
            input_keys=["description"],
        )

        stringContent = exampleSelector.select_examples({"description": inputText})[::-1]

        return stringContent