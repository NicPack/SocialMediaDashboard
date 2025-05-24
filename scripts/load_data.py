import pandas as pd
from datasets import load_dataset


def load_dataset_to_df():
    print("Loading dataset...")
    dataset = load_dataset("reddit", split="train[:10000]", trust_remote_code=True)

    print("Converting to pandas DataFrame...")
    df = pd.DataFrame(dataset)

    print("Preparing data...")

    columns = ["id", "author", "content", "subreddit", "subreddit_id"]
    data = df[columns].values.tolist()

    print("Data successfully loaded into DataFrame!")

    return data


if __name__ == "__main__":
    load_dataset_to_df()
