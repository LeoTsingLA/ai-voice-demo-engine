from dataclasses import dataclass

@dataclass
class RagResult:
    answer: str
    sources: list[str]

def retrieve_answer(question: str) -> RagResult:
    """
    Minimal RAG placeholder.
    Later: vector search -> top-k -> grounded response.
    """
    return RagResult(
        answer=f"(stub) grounded answer for: {question}",
        sources=["kb:demo_card_001"]
    )
