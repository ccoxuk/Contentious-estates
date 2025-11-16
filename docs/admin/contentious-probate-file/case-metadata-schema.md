---
title: "Case Metadata Schema - Contentious Probate"
author: "Legal Practice Team"
date: "2025-11-16"
version: "1.0"
status: "Standard"
category: "Administrative - File Management"
tags: ["metadata", "case-management", "data-schema"]
---

# Case Metadata Schema - Contentious Probate

<!-- This document defines required metadata fields for contentious probate matters -->

## Purpose

To establish standardized metadata fields for all contentious probate matters, enabling effective case management, reporting, searching, and analysis.

---

## Essential Metadata Fields

### Matter Identification

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Matter Reference | Text | Yes | CP-2025-1234 | Unique identifier |
| Matter Name | Text | Yes | Smith Estate Dispute | Short descriptive name |
| Client Name | Text | Yes | Jane Smith | Full legal name |
| Deceased Name | Text | Yes | John Smith | Full legal name |
| Date Opened | Date | Yes | 2025-11-16 | Matter opening date |
| Date Closed | Date | No | 2026-06-15 | When matter concludes |
| Matter Status | Dropdown | Yes | Active/Closed/On Hold | Current status |

### Case Classification

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Practice Area | Dropdown | Yes | Contentious Probate | Fixed value |
| Claim Type | Multi-select | Yes | Lack of Capacity | Primary dispute type |
| Sub-Type | Multi-select | No | Undue Influence | Secondary issues |
| Jurisdiction | Dropdown | Yes | High Court/County Court | Where case is/will be |
| Court Location | Text | No | Manchester | Specific court |
| Claim Number | Text | No | HC-2025-000123 | When issued |

**Claim Type Options:**
- Lack of Testamentary Capacity
- Undue Influence
- Lack of Knowledge and Approval
- Fraudulent/Forged Will
- Wills Act Non-Compliance
- Inheritance Act Claim
- Executor Misconduct
- Construction/Interpretation
- Proprietary Estoppel
- Other

### Parties

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Client Role | Dropdown | Yes | Claimant/Defendant | Client's position |
| Opponent Name(s) | Text | Yes | Robert Jones (Executor) | Key opponents |
| Opponent Solicitors | Text | No | Smith & Co Solicitors | If known |
| Executor Name(s) | Text | Yes | Robert Jones | Personal representatives |
| Number of Beneficiaries | Number | No | 4 | For tracking |

### Financial

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Estate Value (Gross) | Currency | Yes | £500,000 | Estimated gross value |
| Estate Value (Net) | Currency | No | £450,000 | After liabilities |
| Claim Value | Currency | No | £150,000 | Value of client's claim |
| Matter Value Band | Dropdown | Yes | £100k-£500k | For reporting |
| Funding Type | Dropdown | Yes | Private/CFA/DBA | How funded |

**Matter Value Bands:**
- Under £50k
- £50k-£100k
- £100k-£250k
- £250k-£500k
- £500k-£1m
- Over £1m

### Deadlines and Milestones

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Limitation Deadline | Date | Yes | 2026-05-16 | Critical deadline |
| Limitation Type | Dropdown | No | Inheritance Act 6 months | Type of limitation |
| Date of Death | Date | Yes | 2025-05-15 | Deceased's date of death |
| Date of Grant | Date | No | 2025-11-15 | When probate obtained |
| Proceedings Issued | Boolean | Yes | Yes/No | Whether issued |
| Date Issued | Date | No | 2025-12-01 | When claim issued |
| Trial Date | Date | No | 2026-06-15 | If listed |

### Team and Responsibility

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Fee Earner | Dropdown | Yes | Jane Solicitor | Responsible solicitor |
| Supervisor | Dropdown | Yes | Senior Partner | Supervising partner |
| Billing Partner | Dropdown | No | Partner Name | For billing |
| Secretary | Dropdown | No | Secretary Name | Support staff |
| Counsel Instructed | Text | No | John Barrister | If instructed |
| Experts Instructed | Text | No | Dr. Smith (Capacity) | If instructed |

### Risk and Prospects

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Risk Rating | Dropdown | Yes | High/Medium/Low | Overall risk level |
| Prospects of Success | Dropdown | No | Strong/Reasonable/Weak | Merit assessment |
| Limitation Risk | Dropdown | Yes | High/Medium/Low | Specific limitation risk |
| Costs Risk | Dropdown | No | High/Medium/Low | Costs exposure risk |

### Case Management

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Current Stage | Dropdown | Yes | Pre-Action/Pleadings/etc. | Case progress |
| Next Key Date | Date | No | 2025-12-01 | Next milestone |
| Next Action | Text | No | File Defence | Next step required |
| Last Reviewed | Date | Yes | 2025-11-20 | Last file review |
| Review Frequency | Dropdown | Yes | Weekly/Monthly | How often to review |

**Current Stage Options:**
- Initial Assessment
- Pre-Action
- Proceedings Issued
- Pleadings
- Disclosure
- Evidence Exchange
- ADR/Settlement Discussions
- Pre-Trial
- Trial
- Post-Trial
- Enforcement
- Closed

### Source and Marketing

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| Source of Instruction | Dropdown | No | Referral/Website/etc. | How client found firm |
| Referrer | Text | No | Previous Client | If referred |
| Marketing Campaign | Text | No | Contentious Probate 2025 | For tracking |

---

## Document Metadata

### For Individual Documents

| Field | Type | Required | Example |
|-------|------|----------|---------|
| Document Type | Dropdown | Yes | Letter/WS/Pleading |
| Document Date | Date | Yes | 2025-11-20 |
| Document Status | Dropdown | Yes | Draft/Final/Filed |
| Author | Text | Yes | Fee Earner Name |
| Privilege Status | Dropdown | Yes | Privileged/Non-privileged |
| Related Party | Dropdown | No | Client/Opponent/Court |
| Version Number | Text | No | v01, v02, FINAL |

---

## Reporting Categories

### For Management Reports

| Field | Type | Example |
|-------|------|---------|
| Matter Type | Dropdown | New/Existing |
| Conflict Check Status | Dropdown | Cleared/Pending |
| Costs Recovery Prospects | Dropdown | Good/Moderate/Poor |
| Settlement Prospects | Dropdown | High/Medium/Low/None |
| ADR Attempted | Boolean | Yes/No |
| Outcome | Dropdown | Settled/Trial Win/Trial Loss/etc. |

---

## Custom Fields for Contentious Probate

### Will-Specific Fields

| Field | Type | Required | Example |
|-------|------|----------|---------|
| Will Date | Date | Yes | 2020-03-15 |
| Will Drafter | Text | No | ABC Solicitors |
| Earlier Will Date(s) | Date | No | 2015-06-20 |
| Codicils | Boolean | No | Yes/No |

### Medical/Capacity Fields

| Field | Type | Required | Example |
|-------|------|----------|---------|
| Capacity Issue | Boolean | Yes | Yes/No |
| Medical Condition | Text | No | Dementia |
| Medical Expert Needed | Boolean | No | Yes/No |
| Medical Records Obtained | Boolean | No | Yes/No |

### Inheritance Act Specific

| Field | Type | Required | Example |
|-------|------|----------|---------|
| Claimant Category | Dropdown | No | Spouse/Child/Dependant |
| Provision Under Will | Currency | No | £0 |
| Provision Sought | Currency | No | £150,000 |

---

## Data Entry Standards

### Required at Matter Opening

- All "Essential" metadata fields
- Matter identification fields
- Case classification
- Key parties
- Financial estimates
- Risk ratings
- Team assignments

### Update Frequency

**Daily/As Occurs:**
- Next Key Date
- Next Action
- Document metadata

**Weekly:**
- Current Stage
- Matter Status

**Monthly:**
- Last Reviewed
- Risk Rating
- Prospects assessment

**As Changes:**
- Claim Number (when issued)
- Trial Date (when listed)
- Counsel/Expert (when instructed)
- Outcome (when concluded)

---

## Data Quality

### Validation Rules

- Matter Reference must be unique
- Date Opened cannot be in future
- Date Closed must be after Date Opened
- Estate Value must be positive number
- Limitation Deadline must be in future for active matters

### Mandatory Fields Check

Before case can proceed past initial stage:
- [ ] All required fields completed
- [ ] Matter Reference assigned
- [ ] Limitation Deadline diarized
- [ ] Risk Rating assigned
- [ ] Fee Earner and Supervisor assigned

---

## Search and Filtering

### Common Search Criteria

**By Status:**
- Active matters
- Matters approaching limitation
- Matters awaiting trial
- Recently closed matters

**By Type:**
- All Inheritance Act claims
- All capacity challenges
- All executor misconduct cases

**By Value:**
- High-value estates (>£500k)
- Matter value bands

**By Risk:**
- High-risk matters
- Matters with limitation issues

**By Team:**
- All matters for specific fee earner
- All matters requiring supervisor review

---

## Reporting Capabilities

### Standard Reports

- **Active Caseload:** By fee earner, by matter type
- **Limitation Report:** Matters approaching deadlines
- **Financial Report:** WIP, value of matters
- **Risk Report:** High-risk matters requiring attention
- **Stage Report:** Matters at each stage
- **Source Analysis:** Where work is coming from

### Custom Reports

Metadata schema allows custom reporting on any combination of fields.

---

## Data Privacy and Security

### GDPR Considerations

- All metadata contains personal data
- Subject to data protection obligations
- Access restricted to authorized users
- Retention per firm policy
- Deletion upon matter closure and retention expiry

See [Data Protection and Privacy Considerations](data-protection-and-privacy-considerations.md)

---

## Integration

### Case Management System

All metadata fields should be:
- Fields in case management system
- Searchable and filterable
- Reportable
- Exportable

### Document Management System

Document-level metadata should sync with DMS.

---

## Related Resources

- [File Index Master](file-index-master.md)
- [File Naming Conventions](file-naming-conventions.md)
- [Data Protection and Privacy Considerations](data-protection-and-privacy-considerations.md)
- [Practical Administration and File Management](../../contentious-probate-manual/40-practical-administration-and-file-management.md)

## Navigation

- **Up:** [Templates Overview](../../contentious-probate-manual/50-templates-and-appendices-overview.md)

<!-- 
Template Maintenance Notes:
- Review metadata fields annually
- Add new fields as practice evolves
- Remove unused fields
- Ensure compliance with DMS and case management systems
-->
