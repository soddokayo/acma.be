from transformers import pipeline

classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

def classificate(req, cats):
    prediction = classifier(
        req, 
        cats
    )
    res = prediction['labels'][0]
    return res