# What is OPSEC (Operational security)?

OPSEC stands for Operational Security and is a term derived from the United States Military. Since its introduction, OPSEC has been adopted by many organizations and sectors to safeguard sensitive information in various contexts beyond the military. The objective of OPSEC is to prevent sensitive information from getting into the hands of an adversary, primarily by denying access to the data. First, we want to identify the data that can be compromised and then take steps to reduce the exploitation of this data and minimize the risk.

# How to Threat Model for OPSEC

OPSEC is not a static concept. Depending on the types of activities you are conducting, you will need to adapt your OPSEC measures. In order to evaluate your activities, their risk, and the necessary measures to be implemented, we need to conduct threat modelling. This allows us to determine the degree of security which we want to achieve. This threat modelling can be done in a fairly informal manner, merely by taking the time to write down the basic information pertaining to the following points:

- Know your target. A project investigating Threat Actors or organized crime groups, or malware and its developer, has a different level of OPSEC requirements from a project looking into the social media profile of a 16-year-old forum troll.
- Identify potential threats. Possible threats to sensitive data need to be identified and potentially documented. Consider that threats may exist externally through third parties, as well as internally. Data theft or breaches (either accidental or deliberate) can publish a wealth of data about you personally without your knowledge.
- Analyze security vulnerabilities. You must perform an objective analysis of your current security measure implementation strategy. Look for potential weaknesses which can be exploited. This covers all types of vulnerabilities, from cross-usage of devices to digital foot printing, usage of specific monitoring/tracking tools, etc.
- Determine the risk level of each vulnerability. Consider the damage that could be caused should your data be compromised, or if the organization may suffer as a result of your laxity.

It is recommended that, having gathered the information relating to the points, you speak to the relevant individuals who can help you with evaluating whether you belong to the group needing to implement Level 1 OPSEC measures, or Level 2. This may be the Chief Technical Officer (CTO) and/or Information Security Officer (ISO); all organizations are different but should have someone who is an authority and who can help guide your assessment.

# What is the OPSEC process?

OPSEC is an analytical process that entails assessing potential threats, vulnerabilities, and risks to sensitive information.

The five-step OPSEC process:

- Identify sensitive data - understand what your sensitive information might be.
- Threat Assessment - identify potential cybersecurity threats, i.e., think of what adversaries could exploit about you.
- Vulnerability analysis - identify where you are vulnerable and/or weaknesses in security.
- Risk assessment - measure the level of risk to do with each previously identified vulnerability.
- Apply countermeasures - develop countermeasures to minimize the identified risks.
- Everyone's OPSEC will look different depending on what they are doing, who they are, and what types of activities they are engaged in. You can ask yourself some questions to understand this in a better way and to identify your current threat model: What information do you want to protect? i.e., House address, work location, family members, and assets.

What can an adversary gain from looking at your online footprint? Who might want to gain access to that information? This can be in the form of people you don't know who are looking for a soft target online or in the form of you applying for a job and the recruiter finding you on social media to see what you post about to get an idea about your character.

Where do you expose yourself too much? Do you have privacy settings on all your social media? What do you post online? These questions may assist with making your assessment.

# Why is OPSEC important?

We all have something to keep from the general public, and if we didn't, we wouldn't password-protect our devices, lock our front doors, or sign out of our emails. Your online footprint says a lot about you, some of what you might not want to be accessible to just about anyone.

# Why is OPSEC important to OSINT investigators?

OSINT investigators are required to have good OPSEC. This means they should avoid using their personal social media accounts to conduct investigations. The reason for this is to uphold their privacy and security and ensure the investigation's integrity. Research accounts are created to isolate OSINT research, ensuring a separation between the personal and work lives of OSINT investigators. It is essential to emphasize the importance of separating an OSINT investigator's real identity from research accounts.

Read more about Sock Puppets here:https://www.sans.org/blog/what-are-sock-puppets-in-osint.

Those conducting OSINT investigations can make OPSEC mistakes, including:

- Network attribution (visiting the target's website without altering their footprint)
- Using personal accounts and devices for OSINT investigation research
- Accidentally interacting with a target (liking, commenting, friending them on social profiles)
- Those of you who are not conducting OSINT research can also make OPSEC mistakes, including the general oversharing of personal information online, and one example of poor OPSEC is leaving unused social media profiles online (especially when they contain old photos and other information you have posted in the past). The general rule to understand is that we might make mistakes, and the objective should always be to reduce the impact of these mistakes.

# Best Practices for Good OPSEC

### Basics for everyone:

- Use strong and unique passwords. Do not create passwords based on your pet's name, kids, spouse, etc.
- Use a password manager or use a password notebook
- Turn on two-factor authentication on your email/social accounts.
- Install the latest software & app updates to all your devices
- Activate screen-lock when idle
- Don't leave your device unattended
- Use webcam covers and privacy filters
- Use encrypted email services such as Proton Mail
- Use encrypted cloud storage like Proton Drive
- Adjust privacy settings on social media platforms
- Use a secure search engine like search.brave.com or startpage.com
- If you use public Wifi at coffee shops, hotels, or airports, use a Virtual Private Network (VPN)
- Check the permissions apps ask for before downloading
- Educate yourself and your family/friends about online privacy and security

### Additional tips for the OSINT investigator:

- Avoid using your personal devices and social media profiles to conduct OSINT Investigations. Use sock puppets (research accounts).
- Use dedicated devices and accounts for investigations to avoid cross-contamination and compromising an investigation.
- Use a paid Virtual Private Network (VPN) to mask your IP address. Website owners can view who and what IPS visit their site. Expect that a target is looking at who views their personal website. This does not apply to social media research, as only the social media company would see the IP address.
- Use a Virtual Machine (VM) to sandbox your OSINT research, and make sure a VM is used as an operating system with your computer's operating system. If you click on malware, your device will not be impacted.
- Think of your device fingerprint (network computer's IP address when visiting a target's website). You want to make attribution to you difficult. This means taking steps to mask our personal identifiable information (PII).
- Consider the time/days you conduct research (9-5?) - adjust settings to match the target's time zone.
- Vet the OSINT open-source tools you use.
- Have Standard Operating Procedures (SOPs) about how you will conduct online research.
- Avoid posting your security clearance on social media.
- It is important to note that OPSEC is an ongoing process that requires continuous evaluation, adaptation, and improvement to address evolving threats and vulnerabilities. For instance, you may move into a job where you need to reassess your threat model. This is why it's crucial to think about this often and reassess as necessary. It is not a one-time activity but rather a mindset and a set of practices that should be integrated into daily operations.

- ### Reference

- [SANS.org OPSEC](https://www.sans.org/blog/what-is-opsec/)
- [Maltego](https://www.maltego.com/blog/everything-you-need-to-know-about-operational-security-opsec/)
- [Skopenow](https://www.skopenow.com/resource-center/opsec-tradecraft-for-osint)
