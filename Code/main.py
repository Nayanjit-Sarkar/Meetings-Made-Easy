import spacy
import csv


def clean_text(input_string):
    reader = csv.reader([input_string])
    fields = next(reader)
    # print(fields)
    return fields


def analyse_text(text):
    entity = {"ASSIGNEE": "UNKNOWN", "TEXT": ""}
    nlp = spacy.load(
        r"D:\MACHINE LEARNING\Meeting Analysis\model\output\model-best"
    )
    doc = nlp(text)
    for ent in doc.ents:
        entity[ent.label_] = ent.text
    # print(entity)
    return entity


def meeting_analyse(file):
    with open(file, "r") as f:
        for line in f:
            if line:
                data = clean_text(line)
                ts = data[0]
                sent = data[-1]
                entity = analyse_text(sent)
                text, assignee = entity["TEXT"], entity["ASSIGNEE"]
                print(f'"text": {text}, "assignee": {assignee}, "ts": {ts}')


if __name__ == "__main__":
    meeting_analyse(r"D:\MACHINE LEARNING\Meeting Analysis\Data\demo.txt")
