# Architecture

This repository demonstrates a production-oriented, real-time AI voice agent architecture focused on:
- Low-latency streaming (Twilio Media Streams)
- Deterministic control where required (FSM guardrails)
- Knowledge-grounded responses (RAG routing)
- Clear separation of concerns for maintainability and scaling

---

## High-level System Diagram

```mermaid
flowchart LR
  Caller((Caller))
  Twilio[Twilio Voice\nMedia Streams]
  API[FastAPI Backend\n(Webhook + WS)]
  VAD[Voice Activity Detection\n(VAD / turn detection)]
  FSM[FSM Guardrails\n(Intent routing + state transitions)]
  RAG[RAG Router\n(Knowledge retrieval)]
  LLM[LLM / Realtime Model\n(Response generation)]
  TTS[TTS / Audio Out\n(streaming)]
  Ops[Observability\n(Logs/Metrics/Traces)]
  Store[(Storage\n(Call logs / artifacts))]
  KB[(Knowledge Base\n(Cards / Docs / Vectors))]

  Caller -->|Phone Call| Twilio
  Twilio -->|audio stream (WS)| API
  API --> VAD
  VAD --> FSM
  FSM -->|safe path| RAG
  RAG -->|retrieval| KB
  RAG --> LLM
  FSM -->|guardrails\n(when no RAG needed)| LLM
  LLM --> TTS
  TTS --> API
  API -->|audio stream| Twilio
  Twilio -->|Voice| Caller

  API --> Ops
  API --> Store
  RAG --> Ops
  FSM --> Ops
  LLM --> Ops

Call Lifecycle (Step-by-step)

Call connect

Caller dials a Twilio number.

Twilio connects and starts streaming audio via Media Streams.

Streaming ingress

Backend receives audio frames over WebSocket.

Frames are buffered and timestamped for reliable turn processing.

Turn detection

VAD / turn detection identifies when the user is speaking vs. silence.

This stabilizes “when to think / when to speak” in real-time.

Intent routing + FSM guardrails

The FSM determines the current state and allowed transitions.

Certain intents require deterministic collection/confirmation (e.g. IDs, names, plates, VIN-last-6).

RAG knowledge routing (optional)

For knowledge queries, the router fetches relevant knowledge cards/doc snippets.

Retrieved context is passed into the LLM to reduce hallucination.

Response generation

LLM generates a response under the constraints of the current FSM state.

Responses may be segmented for streaming output.

Streaming egress

TTS produces audio output (or realtime voice model streams audio directly).

Audio is streamed back to Twilio and played to the caller.

Observability + artifacts

Logs, call artifacts, and key events (state transitions, retrieval hits, latency) are recorded.

Key Design Principles
1) Guardrails first

Use the LLM where it adds value, but rely on deterministic rules/flows where correctness is required.

2) Separation of concerns

Streaming / transport (Twilio + WS)

Turn detection (VAD)

Control plane (FSM)

Knowledge plane (RAG)

Generation plane (LLM / Realtime voice)

Operations (logging/metrics/artifacts)

3) Extensible for multi-tenant

Tenant-specific scripts, prompts, and knowledge can be added without rewriting core engine logic.

Latency Notes (What matters)

Avoid blocking operations in the streaming path

Keep the turn detector and router lightweight

Record timestamps at each stage:

stream in → VAD decision → FSM route → RAG retrieve → LLM start → first audio out

Future Extensions (Optional)

Multi-tenant config loader (tenant.yaml)

More robust eval harness (replay calls + compare outputs)

Tracing integration (OpenTelemetry)

Safety filters per intent (PII / policy compliance)

