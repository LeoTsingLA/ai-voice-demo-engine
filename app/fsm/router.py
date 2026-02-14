from dataclasses import dataclass

@dataclass
class RouteResult:
    intent: str
    next_state: str

def route_text(text: str, state: str = "start") -> RouteResult:
    """
    Minimal FSM-style router placeholder.
    Replace with real intent map + transitions later.
    """
    t = (text or "").lower().strip()
    if "impound" in t:
        return RouteResult(intent="IMPOUND_INQUIRY", next_state="impound")
    if "tow" in t:
        return RouteResult(intent="TOW_REQUEST", next_state="tow_request")
    return RouteResult(intent="GENERAL_INFO", next_state="general")
