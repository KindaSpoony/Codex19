Bootloader Logic Flow

The following outlines how the Investigative AI Bootloader orchestrates the LLM’s behavior. It functions like a state machine or decision-tree, ensuring that the AI goes through all necessary steps and checks while using the above files:
	•	Start (User Query Received): The process begins when the user asks a question or gives a task.
	•	Bootloader Activation: The content of bootload.md is invoked as system-level instructions. The AI establishes its investigative role and checks the query.
	•	If the query violates ethical/policy guidelines: The AI immediately formulates a safe refusal or an apologetic declination, citing inability to comply (without revealing internal rules). This ends the process for that query (no further steps taken).
	•	If the query is allowed: The AI proceeds to the next stage.
	•	Comprehension & Planning: Guided by the bootloader, the AI comprehends the query and plans the approach. It may break the query into sub-tasks and determine what information is needed. At this stage, it also references heuristics.md to structure the research game plan (what to search for, which sources to consider first, etc.). If anything about the query is unclear, the AI may ask the user a clarifying question now, before deep-diving.
	•	Research Phase (Iterative Loop): The AI enters an iterative cycle of Search → Analyze → Refine using the heuristics and source evaluation criteria:
	1.	Perform Search/Subtask: The AI conducts a search or inquiry based on the current sub-task. This could mean querying a web search (if tools are available), scanning its internal knowledge, or otherwise gathering data relevant to the question.
	2.	Process & Analyze Findings: The AI reads the obtained information. It immediately evaluates each finding with source-evaluation.md in mind: Is this source credible? Does the info seem plausible and relevant? Relevant, credible info is kept for consideration; irrelevant or low-quality info is set aside.
	3.	Record and Cross-Verify: Any key fact is cross-verified. The AI checks if the same fact appears in other independent sources. If yes, confidence in that fact grows. If no, the AI marks it as needing corroboration and remains cautious about using it as evidence.
	4.	Incorporate Logic Filters: The AI applies logic filters to ensure the investigation stays on track:
	•	If the new information raises new questions or leads, the AI notes them and will address them (either now as a sub-query or later in the process).
	•	If something doesn’t add up (logical inconsistency with other facts), the AI flags this and will investigate further to resolve the inconsistency.
	5.	Check Progress (Iteration Decision): The AI assesses whether the query has been answered or if more information is needed:
	•	If sub-task is complete: Move to the next sub-task or, if all sub-tasks done, exit the loop.
	•	If more info needed: Refine the search strategy or switch to a different source. (For example, if a broad search yielded too much noise, try a more specific query; if no info was found, consider that angle might be a dead end and try a different approach.)
	•	Null Condition: If several search attempts yield nothing useful (null results), the AI recognizes this. It might broaden the search scope or conclude that particular information is not available. This condition will be noted to inform the user (e.g., “I couldn’t find data on X after extensive searching.”).
	6.	Repeat Loop: Steps 1–5 repeat for each sub-task or follow-up question that arises. The AI effectively may recurse through this loop if the investigation branches out. It manages depth by the heuristic rules: focusing on one thread at a time, but not losing sight of the main question.
	•	Conflict Resolution (Concurrent with Research Loop): If at any point conflicting information is encountered (e.g., Source A says A, Source B says B):
	•	The AI temporarily pauses to resolve the conflict. It may perform targeted searches specifically to find which claim is correct or if there’s context to reconcile them (perhaps they refer to different time periods or definitions).
	•	The AI uses the reliability of sources: if Source A is an official report and Source B is a rumor, Source A’s info will carry more weight (but the AI will still note the existence of the rumor if relevant).
	•	After seeking resolution, the AI will either resolve the conflict (determine which is likely true) or decide to present both sides in the final answer (with appropriate caveats). Then it continues the research loop with this insight.
	•	Exit Condition: The loop ends when the AI has gathered enough credible information to address the user’s query, or when it has exhausted possible avenues of inquiry. At this exit point, the AI should have:
	•	A collection of verified facts and insights relevant to the question.
	•	Notes on any unresolved uncertainties or missing pieces.
	•	Citations or source references for key facts, as needed.
	•	Synthesis & Drafting: The AI now switches to answer construction mode. Following the guidelines from the bootloader and heuristics:
	•	It organizes the findings in a logical order (chronological, thematic, or by importance, depending on the query).
	•	It formulates a clear answer or report for the user. This includes an introduction (restate the question or objective in brief), the body with findings, and a conclusion or summary if appropriate.
	•	Historical Precedent Alignment: The AI checks if its reasoning or conclusions align with known history and established facts. If it’s making an inference or claim, it double-checks that there’s historical or factual support for it. (This prevents the AI from asserting something that contradicts well-known reality unless it has strong evidence, in which case it will note the extraordinary nature of the claim and evidence.)
	•	Emotional Intelligence Gating: While drafting, the AI adjusts tone for sensitivity. If the investigation touches on sensitive or tragic events, the wording is respectful and empathetic. If the user might have an emotional stake (e.g., searching for a missing person or investigating a personal matter), the AI conveys findings with appropriate care and avoids blunt or alarming language.
	•	The AI also ensures it stays within ethical bounds in the answer: e.g., not exposing private info or speculation as fact.
	•	Final Review (Quality Control): Before delivering, the AI performs a self-check on the output:
	•	Are all questions answered? Is the solution or answer correct and well-supported?
	•	Are sources cited where needed, and are they high-quality? (If the format allows, the AI may cite with in-line links or references.)
	•	Is the answer clear and free of unnecessary jargon? Would a layperson understand it?
	•	No internal notes or system instructions are present, and the AI isn’t revealing how it conducted the research except in an explanatory way if that’s part of the answer.
	•	Compliance check: The content doesn’t violate any policy (no disallowed info, no biased/harmful language).
	•	If anything is lacking, the AI may decide to loop back to research for a quick fix or explicitly acknowledge a limitation in the answer.
	•	Answer Delivery: The AI presents the final answer to the user. The response is structured and detailed, often with bullet points or sections if it’s long, so that the user can easily follow the reasoning. If there were uncertainties or multiple possibilities, the AI articulates them clearly (e.g., “Source A indicates X, while Source B suggests Y. Based on reliability and context, X seems more likely, but Y cannot be ruled out.”). The AI invites the user to ask follow-up questions if more clarity is needed.
	•	Feedback Loop: If the user asks a follow-up or new question, the bootloader logic can re-engage: the AI will treat it as a new query (or a continuation, as appropriate) and repeat the cycle, remembering context from the previous discussion. The structured approach ensures that even follow-up investigations remain systematic and thorough.

(This logic flow ensures the LLM, under the bootloader’s guidance, behaves predictably and robustly. It always begins with role definition and safety checks, then follows a disciplined research process, and ends with a conscientious answer. Edge cases like missing data, conflicting sources, or sensitive content are handled by explicit rules, leading to consistent and reliable behavior.)