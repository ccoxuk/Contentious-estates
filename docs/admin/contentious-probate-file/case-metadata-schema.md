---
title: "Case Metadata Schema - Contentious Probate"
author: ""
date: ""
version: "1.0.0"
status: "Administrative Guide"
category: "Administration"
tags: ["contentious-probate", "metadata", "case-management", "data-schema"]
description: "Standard metadata schema for contentious probate case management systems"
---

# Case Metadata Schema - Contentious Probate

<!-- 
  Purpose: Define standard metadata fields for contentious probate matters in case management systems.
  Usage: Apply when opening matters and update throughout case lifecycle.
  Benefits: Consistent data capture, reporting capability, efficient case management, compliance support.
-->

---

## Overview

Metadata provides structured information about cases that enables efficient management, reporting, and retrieval. This schema defines the standard metadata fields for contentious probate matters.

---

## Core Matter Fields

### Matter Identification

**Matter Reference** (Required)
- Format: [Office code]-[Year]-[Sequential number]
- Example: LON-2025-00123
- Unique identifier for matter
- Used in all documents and correspondence

**Matter Description** (Required)
- Format: "Estate of [Deceased name] - [Claim type]"
- Example: "Estate of John Smith - Capacity Challenge"
- Concise case description
- For internal identification

**Matter Type** (Required)
- Category: Contentious Probate
- Sub-category: [Select from list below]

**Matter Sub-Type Options:**
- Lack of Testamentary Capacity
- Want of Knowledge and Approval
- Undue Influence
- Fraud/Forgery
- Want of Due Execution
- Inheritance Act 1975 Claim
- Proprietary Estoppel
- Constructive Trust
- Executor/Administrator Dispute
- Professional Negligence (Will drafting)
- Mixed/Multiple Claims
- Other

---

### Key Dates

**Date Opened** (Required)
- Date matter opened in system
- Format: DD/MM/YYYY
- Auto-populated on matter creation

**Date of Death** (Required)
- Deceased's date of death
- Format: DD/MM/YYYY
- Critical for limitation calculations

**Date of Grant** (If applicable)
- Date grant of probate/administration issued
- Format: DD/MM/YYYY
- Essential for Inheritance Act claims (6-month deadline)

**Date Instructions Received** (Required)
- When client first instructed firm
- Format: DD/MM/YYYY
- Relevant for delay assessment

**Limitation Deadline** (If applicable)
- Key limitation expiry date
- Format: DD/MM/YYYY
- Triggers reminder system

**Date Closed** (When closed)
- Matter closure date
- Format: DD/MM/YYYY
- Determines retention period start

---

## Client Information

### Primary Client

**Client Name** (Required)
- Full legal name
- Format: Surname, Forename(s)
- Example: Smith, John David

**Client Type** (Required)
- Individual
- Company
- Trust
- Other entity

**Client Reference** (Required if existing client)
- Unique client identifier in system
- Links to client master record

**Client Role** (Required)
- Claimant
- Defendant
- Interested Party
- Other

---

### Client Contact Details

**Address** (Required)
- Full postal address
- Separate fields for address lines, postcode

**Email** (Preferred contact)
- Primary email address

**Mobile Telephone**
- Mobile number

**Home Telephone**
- Home number

**Preferred Contact Method** (Required)
- Email / Telephone / Post / Video call

---

## The Deceased

### Deceased Information

**Deceased Name** (Required)
- Full legal name
- Format: Surname, Forename(s)

**Date of Birth**
- Deceased's DOB
- Format: DD/MM/YYYY

**Date of Death** (Required)
- As per death certificate
- Format: DD/MM/YYYY

**Last Address**
- Deceased's last known address
- Postcode required

**Domicile** (Required)
- England and Wales / Scotland / Northern Ireland / Other
- Impacts jurisdiction

---

## Estate Information

**Approximate Estate Value** (Required)
- Estimated gross value
- Currency: GBP
- Brackets: <£100k / £100k-£250k / £250k-£500k / £500k-£1m / >£1m

**Net Estate Value** (If known)
- After liabilities
- Currency: GBP

**Main Assets**
- Tick boxes:
  - [ ] Real property
  - [ ] Bank accounts/savings
  - [ ] Investments/shares
  - [ ] Business interests
  - [ ] Personal property
  - [ ] Other

---

## Grant Information

**Grant Status** (Required)
- Not yet applied for
- Application pending
- Granted
- Disputed/caveat entered

**Grant Type** (If granted)
- Grant of Probate
- Letters of Administration (with will)
- Letters of Administration (intestacy)

**Grant Date**
- Format: DD/MM/YYYY

**Probate Registry**
- Name of registry

**Executor(s)/Administrator(s)**
- Name(s) of appointed person(s)

---

## Testamentary Documents

**Current Will Date** (If exists)
- Date of will in question
- Format: DD/MM/YYYY

**Previous Will Date(s)** (If relevant)
- Date(s) of earlier will(s)
- Format: DD/MM/YYYY

**Will Drafter**
- Solicitor/firm who prepared will
- Relevant for will file requests

---

## Claim Details

**Claim Type** (Required - select all that apply)
- [ ] Validity challenge (capacity)
- [ ] Validity challenge (knowledge/approval)
- [ ] Validity challenge (undue influence)
- [ ] Validity challenge (fraud/forgery/execution)
- [ ] Inheritance Act 1975
- [ ] Proprietary estoppel
- [ ] Constructive trust
- [ ] Executor/administrator claim
- [ ] Professional negligence
- [ ] Other

**Client's Standing** (Required)
- Beneficiary under current will
- Beneficiary under previous will
- Would benefit on intestacy
- Spouse/civil partner (Inheritance Act)
- Child (Inheritance Act)
- Dependant (Inheritance Act)
- Person with assurance (estoppel)
- Beneficiary/interested party (executor dispute)
- Other

---

## Parties

### Opponent(s)

**Primary Opponent Name** (Required)
- Full name

**Opponent Role**
- Executor
- Administrator
- Beneficiary
- Other party

**Opponent Solicitor** (If known)
- Firm name
- Solicitor name
- Contact details

**Additional Opponents**
- Provision for multiple opponents
- Name and role for each

---

## Case Status

**Current Stage** (Required - select one)
- Initial instruction / Pre-action
- Pre-action correspondence
- Proceedings issued
- Pleadings (pre-CMC)
- Disclosure / Evidence
- Trial preparation
- Trial / Hearing
- Post-judgment
- Settlement discussions
- Mediation
- Closed - Settled
- Closed - Trial/judgment
- Closed - Discontinued
- Closed - Other

**Proceedings Status** (If issued)
- Not yet issued
- Issued - pre-service
- Issued - served
- Defence stage
- Statements of case complete
- Directions given
- Trial listed

**Court Details** (If issued)
- High Court - Chancery Division
- County Court - [location]
- Other

**Claim Number** (If issued)
- Court-assigned claim number

---

## Fee Earners

**Partner Responsible** (Required)
- Name and ID of supervising partner

**Fee Earner** (Required)
- Name and ID of main fee earner

**Other Fee Earners**
- Names of other solicitors working on matter

**Trainee/Paralegal**
- Support staff assigned

---

## Counsel

**Lead Counsel** (If instructed)
- Name and chambers

**Junior Counsel** (If instructed)
- Name and chambers

---

## Financial

### Costs and Billing

**Fee Arrangement** (Required)
- Private client (hourly rates)
- Conditional Fee Agreement (CFA)
- Damages-Based Agreement (DBA)
- Legal Aid
- Insurance-funded
- Other

**Estimated Costs Range** (Required)
- Low estimate: £
- High estimate: £

**Costs Budget** (If required)
- Precedent H filed: Yes/No
- Budgeted costs: £

**Billing Frequency**
- Monthly
- Quarterly
- On completion
- Other

---

### Work in Progress

**Time Recorded** (Auto-calculated)
- Total time recorded to date
- Hours and value

**Costs Incurred** (Auto-calculated)
- Total costs incurred
- Fees + Disbursements

**Billed to Date** (Auto-calculated)
- Total bills delivered
- Amount billed

---

## Risk and Compliance

**Overall Risk Rating** (Required)
- Low
- Medium
- High

**Risk Factors** (Select all that apply)
- [ ] Limitation risk
- [ ] Conflict of interest
- [ ] Client capacity concerns
- [ ] Vulnerable client
- [ ] High costs relative to estate value
- [ ] Adverse publicity risk
- [ ] Regulatory/SRA concern
- [ ] Insurance notification required
- [ ] High value (>£500k)
- [ ] Reputational risk
- [ ] Other

**AML Risk Rating** (Required)
- Low
- Medium
- High

**Conflicts** (Required)
- None identified
- Potential conflict - managed
- Information barrier in place
- Cannot act - referred

---

## Limitation and Deadlines

**Limitation Status** (Required)
- Within limitation - no concern
- Within limitation - approaching expiry
- Outside primary limitation
- Permission required for late claim
- No strict limitation (laches applies)

**Key Deadline 1**
- Description: [e.g., "Inheritance Act 6-month deadline"]
- Date: DD/MM/YYYY

**Key Deadline 2**
- Description:
- Date: DD/MM/YYYY

**Additional Deadlines**
- Provision for multiple deadline entries

---

## Documents

**Key Documents Status**

**Death Certificate**
- [ ] Received
- [ ] Requested
- [ ] Not yet requested

**Will (current)**
- [ ] Copy received
- [ ] Original received
- [ ] Requested
- [ ] Not available

**Previous Will(s)**
- [ ] Received
- [ ] Requested
- [ ] Not available

**Grant**
- [ ] Received
- [ ] Not yet obtained
- [ ] N/A

**Medical Records**
- [ ] Received (complete)
- [ ] Received (partial)
- [ ] Requested
- [ ] Not yet requested
- [ ] N/A

**Solicitor's Will File**
- [ ] Received
- [ ] Requested
- [ ] Refused
- [ ] Not yet requested
- [ ] N/A

---

## Case Management

**Next Action** (Required)
- Description of next step
- Free text field

**Next Action Date** (Required)
- Target date for next action
- Format: DD/MM/YYYY
- Triggers reminders

**Last Review Date**
- Date of last file review
- Format: DD/MM/YYYY

**Next Review Date**
- Date of next scheduled review
- Format: DD/MM/YYYY

**Supervisor Review Status**
- Last reviewed: DD/MM/YYYY
- Next review: DD/MM/YYYY
- Issues flagged: Yes/No

---

## Alternative Dispute Resolution

**ADR Status**
- Not yet considered
- Proposed by us
- Proposed by opponent
- Rejected
- In discussion
- Mediation scheduled
- Mediation completed
- Settlement reached
- N/A

**Mediation Details** (If applicable)
- Mediator name:
- Mediation date:
- Outcome:

---

## Settlement

**Settlement Status**
- Not in negotiation
- Discussions ongoing
- Terms agreed subject to approval
- Settlement concluded
- Not appropriate

**Part 36 Offers**
- We made offer: Date and amount
- They made offer: Date and amount

---

## Outcome

**Case Outcome** (On closure)
- Settled - client terms
- Settled - compromise
- Judgment - client success
- Judgment - opponent success
- Judgment - mixed outcome
- Discontinued
- Struck out
- Other

**Financial Outcome**
- Amount recovered/obtained: £
- Costs recovered: £
- Costs paid to opponent: £

---

## Free Text Fields

**Special Instructions**
- Client-specific requirements
- Handling instructions

**File Notes/Comments**
- General notes about matter
- Running commentary on developments

**Settlement Authority**
- Client's settlement parameters
- Confidential field

---

## System Integration

### Auto-Population

Fields that auto-populate:
- Matter reference (sequential)
- Date opened (system date)
- Financial calculations (from time/billing)

### Mandatory Fields

System should require completion of "Required" fields before matter can be saved/progressed.

### Dropdown Lists

Provide dropdown options for:
- Matter sub-type
- Client role
- Grant status
- Current stage
- Fee arrangement
- Risk ratings

### Validation Rules

- Dates in valid format
- Matter reference unique
- Email in valid format
- Monetary fields numeric

---

## Reporting

### Standard Reports

Metadata enables:
- Matter list by type/stage/fee earner
- Financial reports (WIP, billed, outstanding)
- Deadline reports (approaching deadlines)
- Risk reports (high-risk matters)
- Workload reports (matters per fee earner)

---

## Data Protection

**GDPR Compliance**
- All personal data processed lawfully
- Retention periods applied
- Access controls in place
- Data minimization principle applied
- Subject access request process established

**Sensitive Data**
- Medical information handled appropriately
- Extra security for high-profile clients
- Confidentiality maintained

---

## Maintenance

**Data Quality**
- Regular audits of data accuracy
- Update metadata as case progresses
- Correct errors promptly
- Standardize data entry

**Review**
- Annual review of schema
- Update based on feedback
- Add new fields as needed
- Archive obsolete fields

---

## Training

**User Training**
- Train all users on metadata entry
- Emphasize importance of accuracy
- Provide examples and guidance
- Regular refresher sessions

---

**Version:** 1.0.0  
**Last Updated:** [Date]
