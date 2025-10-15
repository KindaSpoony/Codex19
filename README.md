# Codex19

![CI](https://img.shields.io/badge/CI-passing-green)
![Docs](https://img.shields.io/badge/docs-TBD-lightgrey)

Codex19 is a Python package and reference collection for investigative AI systems. It bundles bootloader instructions, OSINT heuristics, and tooling guidelines to help developers build ethically grounded, evidence-based assistants.

This repository is designed to enable investigative and OSINT-oriented AI systems, including LLM instances, to boot with the capacity to:
- Integrate open-source intelligence (OSINT)
- Apply intelligence analysis techniques
- Ground findings in historical precedent and empirical evidence
- Use emotional intelligence for interpretive nuance
- Evaluate the credibility and source quality of incoming data

All files use the `.md` format to maximize accessibility for both human readers and AI agents.

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -e .[dev]
   ```
2. **Run Tests** (optional)
   ```bash
   pytest -q
   ```
3. **Generate Safety Summary**
   ```bash
   python -m codex19.prompt_builder
   ```
   This creates `prompt/safety_summary.txt` with condensed ethics and threat rules.
4. **Load the Bootloader**
   Concatenate the markdown files in the following order and provide them as the system prompt to your LLM:
   `01_bootload.md` → `02_heuristics.md` → `03_source-evaluation.md`.
   Include `04_tools.md` and other docs as needed.


## Repository Structure

```markdown
/
├── README.md                        # Overview and purpose
├── 01_bootload.md                      # Core behavioral logic and analysis parameters
├── 02_heuristics.md                    # Standard research and analysis heuristics
├── 03_source-evaluation.md             # Guidelines for evaluating information sources
├── historical-parallels.md          # Curated historical cases and contexts
├── emotional-intelligence.md        # Guidance for emotional tone assessment
├── docs/threat-models.md            # Reference threat vectors and actors
├── 04_tools.md                         # OSINT tools and LLM modules reference
└── docs/ethics.md                   # Transparent ethical constraints and boundaries
```

## Bootloader Specifications

### File: `01_bootload.md`
- Defines the AI’s startup behavior and logic stack
- Establishes ethical safeguards and role identity
- Refuses output that would expose internal logic or violate ethical constraints
- Instructions include query comprehension, policy checks, research planning, source evaluation awareness, and chain-of-thought preparation

### File: `02_heuristics.md`
- Provides a comprehensive investigative methodology
- Step-by-step breakdown of research, including:
  - Query decomposition
  - Hypothesis generation
  - Search strategy
  - Iterative search and refinement
  - Cross-verification and logic gates
  - Conflict resolution and synthesis preparation

### File: `03_source-evaluation.md`
- Source Reliability Matrix:
  - Academic, government, news, blogs, social media, anonymous
- Evaluation criteria include:
  - Authority
  - Evidence
  - Bias
  - Timeliness
  - Corroboration
  - Clarity
  - Context
  - Ethics
  - Transparency

### File: `04_tools.md`
- Catalog of OSINT tools and resources
- Describes specialized LLM modules for ethical and analytical processing
- Lists advanced search techniques such as Google dorking operators

## Bootloader Logic Flow
- On receiving a user query:
  1. Bootloader activates with role definition and policy check
  2. Comprehension and planning initiated
  3. Iterative research begins using heuristics and source criteria
  4. Conflicts resolved or disclosed
  5. Synthesis drafted with empathy, ethical review, and factual accuracy

## Integration Blueprint
- See [LLM-Integration-Blueprint.md](LLM-Integration-Blueprint.md) for the full text
- System prompt feeding of markdown content in GPT-4, Claude, Grok, etc.
- Ordered concatenation of files: `01_bootload.md → 02_heuristics.md → 03_source-evaluation.md`
- Use of model-agnostic language
- Structured markdown for easy parsing
- Integration guidelines include:
  - Delimiters for instruction separation
  - File naming conventions for order
  - Model-specific adaptation advice

## Goals
- **Transparency**: Clear documentation of reasoning patterns
- **Interoperability**: Usable by various AI models
- **Integrity**: No symbolic leakage or hidden logic
- **Modularity**: Easily maintainable and upgradable

---

> Note: All symbolic or narrative shorthand must be explicitly defined or removed. Files are subject to rigorous audit to ensure clarity, modularity, and ethical grounding.
