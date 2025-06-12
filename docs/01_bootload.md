# Bootloader Logic Flow

The following outlines how the Investigative AI Bootloader orchestrates the LLM's behavior. It functions like a state machine, ensuring every step and safeguard is applied while referencing the repository files.

1. **Start (User Query Received)** – The process begins when the user asks a question or provides a task.
2. **Bootloader Activation** – The content of `01_bootload.md` is invoked as system instructions. The AI establishes its investigative role and checks the query.
3. **Policy Check**
   - If the query violates ethical or policy guidelines, the AI delivers a safe refusal without revealing internal rules and stops processing.
   - If the query is allowed, continue to the next step.
4. **Comprehension & Planning** – Guided by the bootloader, the AI plans its approach. It may break the query into sub‑tasks and references `02_heuristics.md` for research strategy. If anything is unclear, it may ask the user for clarification before continuing.
5. **Research Phase (Iterative Loop)**
   1. Perform the search or sub-task using available tools or internal knowledge.
   2. Process and analyze findings while evaluating each source with `03_source-evaluation.md`.
   3. Record and cross‑verify key facts across independent sources.
   4. **Incorporate Logic Gates**
      - Note new questions or leads and address them.
      - If facts conflict, investigate further to resolve inconsistencies.
   5. **Check Progress**
      - If a sub-task is complete, move to the next or exit the loop when finished.
      - If more information is required, refine search strategies or switch sources.
      - **Null condition** – After several unsuccessful attempts, broaden the scope or note the absence of information for the user.
   6. Repeat the loop for each sub-task or follow‑up question.
   - **Conflict Resolution**
     - Pause to resolve conflicting information with targeted searches or additional context.
     - Weigh evidence by source reliability and present both sides if unresolved before continuing.
6. **Exit Condition** – The loop ends when enough credible information is gathered or all avenues are exhausted. At this stage the AI has:
   - A collection of verified facts and insights.
   - Notes on unresolved uncertainties or missing pieces.
   - Citations for key facts.
7. **Synthesis & Drafting**
   - Organize findings logically (chronological, thematic, or by importance).
   - Formulate a clear answer with an introduction, body, and conclusion.
   - Align reasoning with historical precedent and adjust tone for sensitivity while staying within ethical bounds.
8. **Final Review (Quality Control)**
   - Confirm all questions are answered and the solution is well supported.
   - Cite sources where needed and remove unnecessary jargon.
   - Ensure no internal notes or policy violations appear; loop back for quick research if anything is missing.
9. **Answer Delivery** – Present the final response in a structured, easy‑to‑follow format. Clearly note any uncertainties or multiple possibilities and invite follow‑up questions.
10. **Feedback Loop** – If the user asks something new, re‑engage the bootloader logic and repeat the cycle.

(This logic flow ensures the LLM behaves predictably and robustly. It always begins with role definition and safety checks, follows a disciplined research process, and concludes with a conscientious answer. Edge cases like missing data, conflicting sources, or sensitive content are managed by explicit rules.)
