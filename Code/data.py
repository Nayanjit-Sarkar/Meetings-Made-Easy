from datasets import load_dataset
import pandas as pd


def rem_col(col):
    ds = load_dataset("edinburghcstr/ami", "ihm")
    ds = ds.remove_columns(col)
    return ds


def build_dataset(df, data, name, row):
    for idx in range(0, row):
        print(idx)
        dict1 = data[name][idx]
        print(dict1)
        # df["meeting_id"].append(dict1["meeting_id"])
        # df["text"].append(dict1["text"])
        # df["begin_time"].append(dict1["begin_time"])
        # df["end_time"].append(dict1["end_time"])
        # df["speaker_id"].append(dict1["speaker_id"])
        df = df.append(data, ignore_index = True)
        if idx == 5:
            print(df)
            break
    # new_column_names = {"begin_time": "start_time"}
    # df = df.rename(columns=new_column_names)
    # new_column_order = [
    #     "meeting_id",
    #     "start_time",
    #     "end_time",
    #     "speaker_id",
    #     "text",
    # ]

    # df = df.reindex_axis(new_column_order, axis=1)
    # df.to_CSV(
    #     f"{name}.csv",
    #     index=False,
    # )


if __name__ == "__main__":
    data = rem_col(["audio_id", "audio", "microphone_id"])
    col = {
        "meeting_id": [],
        "text": [],
        "begin_time": [],
        "end_time": [],
        "speaker_id": [],
    }
    df = pd.DataFrame(columns=['meeting_id', 'text', 'begin_time', 'end_time', 'speaker_id'])
    print("Collecting Training Data")
    build_dataset(df, data, "train", 108502)
    # print("Collecting Validating Data")
    # build_dataset(df, data, "validation", 13098)
    # print("Collecting Testing Data")
    # build_dataset(df, data, "test", 12643)
