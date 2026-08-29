# Doctrinal Source: UETA §14 — "Automated Transaction"

| Metric | Details |
| :--- | :--- |
| **Instrument** | Uniform Electronic Transactions Act (1999), §14 |
| **Adopting Jurisdictions** | 49 U.S. states (all but New York, which has its own e-sign statute), D.C., Puerto Rico, U.S. Virgin Islands |
| **Federal Analogue** | E-SIGN Act, 15 U.S.C. §7001 et seq. (federal floor; UETA governs in adopting states) |
| **Relevance to Paper A** | Establishes that a contract can already form through an "electronic agent" with no human review — the doctrinal floor under any LLM-agent transaction argument. |

---

## 1. Text (paraphrase of the operative provision — verify exact statutory language for the adopting state before quoting in the draft)

UETA §14 provides that a contract may be formed by:
1. The interaction of **electronic agents of both parties**, even if no individual was aware of or reviewed the agents' actions or the resulting terms; or
2. The interaction of **an electronic agent and an individual**, including where the individual performs an action they are free to refuse but which they know or have reason to know will cause the electronic agent to complete a transaction.

"Electronic agent" is defined elsewhere in UETA (§2(6)) as a computer program or electronic means used to initiate an action, or respond to electronic records/performances, without review or action by an individual at the time of the action or response.

## 2. Legislative Purpose

The official comment to §14 explains the section was drafted to **negate any argument based on lack of subjective intent** when a machine, not a human, executes the transaction. Under UETA's framework, the requisite contractual intent is imputed from the act of **programming and deploying** the electronic agent, not from a human's contemporaneous mental state at the moment of formation.

## 3. Why This Matters for Paper A

This is the load-bearing doctrine that makes the paper's core claim *already true today*, not speculative:
- LLM agents that negotiate refunds, apply discounts, or issue commitments are squarely "electronic agents" under UETA §2(6).
- Under §14, the enterprise deploying the agent cannot escape contract formation by arguing "no human approved this" — that is precisely the scenario §14 was written to bind.
- This shifts the paper's central question from *"can an AI agent's output bind a company?"* (answered: yes, under decades-old e-commerce statute) to *"what apparent-authority and reliance conditions determine the scope of what it binds them to?"* — which is where Restatement (Third) of Agency §2.03 (see `restatement_third_agency_203.md`) and the emerging case law (`moffatt_v_air_canada_2024.md`, `mobley_v_workday_2024.md`) come in.

## 4. Verification Status (updated)

**California codification confirmed** — California Civil Code §1633.14, fetched directly from the
official legislature site (leginfo.legislature.ca.gov), verbatim:

> **(a)** In an automated transaction, the following rules apply:
> (1) A contract may be formed by the interaction of electronic agents of the parties, even if no
> individual was aware of or reviewed the electronic agents' actions or the resulting terms and
> agreements.
> (2) A contract may be formed by the interaction of an electronic agent and an individual, acting
> on the individual's own behalf or for another person, including by an interaction in which the
> individual performs actions that the individual is free to refuse to perform and which the
> individual knows or has reason to know will cause the electronic agent to complete the
> transaction or performance.
> **(b)** The terms of the contract are determined by the substantive law applicable to it.
>
> *(Added by Stats. 1999, Ch. 428, Sec. 1. Effective January 1, 2000.)*

"Electronic agent" is defined at Cal. Civ. Code §1633.2(f): *"a computer program or an electronic
or other automated means used independently to initiate an action or respond to electronic
records or performances in whole or in part, without review by an individual."* This confirms the
dossier's original paraphrase (§1 above) was accurate — the California codification tracks the
uniform-act model text essentially word for word, no material state variation found.

**Delaware codification confirmed** — Del. Code Title 6, §12A-114, fetched directly from the
official state code site (delcode.delaware.gov): *"In an automated transaction, the following
rules apply: (1) A contract may be formed by the interaction of electronic agents of the parties,
even if no individual was aware of or reviewed the electronic agents' actions or the resulting
terms and agreements. (2) A contract may be formed by the interaction of an electronic agent and
an individual... (3) The terms of the contract are determined by the substantive law applicable to
it."* Structurally and substantively identical to California's §1633.14 — confirms this is genuine
uniform-act boilerplate, not a state-specific variant, closing the "only California was checked"
gap.

**ULC official comment confirmed.** Comment 1 to UETA §14 states that the lack of contemporaneous
human intent does not defeat enforceability for contracts "formed by machines functioning as
electronic agents for parties to a transaction," and that "when machines are involved, the
requisite intention flows from the programming and use of the machine." This directly confirms
§2 above (the "imputed intent" characterization) was accurate to the ULC's own drafting purpose,
not an inference — closing the previously-flagged highest-exposure unverified claim in the paper.

**New York — genuine gap found, not just an unverified checkbox.** New York's non-UETA statute
(State Technology Law, Article 3, "Electronic Signatures and Records Act" — NY Senate legislation
site, §§301-309) was fetched section-by-section. **It contains no "automated transaction" or
"electronic agent" provision at all** — its 9 sections cover only electronic signature/record
validity, evidentiary admissibility, excluded transactions, privacy safeguards, and voluntariness
of participation. The definitions section (§302) defines "electronic," "electronic record,"
"electronic signature," "person," and "governmental entity" — **"electronic agent" is not among
them.** This is a real, substantive finding, not a technicality: New York has no dedicated statute
addressing whether a contract can form through an electronic agent's unreviewed action. A New York
court would have to reach that result (if at all) through ordinary common-law contract
formation doctrine (offer/acceptance/mutual assent inferable from conduct), not through an express
UETA-§14-equivalent grant. **Correction for the paper:** do not state or imply that New York
reaches "the same result" as the other 49 UETA-adopting jurisdictions — state instead that 49
states plus D.C. have an express statutory electronic-agent contract-formation rule, and New York
would require a common-law argument to reach an equivalent conclusion, which is a meaningfully
weaker doctrinal footing for any New York-specific claim this paper makes.
