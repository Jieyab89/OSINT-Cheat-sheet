# Key Elements of a Penetration Testing Report

A penetration testing report is the primary deliverable of a security assessment and serves as a formal record of the testing activities, findings, and recommendations. Beyond documenting technical vulnerabilities, the report should provide clear, structured, and actionable information that can be understood by both technical teams and management. A well-prepared report not only demonstrates the results of the assessment but also helps organizations prioritize remediation efforts, improve their security posture, and support compliance or audit requirements.

The following sections describe the key elements that should be included in a professional penetration testing report, along with their purpose and importance throughout the reporting process.

# Title

The report title is the first element readers will see and should clearly describe the purpose and scope of the document. A well-defined title helps distinguish the report from other technical documents while immediately communicating the type of security assessment that was performed. The title should be concise, professional, and consistent with the organization's reporting standards.

Common report titles include:

- **Penetration Testing Report**
- **Web Application Penetration Testing Report**
- **Mobile Application Penetration Testing Report**
- **API Security Assessment Report**
- **Network Penetration Testing Report**
- **Security Assessment Report**
- **Vulnerability Assessment Report**
- **Red Team Assessment Report**
- **Cloud Security Assessment Report**
- **Infrastructure Security Assessment Report**

When appropriate, the title may also include the project or organization name, assessment period, or report version. For example:

- **Penetration Testing Report – XYZ Web Portal**
- **API Security Assessment Report – Payment Gateway**
- **Mobile Application Penetration Testing Report v1.0**
- **Network Security Assessment Report – Internal Infrastructure**

Example 

```
Penetration Report 

Logo 

Author name 

Version

Date 
```

# Document Details 

| Document Title      | Penetration Report xxxx                          |
| ------------------- | ------------------------------------------------ |
| Report Date         | D-M-Y                                            |
| Classification      | Confidential                                     |
| Version             | 1.x / Final / Penetration Test / Regression Test |
| Author              | Name Author                                      |
| Author Contact      | Email xxxxx                                      |
| Recipient Name      | xxxxxx                                           |
| Recipient Contact   | Email xxxxx                                      |
| Scope / Features    | xxxxx                                            |
| Target              | xxxxx                                            |
| Pentest Methodology | Black, Grey, White Box                           |
| Environment         | UAT/PROD/INTRANET                                |
| Timeline            | D-M-Y - D-M-Y                                    |
| Penetration Test    | Finished / Completed / Not Completed             |
| Regression Testing  | Finished / Completed / Not Completed             |
# Table Of Content 

```
Document Details......................................................3
Version History Information......................................................	3
Recipient......................................................3
Penetration Testing Team Members......................................................	4
Contact......................................................4
```

# [Pentest / Assesment] Methodology 

# Assesment Checklist 

The penetration testing engagement was conducted using industry-recognized methodologies and security testing standards to ensure a systematic, comprehensive, and repeatable assessment process. The testing approach and methodology applied during the engagement depend on the type of application, assessment scope, and objectives defined at the beginning of the project. Depending on the assessment scope, one or more of the following methodologies may be applied.

# OWASP Web Security Testing Guide (WSTG) [Select one]

The **OWASP Web Security Testing Guide (WSTG)** is a comprehensive framework developed by the Open Worldwide Application Security Project (OWASP) for assessing the security of web applications. It provides structured testing procedures covering information gathering, configuration testing, authentication, authorization, session management, input validation, error handling, cryptography, business logic, client-side security, and other critical web application security controls. The WSTG is widely recognized as one of the primary methodologies for manual web application penetration testing.

# OWASP Mobile Application Security Testing Guide (MASTG) [Select one]

The **OWASP Mobile Application Security Testing Guide (MASTG)** is a standardized methodology for evaluating the security of Android and iOS mobile applications. It provides detailed guidance on testing mobile application architecture, secure data storage, cryptographic implementations, authentication mechanisms, network communication, platform interaction, reverse engineering resistance, code quality, and runtime protections. MASTG is commonly used during mobile application penetration testing and secure code reviews.

# OWASP API Security Top 10 [Select one]

The **OWASP API Security Top 10** is a security standard that identifies the most critical security risks affecting modern APIs, including REST, SOAP, GraphQL, and other web service implementations. It provides testing guidance for vulnerabilities such as Broken Object Level Authorization (BOLA), Broken Authentication, Excessive Data Exposure, Security Misconfiguration, Injection, Improper Asset Management, and Server-Side Request Forgery (SSRF). This methodology is commonly used when assessing API security.

# OWASP Application Security Verification Standard (ASVS) [Select one]

The **OWASP Application Security Verification Standard (ASVS)** is a framework for verifying the implementation of security controls within an application. Rather than focusing solely on vulnerabilities, ASVS defines measurable security requirements across authentication, access control, cryptography, session management, input validation, logging, error handling, and secure configuration. It is commonly used to validate application security maturity and support secure software development.

# Penetration Testing Execution Standard (PTES) [Select one]

The **Penetration Testing Execution Standard (PTES)** provides a complete framework for conducting penetration testing engagements from planning through reporting. The methodology covers pre-engagement interactions, intelligence gathering, threat modeling, vulnerability analysis, exploitation, post-exploitation, and reporting. PTES helps ensure that penetration testing activities are conducted in a structured and repeatable manner.

# NIST SP 800-115 [Select one]

**NIST Special Publication 800-115: Technical Guide to Information Security Testing and Assessment** provides guidance for planning, performing, and documenting technical security assessments. It describes recommended testing techniques, including vulnerability scanning, security configuration reviews, penetration testing, and security assessment methodologies based on industry best practices.

# Open Source Security Testing Methodology Manual (OSSTMM) [Select one]

The **Open Source Security Testing Methodology Manual (OSSTMM)** is an operational security testing framework that evaluates the security of networks, applications, wireless infrastructure, telecommunications, and physical security controls. OSSTMM emphasizes objective, measurable, and repeatable testing procedures to evaluate operational security effectiveness.

# MITRE ATT&CK Framework [Select one]

The **MITRE ATT&CK Framework** is a globally recognized knowledge base of adversary tactics, techniques, and procedures (TTPs). During penetration testing, ATT&CK can be used to map identified attack techniques to real-world adversary behaviors, helping organizations better understand potential attack paths and improve defensive capabilities.

# Common Vulnerability Scoring System (CVSS) [Select one]

The **Common Vulnerability Scoring System (CVSS)** is an industry-standard framework used to assess and communicate the severity of identified vulnerabilities. CVSS calculates a numerical score based on exploitability and impact metrics, enabling organizations to prioritize remediation efforts according to the level of risk posed by each finding.

# OWASP Risk Rating Methodology **[Select]**

The **OWASP Risk Rating Methodology** is a qualitative risk assessment framework developed by the Open Worldwide Application Security Project (OWASP). Unlike CVSS, which produces a standardized numerical score, the OWASP methodology evaluates the overall risk by considering multiple factors, including **Threat Agent Factors**, **Vulnerability Factors**, **Technical Impact Factors**, and **Business Impact Factors**. These factors are combined to estimate the likelihood and impact of a vulnerability, allowing organizations to prioritize remediation based on both technical severity and business risk. Findings are generally categorized into **Critical**, **High**, **Medium**, **Low**, or **Informational** according to the organization's defined risk matrix.

## Information Gathering

Information Gathering is the initial phase of the penetration testing process, aimed at collecting relevant information about the target environment. During this stage, publicly available information and accessible technical details are gathered to define the attack surface and identify potential entry points. Activities may include domain enumeration, DNS analysis, subdomain discovery, technology fingerprinting, network reconnaissance, service identification, and information collection from public sources. The information obtained during this phase forms the foundation for subsequent vulnerability assessment and exploitation activities.

## Vulnerability Assessment

Vulnerability Assessment is the process of identifying, analyzing, classifying, and prioritizing security weaknesses within the target environment. This phase involves the use of automated vulnerability scanners, manual verification, and security best practice reviews to detect known vulnerabilities, security misconfigurations, outdated software, and insecure configurations. Each identified vulnerability is assessed based on its potential impact and likelihood of exploitation to determine the overall risk to the organization.

## Penetration Testing

Penetration Testing is an authorized security assessment performed by simulating real-world cyberattacks against the target application, network, or system. The objective is to validate whether identified vulnerabilities can be successfully exploited and to assess their actual business impact. This phase combines automated tools with manual testing techniques to evaluate authentication mechanisms, authorization controls, business logic, input validation, session management, and other security controls that cannot be fully assessed through automated scanning alone.

## Exploitation & Custom Code Development

Following the identification of vulnerabilities, controlled exploitation is performed to verify the existence and impact of the identified security issues. The objective of this phase is to demonstrate the potential consequences of successful exploitation without causing disruption to the target environment. Activities may include privilege escalation, authentication bypass, sensitive data access, and proof-of-concept exploitation. Where necessary, custom scripts or proof-of-concept code are developed to automate reconnaissance, validate complex attack scenarios, or demonstrate vulnerabilities that cannot be verified using standard security tools.

## Black Box Testing [Select one]

Black Box Testing is a methodology in which the security assessor has no prior knowledge of the target application's internal architecture, source code, infrastructure, or credentials. Testing is conducted entirely from the perspective of an external attacker using only publicly available information. This approach simulates real-world attacks against publicly accessible systems and evaluates how effectively the organization's external security controls withstand unauthorized access attempts.

## Gray Box Testing [Select one]

Gray Box Testing is a methodology in which the security assessor is provided with limited knowledge or partial access to the target environment. This may include user credentials, application documentation, API specifications, or partial system architecture. The approach simulates an attacker with a legitimate user account or limited insider knowledge, allowing a more comprehensive assessment of authentication, authorization, business logic, and privilege management while maintaining a realistic attack scenario.

## White Box Testing [Select one]

White Box Testing is a methodology in which the security assessor is provided with complete knowledge of the target environment before testing begins. This may include source code, application architecture, infrastructure diagrams, configuration files, API documentation, database schemas, and privileged credentials. Having full visibility enables an in-depth security assessment through manual code review, configuration analysis, and advanced testing techniques to identify vulnerabilities that may not be discoverable through external testing alone.

## Crystal Box Testing [Select one]

Crystal Box Testing is an advanced assessment methodology that combines the advantages of White Box Testing with continuous collaboration between the security assessor and the development or engineering team. In addition to full access to source code, architecture, documentation, and privileged credentials, testers may communicate directly with developers to clarify application behavior, validate security controls, and discuss implementation details. This collaborative approach enables deeper security analysis, improves vulnerability validation, reduces false positives, and provides more effective remediation recommendations throughout the assessment process.

# Executive Summary

Contains information regarding a summary of the project results, the author’s name, the company or project name, the project timeline, and the report date, as well as the penetration testing or execution methods (e.g., black, gray, white). Summary of findings, such as a broken access control with an impact such as file theft, and a risk rating, such as high. Example 

```
This report presents the results of the penetration testing engagement conducted for **[Project / Company Name]**. The objective of this assessment was to evaluate the security posture of the target application by identifying vulnerabilities that could be exploited by unauthorized parties and assessing their potential impact on the organization's information assets.

The assessment was performed by **[Author Name]**. Testing activities were conducted from **[Start Date]** to **[End Date]**, and this report was issued on **[Report Date]**.

*Choose one of the penetration testing methods used—for example, using only blackbox*

**Black Box Assessment** [Select / Optional]

The assessment was conducted using a **Black Box** testing methodology, where no prior knowledge of the target application's internal architecture, source code, credentials, or system documentation was provided. Testing was performed from the perspective of an external attacker, simulating real-world attack scenarios to identify vulnerabilities that could be exploited without privileged access.

**Grey Box Assessment** [Select / Optional]

The assessment was conducted using a **Grey Box** testing methodology, where limited information and access were provided to the tester, such as user credentials, application documentation, or partial knowledge of the system architecture. This approach simulates an attacker with a certain level of authorized access and enables a more comprehensive evaluation of authentication, authorization, business logic, and privilege-related security controls.

**White Box Assessment** [Select / Optional]

The assessment was conducted using a **White Box** testing methodology, where complete knowledge of the target environment was provided, including source code, application architecture, configuration details, credentials, and supporting documentation. This approach enables an in-depth security review of the application by combining manual testing and code analysis to identify vulnerabilities that may not be discoverable through external testing alone.

**Crystal Box Assessment** **[Select / Optional]**

The assessment was conducted using a **Crystal Box** testing methodology, where complete knowledge of the target environment was provided along with active collaboration between the security assessor and the development or engineering team. This included access to source code, application architecture, configuration details, credentials, technical documentation, and direct communication with relevant stakeholders. By combining comprehensive system visibility with collaborative validation, this approach enables a deeper security assessment, more accurate vulnerability verification, reduced false positives, and practical remediation recommendations that align with the application's design and business requirements.

Throughout the assessment, multiple security vulnerabilities were identified with varying levels of severity. Each finding was evaluated based on its likelihood of exploitation and potential business impact. The results provide an overview of the current security posture and highlight areas requiring immediate remediation to reduce the organization's exposure to cyber threats.

The most significant vulnerability identified during this engagement is **[Vulnerability Name]**, which has been assigned a **[Critical / High / Medium / Low]** severity rating [CVSS OR OWASP CALC]. The vulnerability may allow an attacker to **[describe the primary impact, e.g., bypass authorization controls, access sensitive information, execute arbitrary commands, manipulate application data, or compromise user accounts]**, potentially affecting the confidentiality, integrity, and availability of the target application and its underlying information assets. Based on the assessment results, this finding represents the highest risk observed during the engagement and should be prioritized for remediation. It is strongly recommended that the identified vulnerability be addressed in accordance with its assigned risk level, with **Critical** and **High** severity findings requiring immediate remediation, followed by **Medium** and **Low** severity findings as part of the organization's regular vulnerability management and risk mitigation process.
```

# Finding Rating Levels

Bisa menggunakan CVSS atau owasp, misalnya disni menggunakan CVSS 

The severity of each finding identified during this assessment is determined using the **Common Vulnerability Scoring System (CVSS) v3.1**, an industry-recognized standard for evaluating the severity of security vulnerabilities. The assigned rating reflects the potential impact of a vulnerability on the confidentiality, integrity, and availability (CIA) of the affected system, as well as the likelihood of successful exploitation. The severity levels and their corresponding remediation priorities are summarized below.

| Severity          | CVSS v3.1 Score | Description                                                                                                                                                                                                 | Remediation Recommendation                                                                                                                                                                       |
| ----------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Critical**      | **9.0 – 10.0**  | Vulnerabilities that can be exploited with severe impact, potentially leading to complete system compromise, remote code execution, privilege escalation, or large-scale data exposure.                     | **Immediate remediation is required.** These vulnerabilities should be addressed as the highest priority before the application or system is deployed or remains in production.                  |
| **High**          | **7.0 – 8.9**   | Vulnerabilities that may allow unauthorized access, significant data disclosure, authentication bypass, or other attacks resulting in substantial security impact.                                          | **High-priority remediation is required.** Fix these vulnerabilities as soon as possible to minimize the risk of exploitation.                                                                   |
| **Medium**        | **4.0 – 6.9**   | Vulnerabilities with moderate security impact that generally require specific conditions or limited privileges to exploit but may still pose a meaningful security risk.                                    | **Remediation is recommended.** These issues should be resolved according to the organization's risk management and patching schedule.                                                           |
| **Low**           | **0.1 – 3.9**   | Vulnerabilities with limited security impact that are unlikely to result in significant compromise on their own but may contribute to attack chains when combined with other weaknesses.                    | **Remediation is recommended when practical.** Address these findings during routine maintenance or future development cycles.                                                                   |
| **Informational** | **0.0**         | Observations that do not represent exploitable vulnerabilities but identify security best practices, configuration improvements, or opportunities to strengthen the application's overall security posture. | **Remediation is optional.** Implementing these recommendations is encouraged to improve security maturity and reduce potential future risks, although no immediate security impact is expected. |
Source 
https://www.first.org/cvss/calculator/3.1

# Vulnerability Summary

The table below provides an overview of the vulnerabilities identified during the penetration testing engagement. It summarizes the number of findings by severity level, along with their current remediation status.

| No.       | Severity      | Total Findings | Open  | Closed |
| --------- | ------------- | -------------- | ----- | ------ |
| 1         | Critical      | 0              | 0     | 0      |
| 2         | High          | 0              | 0     | 0      |
| 3         | Medium        | 0              | 0     | 0      |
| 4         | Low           | 0              | 0     | 0      |
| 5         | Informational | 0              | 0     | 0      |
| **Total** | **Overall**   | **0**          | **0** | **0**  |
# Vulnerability Components and Findings Summary

The table below provides a summary of the affected components and the vulnerabilities identified during the penetration testing engagement, including their current remediation status and assigned severity level.

| No. | Vulnerability Name               | Status | Severity | Score CVSS |
| --- | -------------------------------- | ------ | -------- | ---------- |
| 1   | Broken Access Control            | Open   | High     | 8.0        |
| 2   | SQL Injection                    | Closed | Critical | 9.0        |
| 3   | Cross-Site Scripting (XSS)       | Open   | Medium   | 6.0        |
| 4   | Unrestricted File Upload         | Open   | High     | 8.0        |
| 5   | Sensitive Information Disclosure | Closed | Low      | 3.0        |
# Vulnerability Details and Description 

## Vulnerability Name 

**Severity** : Critical/High/Medium/Low/Informational

**Score**: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H

Example desc

```
A file download functionality was identified that allows users to retrieve a list of institutional bank account files. However, the application does not properly validate the supplied filename parameter before processing the request. An attacker can manipulate this parameter to reference arbitrary files or directories on the server. Because the application utilizes the `readfile()` function without sufficient input validation, supplying a directory path instead of a filename may result in directory listing, while supplying crafted path traversal sequences may allow arbitrary file disclosure. This vulnerability could expose sensitive files, application source code, configuration files, credentials, and other confidential information stored on the server.
```

**Status** : Closed/Open

**Summary table** 

| No  | Url               | Paramater | Method | Remarks                                                                                                            |
| --- | ----------------- | --------- | ------ | ------------------------------------------------------------------------------------------------------------------ |
| 1   | `/download?file=` | file      | GET    | Allows arbitrary file read and directory listing, potentially exposing sensitive information stored on the server. |
| 2   | XXXX              | XXX       | XX     | XXXXX                                                                                                              |
Here are the details on how to carry out the exploit to find xxxx

#### NO 1 
Proof of concept here............ also screenshoot 
#### NO 2
Proof of concept here............ also screenshoot 

**Impact** 
#### NO 1 
Impact here 
#### NO 2
Impact here 

**Recommendation** 
#### NO 1 
Recommendation here 
#### NO 2
Recommendation here 

**Reference** 

OWASP

[https://owasp.org/www-community/attacks/Path_Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

CWE 

LINK 

MITRE 

LINK 

**Regression Testing**

| No. | Retest Date | Status  | Remarks |
| :-: | :---------: | :-----: | ------- |
|  1  |    D-M-Y    | Pending | XXXX    |
|  2  |    D-M-Y    |  Pass   | XXX     |
|  3  |    D-M-Y    |  Fail   | XXXX    |
*Repeat if any other different finding* 

# Additional Information

The information contained in this report is **strictly confidential** and is intended solely for the authorized recipients designated by **[Company / Organization Name]**. This report contains sensitive technical information regarding the security posture of the assessed environment and must be handled in accordance with the organization's information security policies.

The contents of this report may not be copied, reproduced, distributed, disclosed, or used for any purpose other than the intended security remediation activities without the prior written authorization of **[Company / Organization Name]**. Any unauthorized disclosure, publication, or distribution of this document, whether in whole or in part, is strictly prohibited.

This penetration testing engagement was conducted with the authorization of the system owner and in accordance with the agreed scope, rules of engagement, and applicable laws and regulations. All testing activities were performed in a controlled manner with the objective of identifying security weaknesses while minimizing operational impact on the target environment.

The findings and recommendations presented in this report represent the security posture of the assessed systems at the time the assessment was performed. Because information systems continuously evolve through configuration changes, software updates, infrastructure modifications, and emerging threats, the results should not be interpreted as a guarantee that the assessed environment is free from vulnerabilities either now or in the future.

Although reasonable efforts were made to perform a comprehensive security assessment within the agreed timeframe, no penetration test can guarantee the identification of every security vulnerability. The absence of a reported finding should not be interpreted as evidence that a vulnerability does not exist. Additional vulnerabilities may remain undiscovered due to scope limitations, environmental constraints, newly disclosed vulnerabilities, or attack techniques that were outside the agreed assessment scope.

The testing team shall not be held liable for any direct, indirect, incidental, special, or consequential damages resulting from the use, interpretation, or implementation of the information contained in this report, except where such liability is required by applicable law. Responsibility for evaluating, prioritizing, and implementing the recommended remediation measures remains with the system owner and the responsible stakeholders.

This report should be treated as a confidential security document and retained only for legitimate business, compliance, audit, and remediation purposes. Appropriate administrative, technical, and physical safeguards should be implemented to protect this document from unauthorized access or disclosure.

# Document Approval and Signature

The issuance of this report confirms that the authorized parties listed below have reviewed the contents of the document and acknowledge that the information presented accurately reflects the results of the penetration testing engagement conducted within the agreed scope. By signing this document, the parties also acknowledge the confidentiality of the report and agree to its intended use in accordance with the applicable terms and conditions.

|Name|Position / Title|Organization|Signature|Date|
|---|---|---|---|---|
||||||
||||||
||||||

**Notes:**

- This document shall become effective upon approval by the authorized representatives.
- Electronic or digital signatures may be accepted where permitted by the organization's policies and applicable regulations.
- Any modification to this report after approval must be documented and re-approved by the relevant authorized parties.

# Read full here for detail also template docx

https://jieyab89-osint.gitbook.io/jieyab89-osint-cheat-sheet-wiki-tips/osint-tool-resouces-usage/all-about-reporting