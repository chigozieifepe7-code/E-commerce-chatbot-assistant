import pandas as pd
from pathlib import Path
import chromadb


chroma_client = chromadb.Client()
collection_name_faq = "faqs"
faqs_path = Path(__file__).parent / "resources/faq_data.csv"


def ingest_faq_data(path):
    df = pd.read_csv(path)


if __name__ == "__main__":
    ingest_faq_data(faqs_path)
