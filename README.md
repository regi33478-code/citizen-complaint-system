# Citizen Complaint System

A simple Python program that lets citizens file complaints about public services (water, roads, electricity, sanitation) and lets an office track and update them. Built with Object-Oriented Programming for PROG211 Object-Oriented Programming 1, Limkokwing University of Creative Technology, Sierra Leone.

**Author:** Reginald Obededom Alex Michael Johnson | **Student ID:** 905006460

## The problem it solves

Citizens often have no simple, trackable way to report problems with public services. This program records each complaint with a category, a description and a status (Open or Resolved), so an office can see what has been reported and what has been dealt with.

## Features

- Two classes: `Complaint` and `Citizen`
- One list stores many `Complaint` objects, with functions to add and display records
- A tuple, `VALID_CATEGORIES`, stores the approved complaint categories
- Instance methods: `display_info()`, `update_status()`, `file_complaint()`
- Class methods: `get_office_name()` and `get_total_complaints()`
- Static method: `is_valid_category()` checks a category without needing an object

## How to run

1. Install Python 3 from python.org.
2. Download `main.py`.
3. Run: `python main.py`

No extra libraries are needed.

## How this solution meets Digital Public Goods (DPG) standards

**1. Open-source.** The full source code is published in this public GitHub repository, so anyone can read, use and improve it. It uses only standard Python, with no paid software.

**2. Inclusive and accessible.** It runs on any computer with Python, works offline, needs no login and no special hardware. The output is plain text in simple English. Because the code is open, it can be translated into local languages such as Krio.

**3. Privacy-respecting.** The program stores no sensitive personal data. Citizens are identified only by anonymous IDs (for example `CIT-001`) and a district. There are no names, phone numbers or addresses. Complaint descriptions should describe the problem only, without personal details.

**4. Modular and reusable.** Each part has one job. `Complaint` handles complaint data, `Citizen` handles filing, and separate functions handle the list. The same design can be reused for other services, such as permits or service requests, by changing the categories and attributes.

## Example usage

Input (the data in the main program of the code):

```python
citizen1 = Citizen("CIT-001", "Western Area")
add_complaint(complaints, citizen1.file_complaint("CMP-001", "Water", "No running water for three days."))
complaints[0].update_status("Resolved")
print(Complaint.is_valid_category("Football"))
```

Output:

```
---- Filing complaints ----
CIT-001 from Western Area filed CMP-001.
Added CMP-001. Total in list: 1
CIT-001 from Western Area filed CMP-002.
Added CMP-002. Total in list: 2
CIT-002 from Bo filed CMP-003.
Added CMP-003. Total in list: 3

---- All complaints ----

---- Complaint 1 ----
Complaint ID: CMP-001
Category: Water
Description: No running water for three days.
Status: Open
Office: Citizen Complaints Office

---- Complaint 2 ----
Complaint ID: CMP-002
Category: Roads
Description: Large pothole on the main road.
Status: Open
Office: Citizen Complaints Office

---- Complaint 3 ----
Complaint ID: CMP-003
Category: Electricity
Description: Street lights not working.
Status: Open
Office: Citizen Complaints Office

---- Updating a complaint ----
Status updated for CMP-001: Resolved

---- Class method results ----
Citizen Complaints Office
Total complaints: 3

---- Static method check ----
True
False
```

## Project files

- `main.py` - the source code
- `README.md` - this file
