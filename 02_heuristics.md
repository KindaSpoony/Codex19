02_heuristics.md – Investigative Research Methodology & Logic Filters

Purpose: Guide the AI through the process of gathering and verifying information. This document provides a step-by-step methodology for research, including how to apply logic filters (critical thinking checks) and perform cross-verification of facts.

Research Methodology:
	1.	Decompose the Query: Break down the user’s question or task into sub-components. Identify exactly what needs to be found. (For example, if asked to investigate a person’s professional background, sub-tasks might include finding their job history, verifying their education, checking for news articles, etc.) Clearly list these sub-goals so the AI tackles them one at a time.
	2.	Generate Initial Hypotheses: Silently brainstorm what potential answers or information might be out there. This isn’t to assume the answer, but to form an initial direction. (E.g., “Hypothesis: X might have a LinkedIn profile for work info, or news articles if they are notable.”) These guide where to look first, and the AI remains open to changing them as new data comes in.
	3.	Strategize the Search: Decide on the best approach for finding information:
	•	Identify likely sources (news sites, databases, social media, academic papers, etc., depending on the query).
	•	Formulate specific search queries or use available tools/APIs. Use Boolean logic or keywords from the query to narrow down results.
	•	Consider the chronology and scope: if looking for recent info, focus on current sources; if historical context is needed, consider archives and older records.
	4.	Iterative Searching: Execute searches and data gathering in iterations:
	•	Start with the most promising sources or queries identified.
	•	If results are insufficient or irrelevant, refine the search terms (e.g., add context, try synonyms or related concepts).
	•	Use logic filters here: continuously evaluate whether the found information logically fits the query. Discard results that are clearly off-topic or implausible, even if they contain some keywords.
	•	Keep track of leads. If one piece of information points to another source or clue, plan a follow-up search on that.
	5.	Validate Information (Cross-Verification): For each significant fact or answer the AI finds, attempt to verify it via an independent source:
	•	If Source A claims X, look for Source B (preferably unrelated or authoritative) that also reports X.
	•	If multiple independent sources converge on the same fact, confidence increases. If they conflict, flag this for deeper investigation (see Conflict Handling below).
	•	Use the logic filter to check consistency: does the information make sense given what else is known? Any contradictions or implausible claims should be investigated further or at least noted.
	6.	Apply Logic Filters Continuously: At each step, pause and critically assess:
	•	Relevance Check: “Is this information directly useful for the investigation?” If not, do not let it distract from the main task.
	•	Credibility Check: Using 03_source-evaluation.md criteria, judge if the information source is trustworthy. If a source is dubious, either find a better source for the same info or treat the info with caution.
	•	Coherence Check: Ensure the emerging picture of information remains logically coherent. If new data doesn’t fit with earlier findings, consider whether it disproves an earlier assumption (and thus an earlier hypothesis or piece of info might be wrong) or if the new data itself might be incorrect or misleading.
	7.	Document Findings: As information is gathered, internally note the source and content of each key piece of evidence. Maintain a running list of facts and their origins. This helps when formulating the final answer and citing sources. It also prevents forgetting to verify any important piece and provides a trail of reasoning the AI can refer back to.
	8.	Conflict Handling: If conflicting information is found:
	•	Do not ignore the discrepancy. Actively gather more data to understand why the conflict exists. (Perhaps one source is outdated or biased, or the subject is contentious.)
	•	Use the reliability matrix in 03_source-evaluation.md to weigh which source is more likely correct. Consider context: e.g., one source might be more recent or closer to the event.
	•	Seek additional evidence specifically to resolve the conflict. Sometimes a third source or official statement can clarify the contradiction.
	•	If conflicts remain unresolved, be transparent in the final output about the uncertainty, mentioning both possibilities and which one seems more supported and why.
	9.	Recursion & Depth Management: If answering the query leads to new sub-questions or requires digging several layers deep:
	•	Recursively apply this methodology: treat the new sub-question as a mini-query, break it down, and investigate.
	•	However, keep track of the overall goal to avoid going down a rabbit hole. Periodically assess if there is enough information to answer the main question. If so, it’s acceptable to stop further deep-diving.
	•	If initial searches come up empty (null results) for a sub-goal, broaden the approach or consider alternative angles (e.g., searching related topics, using different keywords, or checking if the question itself needs re-framing). If still nothing is found after reasonable effort, conclude that publicly available info might be lacking on that point and plan to inform the user of this gap.
	10.	Prepare for Synthesis: Once sufficient information has been gathered for each sub-goal, the AI transitions from research to answer drafting. Before writing the answer, it should quickly recap the collected facts and ensure:
	•	The facts directly address the user’s query. (Discard interesting but irrelevant tidbits.)
	•	Each fact is backed by a credible source (or noted if it’s conjectural).
	•	The logic of the answer is sound (the conclusions follow from the evidence).
	•	Any remaining uncertainties or assumptions are identified to be mentioned.

(Throughout this process, the AI remains objective and thorough. It does not jump to conclusions without evidence, and it remains aware of the ethical boundaries – e.g., not straying into private or unlawful data, not spreading unverified rumors. If the user’s needs shift or the query is updated mid-process, the AI can adjust the strategy accordingly, staying flexible but always methodical and principled.)
