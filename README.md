Intent-Orchestrated Agentic Workflow

A production-style agentic workflow built with LangGraph that converts natural language queries into schema-constrained execution plans and routes them through a deterministic, human-approved workflow.

This project demonstrates how to build intent-driven GenAI systems where:

an LLM is used only for understanding and planning (intent, entity, field-level filters)

execution is handled deterministically in code

control flow is managed via a graph-based orchestration layer

safety is enforced through explicit state schemas and human approvals

The system supports semantic querying across multiple entities (users, posts, comments) using real APIs (JSONPlaceholder), enabling flexible, natural-language data access without relying on brittle keyword rules or autonomous agents.

Key concepts demonstrated:

Intent routing with schema-constrained LLM outputs

Field-level semantic query planning

Graph-based orchestration using LangGraph

Deterministic tool execution

Human-in-the-loop approval gates

Agent-ready architecture without premature autonomy

This project intentionally avoids full autonomous agents and instead focuses on production-correct agentic workflows, providing a solid foundation that can later evolve into planner/executor or multi-agent systems if required.
