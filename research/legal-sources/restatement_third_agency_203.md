# Doctrinal Source: Restatement (Third) of Agency §2.03 — Apparent Authority

| Metric | Details |
| :--- | :--- |
| **Instrument** | Restatement (Third) of Agency (Am. Law Inst. 2006), §2.03 |
| **Legal Status** | Persuasive (not binding statute) — widely adopted by state courts as the controlling articulation of apparent authority |
| **Relevance to Paper A** | Defines the scope-of-binding-power test that determines *how far* an LLM agent's apparent power to bind its principal extends. |

---

## 1. Text

> "Apparent authority is the power held by an agent or other actor to affect a principal's legal relations with third parties when a third party reasonably believes the actor has authority to act on behalf of the principal and that belief is traceable to the principal's manifestations."

## 2. Elements

1. **Power to affect legal relations** — the agent's act can create binding legal consequences for the principal.
2. **Reasonable belief** — the third party (e.g., the customer chatting with a support bot) must reasonably believe the actor has authority.
3. **Traceable to the principal's manifestations** — critically, the belief cannot rest on the agent's own say-so alone; it must trace back to something the principal (the deploying company) said or did — e.g., deploying a branded chatbot on its own domain, with no disclaimer, is itself a manifestation of authority.

## 3. Why This Matters for Paper A

This is the doctrine that supplies the paper's **liability-scoping argument**, complementing UETA §14 (which establishes *that* a contract can form) with the test for *what a court will hold the principal to*:
- A company that deploys an LLM support agent without guardrails or disclaimers manifests apparent authority broadly — a customer's reliance on the agent's promises (discounts, refunds, warranty terms) is more likely "reasonable" and thus binding.
- Conversely, disclosed limitations (e.g., "I cannot authorize discounts above X%; a human will confirm") narrow the scope of apparent authority a court will find reasonable to rely on.
- This directly motivates the paper's technical argument: a **transactional gate** (like Gavel's `LAW-01` rule and its planned extensions) is not just a security control — it is evidence a company can point to that it did not manifest unlimited authority, narrowing its Restatement §2.03 exposure.

## 4. Verification Status (updated) — found a squarely on-point, very recent appellate case

**Caribbean Sun Airlines Inc. v. Halevi Enterprises LLC**, No. 199, 2024 (Del., argued from Delaware
Superior Court C.A. No. N21J-04427), decided by the Delaware Supreme Court **January 21, 2025** —
reversing the Superior Court. This is an unusually good fit: the case is *about* §2.03's
traceability element specifically, not apparent authority generally.

**Source note:** direct access to the Delaware Supreme Court's own opinion PDF was blocked to
automated fetching (CanLII-style 403). Instead, the Appellants' Opening Brief (filed July 9, 2024,
Case No. 199,2024, EFiled with the Delaware Supreme Court — a genuine primary-source court filing,
not a secondary summary) was fetched and read directly. Three independent secondary sources (a
Casemine commentary, a Justia case page, and general web search) consistently confirm the Supreme
Court reversed and agreed with the argument excerpted below — but the Court's own opinion language
itself has not been directly read. **Before final publication, pull the actual opinion text to
confirm the Court adopted this reasoning in these terms, not just the result.**

**Facts:** Alan Boyer falsely told lender Halevi Enterprises he was CEO of Caribbean Sun Airlines
and Miami Air International, obtained a $7,000,000 loan (Halevi later sought $25M+ via confessed
judgment), using documents Boyer himself supplied and that Halevi never independently verified.
Halevi never contacted the companies' actual sole owner. The Superior Court held Halevi reasonably
believed Boyer had apparent authority and entered judgment against the companies; the companies
appealed.

**The exact question presented (verbatim, brief p.22) is a clean statement of §2.03's traceability
element:** *"Does Delaware law permit a lender to reasonably believe that someone is an apparent
agent of a borrower when: (A) that belief cannot be traced to the borrower's manifestations; and
(B) the lender fails to ascertain and/or further investigate the scope of the apparent agent's
authority where the lender (i) obtained its documents from the agent, (ii) ignored documents it
received contradicting the agent's apparent authority, and (iii) failed to investigate further..."*

**Argument heading I.C.3 (brief p.29):** *"The Superior Court erred in holding that Halevi could
rely on Boyer's conduct alone absent any manifestations from Appellants."* — this is the exact
§2.03 point Paper A's `LAW-03`/`llama-3.3-70b-versatile` discussion turns on: an agent's own
self-serving representations, uncorroborated by anything the principal itself did or said, do not
establish apparent authority.

**Underlying Delaware apparent-authority case law cited in the brief** (all verified present in the
brief's own Table of Authorities, not independently re-verified against their own primary text):
`Billops v. Magness Const. Co.`, 391 A.2d 196, 199 (Del. 1978) (apparent authority is a question of
fact); `Parke Bancorp Inc. v. 659 Chestnut LLC`, 217 A.3d 701, 710 (Del. 2019) (standard of review —
factual findings reviewed for clear error, legal conclusions de novo); `Int'l Boiler Works Co. v.
Gen. Waterworks Corp.`, 372 A.2d 176 (Del. 1977); `Finnegan Const. Co. v. Robino-Ladd Co.`, 354 A.2d
142 (Del. Super. Ct. 1976); `Limestone Realty Co. v. Town & Country Fine Furniture & Carpeting,
Inc.`, 256 A.2d 676 (Del. 1969).

**Relevance to Paper A:** directly supports the paper's `LAW-03` discussion (§4.3) that traceability
can fail even when an agent (human or AI) makes confident, specific representations — what matters
is whether the *principal itself* manifested the authority, not merely whether the agent claimed
it convincingly. An LLM agent confidently claiming to be "John, a five-year employee" is
structurally the same failure pattern as Boyer confidently claiming to be CEO: confident
self-representation by the agent, with nothing from the principal to trace it to.

**Remaining open item (not done in this pass):** cross-check against Restatement §2.03's companion
sections on inherent agency power / estoppel — not pursued given time; flagged as a real gap if the
paper's scope expands to address those distinct theories.

**Follow-up verification pass — strengthened, not fully closed.** A direct fetch of the Court's own
opinion (Justia's case page, law.justia.com/cases/delaware/supreme-court/2025/199-2024.html) was
blocked (HTTP 403), same as before. However, an independent web search surfaced content describing
the Court's own reasoning (not the brief's) that matches the brief's argument closely: the Court
"emphasized that apparent authority must be based on the principal's manifestations, not solely on
the agent's conduct," and "concluded that the borrower lacked apparent authority" — reversing on
that basis. This is a second, independent corroboration beyond the three secondary sources already
cited above, and it specifically describes the *Court's* holding rather than the appellant's
argument. It is still a search-engine-summarized secondary description, not a verbatim primary
read — the recommendation stands: pull the actual opinion text directly before quoting the Court's
own language in the final draft.

**CLOSED — full primary-source read completed.** The user obtained the Court's own slip opinion PDF
(`2025-199-2024.pdf`, 30 pages, filed alongside this dossier) and it was read directly in full:
*Caribbean Sun Airlines Inc. v. Halevi Enters. LLC*, No. 199, 2024 (Del. Jan. 21, 2025) (Traynor, J.,
for the Court en banc). This is now a genuine primary-source citation, not a brief or secondary
reproduction.

**The Court's own formulation of the §2.03 test (p.16), verbatim:** *"apparent authority 'is the
power held by an agent or other actor to affect a principal's legal relations with third parties
when a third party reasonably believes the actor has authority to act on behalf of the principal
and that belief is traceable to the principal's manifestations.'"* (quoting *Parke Bancorp, Inc. v.
689 Chestnut LLC*, 217 A.3d 701, 712 (Del. 2019), quoting *Vichi v. Koninklijke Philips Elecs.,
N.V.*, 85 A.3d 725, 799 (Del. Ch. 2014)) — this is Delaware's own restated version of Restatement
§2.03's black-letter text, essentially word-for-word.

**The single most citable line for Paper A's thesis (p.17):** *"apparent authority can never be
derived from the acts of the agent alone."* This is the exact doctrinal point the `LAW-03`/
`llama-3.3-70b-versatile` discussion in outline §4.3 already makes about the model's own
self-representation ("I'm John...") — now backed by the Delaware Supreme Court's own words, not an
inference from the brief.

**Holding (pp. 17–29):** the Superior Court's error was affording "primacy to the agent's conduct
and representations to the virtual exclusion of any manifestations by" the principals. On *de novo*
review, the Court held none of the evidence Halevi relied on — Boyer's own signed "Officer's
Certificate," a private placement memorandum created by Boyer's own entity, forged board
documents, or Boyer's physical access to the companies' facilities — constituted a *manifestation
by the principal*, as opposed to self-serving conduct by the purported agent himself. Access to
facilities/records "granted to employees who have no authority to bind an entity is done frequently
in the ordinary course of business" and, without more, cannot establish apparent authority for a
major transaction (p.26). The Court reversed and vacated the confessed judgment in full (p.30).

**Case law now confirmed as actually used by the Court itself** (previously only confirmed present
in the brief's Table of Authorities, one level removed): *Parke Bancorp, Inc. v. 689 Chestnut LLC*,
217 A.3d 701 (Del. 2019); *Billops v. Magness Constr. Co.*, 391 A.2d 196, 197 (Del. 1978);
*Finnegan Constr. Co. v. Robino-Ladd Co.*, 354 A.2d 142, 144 (Del. Super. Ct. 1976); *Int'l Boiler
Works Co. v. Gen. Waterworks Corp.*, 372 A.2d 176, 177 (Del. 1977); Restatement (Third) of Agency
§3.03 (2006) (how apparent authority is created) and §2.01 (2006) (actual authority, for contrast).

**Bluebook pin-cite going forward:** *Caribbean Sun Airlines Inc. v. Halevi Enters. LLC*, No. 199,
2024, at 16–17 (Del. Jan. 21, 2025). No further verification action needed on this source.
