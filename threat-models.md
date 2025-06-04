# threat-models.md

## Purpose
This document defines threat actor categories, methods, and vectors relevant to an OSINT-focused investigative AI. It outlines how adversaries exploit information and technology to spread disinformation, conduct cyber attacks, destabilize societies, and threaten critical systems. It emphasizes recognition of disinformation campaigns, cybercrime, ideological warfare, and covert influence.

## Taxonomy Table

| Actor Type             | Modus Operandi                                  | Primary Vector                          | AI Countermeasure Strategy             |
|------------------------|--------------------------------------------------|------------------------------------------|----------------------------------------|
| State Actors           | Influence ops, cyber espionage, hybrid warfare | State media, fake personas, deepfakes    | Detect coordinated behavior, validate content, trace narrative origins |
| Cybercriminal Syndicates | Phishing, extortion, fake narratives           | Phishing emails, dark web, fake news     | Pattern recognition, entity checks, financial hoax tracking |
| Disinformation Agents  | Ideological propaganda, narrative flooding      | Social media, forums, pseudo-media       | Behavior clustering, bot analysis, cross-platform theme tracing |
| Domestic Extremists    | Radicalization, hate propaganda, mobilization   | Encrypted chat, memes, forums            | Extremist lexicon filter, sentiment shift detection, risk flags |
| Covert NGOs / Fronts   | Narrative laundering, influence cloaking        | Reports, events, advocacy campaigns       | Network provenance analysis, funding/source triangulation |

## Threat Signatures

- **Narrative Timing Clusters**: Coordinated bursts of similar messaging
- **Synchronized Bot Bursts**: Simultaneous, repetitive messaging by networks
- **Data Void Exploitation**: Rapid content generation around unexplored terms
- **Multi-lingual Narrative Bridges**: Same narrative adapted cross-language to widen reach

## Escalation Thresholds

Escalation occurs when automated systems encounter:

1. **Credible Threats to Life/Infrastructure**
   - Incitement to violence
   - Coordinated sabotage messaging
   - AI flags immediately for human escalation

2. **Targeted Identity or Personal Harm**
   - Doxxing, impersonation, reputational attacks
   - Detected via patterns in account coordination or leak cascades

3. **Public Safety Misinformation**
   - Fake evacuation alerts, health hoaxes
   - Autonomous review suspended; forward to trusted human actors

4. **High-Impact Influence or Tampering**
   - Election disinfo, synthetic media aimed at destabilization
   - Mass botnets, adversarial inputs to manipulate AI logic

## Integration Protocol
Each detected pattern initiates:
- Source tracing
- Vector verification
- Cross-language/narrative correlation
- Volume and velocity checks

When a redline is breached, the system:
- Halts autonomous assessment
- Transfers evidence chain
- Initiates chain-of-review with human analyst audit trail

This threat model is designed to evolve through periodic audit and should be re-trained against emerging actors, techniques, and geopolitical shifts.
