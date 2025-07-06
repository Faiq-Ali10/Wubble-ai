# Agent Evaluation & Correctness

## How would you measure whether your agent is taking the correct action in response to the prompt?

To measure agent correctness, I use a combination of **automated evaluation** and **tool-specific validation logic**:

- **Tool Usage Auditing**: Track which tool the agent invokes (e.g., SerpAPI for real-time info, Calculator for math). This is compared against the expected tool usage based on the prompt type.
- **Schema Validation**: Ensure outputs conform to the `AgentResponse` schema using Pydantic.
- **Prompt-Response Testing**: Run unit tests with varied inputs (factual, edge-case, ambiguous) and use regex or rule-based validators to assert correctness.
- **LLM-as-Judge (Optional)**: For subjective or nuanced prompts, use a secondary LLM with a static rubric to evaluate the appropriateness of responses.

## Propose a mechanism to detect conflicting or stale results

To detect and mitigate stale or conflicting outputs:

- **Timestamp Injection**: Embed a retrieval timestamp in the response from real-time tools.
- **Source Traceability**: Ensure the response includes reference to the tool used (e.g., "According to SerpAPI..." or "Wikipedia says...").
- **Cross-tool Validation**: When appropriate, cross-check information between tools (e.g., verify Wikipedia facts with Search if recent).
- **Content Drift Detection**: Use hash/version tracking for sources and flag mismatches across identical queries.
- **Timeout & Retry Logic**: If a real-time tool fails or is slow (e.g., LLM latency), fallback to static/default error responses ("I don't know.").

---

# Prompt Engineering Proficiency

## How do you design system prompts to guide agent behavior effectively?

An effective system prompt is **task-specific, unambiguous, and strict on tool use**. I follow this structure:

- **Goals Definition**: Clearly state what the agent must optimize for (e.g., correctness, minimal tool use).
- **Tooling Instructions**: Specify which tools to use for which cases (e.g., always use `Search` for recent data).
- **Reasoning Constraints**: Include phrases like "Never guess", "Do not override tool output", "Use one tool per prompt".
- **Response Structure**: Define expected response format (short, focused, justified if needed).
- **Fallback Behavior**: Define responses for edge-cases like unknowns ("If the answer cannot be found, say 'I don't know'.").

## What constraints, tone, and structure do you enforce, and how do you test them?

### Constraints:
- One relevant tool per prompt
- Use tools only when necessary
- No hallucinations or guessing
- Always return accurate, short answers
- Do not synthesize data unless clearly instructed

### Tone:
- Professional
- Clear and concise
- Factual over speculative

### Structure:
- Tool-used → Observation → Reasoned response
- If tool not used, include explanation why
- Include response key (e.g., `{"response": "..."}`) for schema compliance

### Testing:
- **Rule-based test cases** for behavior validation
- **Edge-case prompts** for constraint checking
- **Adversarial testing** (confusing or tricky inputs)
- **LLM-in-the-loop** to critique responses under a rubric
