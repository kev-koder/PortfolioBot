from transformers import pipeline

def get_llm():
    return pipeline(
        "text-generation",
        # model="mistralai/Mistral-7B-Instruct-v0.2",
        # max_new_tokens=200
        model="microsoft/phi-2",
        max_new_tokens=50
    )

