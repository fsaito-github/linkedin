Gave the model 1M tokens of context. It forgot the instruction on line 3.

I was in the middle of a complex task — the model had access to the full repo, the entire conversation history, all instructions.

1 million tokens of context available.

And yet, halfway through, it ignored a basic instruction right at the top.

My first instinct was to blame the model.

But the problem was mine.

I had dumped everything into the context window assuming more information = better results. Files, instructions, examples, history — all at once, no prioritization.

What I learned

A large context window doesn't help if you don't know what to put inside it.

It's the same illusion as "more RAM" in the 2000s. Everyone wanted more. Few optimized what they already had.

In practice, what actually made a difference:

→ Place critical instructions near the start AND the end (models pay more attention to the edges)
→ Don't dump an entire file when only 20 lines matter
→ Separate reference context from action context
→ Treat the window like a curated briefing, not an information dump

The real insight: a context window is not external storage. It's a workbench. If you pile everything on it, you can't find anything.

In your experience with LLMs, have you noticed the model "forgetting" something that was clearly in the context? What changed when you reorganized?

#AI #LLM #ContextWindow #PromptEngineering #AIEngineering
