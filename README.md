# AI Voice Demo Engine

Production-ready real-time AI voice agent system built with:

- Twilio Media Streams (low-latency streaming)
- OpenAI Realtime / LLM integration
- Structured Intent Control (Finite State Machine guardrails)
- Retrieval-Augmented Generation (RAG) knowledge routing
- Async FastAPI backend architecture

---

## 🎯 Overview

This project demonstrates a scalable AI voice agent architecture designed for:

- Inbound call automation
- Industry-specific call routing
- Guardrailed conversation control
- Knowledge-grounded responses
- Low-latency speech streaming

The system focuses on production reliability rather than chatbot-style experimentation.

---

## 🏗 Architecture

Call Flow:

1. Caller connects via Twilio
2. Audio streamed through Media Streams
3. Voice Activity Detection (VAD)
4. Intent detection + FSM routing
5. RAG-based knowledge retrieval (if needed)
6. Structured response generation
7. Low-latency TTS response

Key Principles:

- Deterministic control where required
- LLM used only where appropriate
- Clear separation between intent logic and generation
- Production-grade async backend design

---

## 🧠 Core Capabilities

- Multi-intent routing
- Structured state transitions
- Guardrail enforcement
- Knowledge card retrieval
- Turn-based audio streaming
- Response isolation control
- Extensible tenant architecture

---

## 🛠 Tech Stack

- Python
- FastAPI
- Twilio Media Streams
- OpenAI Realtime API
- AsyncIO
- Structured FSM Controller
- Vector-based retrieval layer

---

## 🚀 Intended Use Cases

- AI Voice Receptionists
- Service industry call automation
- Lead qualification flows
- Workflow-triggered call systems
- Escalation-ready voice agents

---

## 📌 Note

This repository is a demonstration engine showcasing architecture patterns and real-time voice orchestration design.
