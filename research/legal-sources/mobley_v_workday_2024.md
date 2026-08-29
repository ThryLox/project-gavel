# Case Dossier: Mobley v. Workday, Inc.

| Metric | Case Details |
| :--- | :--- |
| **Court** | U.S. District Court, Northern District of California |
| **Case No.** | 3:23-cv-00770-RFL |
| **Order Date** | July 12, 2024 (order on motion to dismiss first amended complaint); June 2025 conditional ADEA collective certification; **now well past that stage — see §4 below for the current (2026) posture: certified collective (~1.1B applications), a March 6, 2026 ADEA-applicability win for plaintiffs, and further amended complaints through at least March 2026.** |
| **Claims** | Title VII, ADEA, ADA, California FEHA — disparate impact from AI-driven applicant screening |
| **Central Theory** | Workday, a third-party HR software vendor, is an "agent" of its client-employers and therefore itself subject to federal antidiscrimination statutes |

---

## 1. Facts

Derek Mobley alleged that Workday's AI-based applicant-screening and recommendation tools disproportionately rejected applicants on the basis of race, age, and disability across the many employers who use Workday's platform to screen candidates. Mobley was not an employee of Workday — Workday is a software vendor, not the hiring employer — so the threshold legal question was whether Workday could be sued at all under statutes that generally target "employers."

## 2. Holding

The court allowed the case to proceed against Workday on an **agency theory**: because Workday's software performs a traditional employer function (screening and recommending candidates) with significant discretion delegated to it by the client-employers, Workday can be treated as an "agent" of those employers and thus falls within the statutory definition of "employer" for Title VII, ADEA, and ADA purposes — even though Workday itself never directly employed the plaintiff.

## 3. Relevance to Paper A

This case runs the agency argument in the **opposite direction** from Moffatt, and both directions matter for the paper:
- Moffatt: the **deploying company** is bound by its own agent's output (principal held liable for agent's representations to a third party).
- Mobley: the **AI vendor** is itself found to be an "agent" that can be independently liable, not merely a tool the employer used — pulling the vendor, not just the deployer, into direct liability.
- Together these establish that agency-based liability for LLM/AI systems is being litigated on **both ends of the vendor-deployer relationship simultaneously** — a structural point the paper should make explicitly: a Gavel-style pre-deployment audit is relevant evidence for *both* an enterprise deploying a third-party model and a vendor whose product performs an agent-like function for its customers.

## 4. Verification Status (updated) — litigation has advanced substantially since the June 2025 status this dossier originally reported

The case is far more developed than "conditional ADEA collective certification, June 2025." Confirmed
via multiple independent sources (web search corroborated by an April 2026 status-summary article
plus consistent references to a Courthouse News PDF mirror and a govinfo.gov docket PDF — the
official CourtListener docket itself returned HTTP 403 to automated fetching, so this is
secondary-source corroboration, not a direct docket read):

- **March 6, 2026** — Judge Rita Lin (N.D. Cal.) rejected Workday's central remaining defense: that
  the ADEA doesn't cover job *applicants*, only current employees. The court held the Supreme
  Court's 2024 *Loper Bright* decision (overturning *Chevron* deference) did not disturb the prior
  precedent extending ADEA protection to applicants, and that the relevant EEOC interpretation
  remains persuasive under *Skidmore*. A significant defeat for Workday's litigation strategy.
- **February 17, 2026** — court authorized formal collective opt-in notice (deadline March 7,
  2026). The certified collective covers *"all individuals aged 40 and over who applied for job
  opportunities using Workday... and were denied employment recommendations,"* spanning
  September 2020 to present — reported scope: **approximately 1.1 billion rejected applications**.
  This is a dramatically larger scale than the dossier's original "conditional certification"
  framing conveyed.
- **March 30, 2026** — plaintiffs filed an amended complaint reasserting California FEHA claims and
  disability-discrimination claims with more specific factual allegations, after partial dismissal
  with leave to amend.
- **June 22, 2026** (per independent secondary corroboration, not the article above) — Judge Lin
  largely denied Workday's motion to dismiss a further amended complaint, including rejecting the
  argument that California's antidiscrimination laws don't reach Workday's screening of applicants
  located outside California.
- **The core "Workday is an agent of its client-employers" theory this dossier is cited for
  remains intact and central** — it is still the operative theory the ADEA/Title VII/ADA claims
  proceed under, now with an expanded factual record (a July 2025 disclosure order reportedly
  required Workday to identify its employer-clients using the implicated "HiredScore" AI features,
  expanding the collective's scope further).

**Net effect on Paper A:** the underlying doctrinal point this dossier supports (§3.2 — Mobley as
the vendor-side half of the "agency liability on both sides of the deployer/vendor relationship"
structural point) is unaffected and, if anything, strengthened by the case's continued survival
through multiple dismissal attempts. But any language in the paper stating or implying the case is
still at an early, "conditional certification" stage would now be **stale and should be corrected**
to reflect that merits litigation is well underway with a certified collective in the billions of
applications. Recommend citing this dossier's update date/session rather than the original June
2025 status if the paper quotes a specific procedural posture.

- [x] Distinguish this "AI-as-agent-of-employer" theory (statutory employment-discrimination agency) clearly from the apparent-authority contract theory (Restatement §2.03) — done at the outline level, see `research/paper-a-agent-liability-outline.md` §3's doctrinal scope note (added during an adversarial review pass).

**Follow-up verification pass.** Direct CourtListener docket access remains blocked (HTTP 403,
unchanged). Re-checked via an independent secondary source (aigovernanceforhr.com, April 2026
status article) not previously fetched directly — it corroborates every date and
figure above without discrepancy (March 6, 2026 ADEA ruling; Feb. 17, 2026 opt-in notice; March 30,
2026 amended complaint; ~1.1B applications in the certified collective). This is independent
re-confirmation that the dossier's citations describe real, accurately-quoted articles, not
hallucinated content — still not a direct docket read, so the recommendation to pull the docket
directly before quoting a precise procedural detail stands.

**Partial primary-source close.** The user obtained the actual original complaint PDF
(`gov.uscourts.cand.408645.1.0_1.pdf`, docket entry 1, filed by Winston Cooks LLC on behalf of Derek
Mobley) and it was read directly in full (16 pages). This confirms the case's foundational filing
and, more importantly, surfaces the exact statutory hook for the "agent" theory that the dossier's
§2 summarized but hadn't quoted: **Title VII §701(c), 42 U.S.C. §2000e(c), defines "employment
agency" as "any person regularly undertaking with or without compensation to procure employees for
an employer or to procure for employees opportunities to work for an employer, and includes an
agent of such a person"** (Compl. ¶25, emphasis added) — the complaint states directly, "Workday,
Inc. is an employment agency under Title VII." This is the literal statutory text the "vendor as
employer's agent" theory is built on, not just a judicial gloss — a stronger citation than the
dossier previously had for that specific point.

**Scope of this partial close:** this document is the original February 2023 complaint, not the
2026 procedural developments. **The complaint's core theory and statutory basis are now
primary-verified; the 2026 case-status claims (certification, ADEA ruling, ~1.1B-application
figure) still rest on secondary-source corroboration only** — pulling the current docket directly
remains worthwhile before quoting a 2026-specific figure or date precisely.

**Bluebook pin-cite for the statutory theory itself (now primary-sourced):** Class Action Complaint
¶25, *Mobley v. Workday, Inc.*, No. 3:23-cv-00770 (N.D. Cal. filed Feb. 21, 2023) (quoting 42
U.S.C. §2000e(c)).
