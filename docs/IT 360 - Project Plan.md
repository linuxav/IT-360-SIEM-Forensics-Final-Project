# ThreatFlare

Tyler Werner, Alex Valentine

Overview  
FireWatch sorts and formats relevant firewall log data to find IP addresses. The clean data is sent to an AI agent that uses APIs from threat tracker websites to gather relevant threat information. The AI summarizes the information in a simple readable format for the user.

Objectives:

- Search system log files for IP addresses
- Send IP addresses to database API to compare against known malicious IP’s
- Output list of safe and malicious IP addresses

- AI can either be used for searching log files for IP addresses or to explain risks with malicious sites. To be determined based on available information

Success Criteria: Report relevant security info on all real threats found in the list of IP addresses.

Start and end dates: **start 8/18/2026 end 12/11/2026**

Stakeholders  
 \- Sponsor designation: **Instructor**  
 \- Stakeholders:

- Alex Valentine \- \[Role TBD\]
- Tyler Werner \- \[Role TBD\]

  Scope Management  
  \- In-scope items: Search log files, identify IP addresses, send to APIs, format and summarize data with AI.  
  \- Out-of-scope items: Threat remediation, GUI,  
  \- Project assumptions and constraints:

Assumptions: Linux Operating system with internet connection. Access to AI agent and threat database APIs.

Constraints: log contents, AI reliability, firewall compatibility, unknown threats may not be cataloged in threat databases.

Timeline  
 Tentative Schedule \- Subject to Change

- 8/27: Submit plan
- 9/3: Presentation proposal
- 11/27: Code completed
- 12/4: Video Presentation and written report Completed
- 12/11: Project Due

  Risk Management  
   \- Identified risks with impact/probability assessments: False negative(high, moderate), AI inaccuracies(medium, TBD based on model), AI data security(high, TBD based on model)

  Resources  
   \- Required tools and technology: Linux VM with internet access, AI model, Threat database API  
   \- Project dependencies: python, TBD

  Communication  
   \- Meeting cadence and reporting frequency  
  Wednesdays 2pm  
   \- Communication channels  
  Microsoft Teams & Discord(Backup)

  Action Items  
   \- Actionable tasks with owners, due dates, and GSD sync capability (items can be pushed to the main GSD inbox for tracking)

- Setup test environment
- Research project requirements
- Setup log files(linux Firewall)
- Write script to grab IP addresses from log files
- Extend script to send IP addresses to Threat database API
- Extend script to send discovered threats to AI for explanation
- Setup AI agent to summarize/explain data
- Written report
- Video Presentation
- **DATES TBD**
