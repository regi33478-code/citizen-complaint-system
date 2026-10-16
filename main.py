# Citizen Complaint System
# A simple OOP program where citizens file complaints and an office tracks them.


class Complaint:
    """Represents one complaint filed by a citizen."""

    # Class attributes: shared by every Complaint object
    office_name = "Citizen Complaints Office"
    total_complaints = 0  # counts how many complaints have been created
    VALID_CATEGORIES = ("Water", "Roads", "Electricity", "Sanitation")  # tuple of approved categories

    def __init__(self, complaint_id, category, description):
        """Create a complaint after checking that its category is valid."""
        # Stop with an error if the category is not in the approved tuple
        if not Complaint.is_valid_category(category):
            raise ValueError(f"Invalid category: {category}")
        # Instance attributes: different for each complaint
        self.complaint_id = complaint_id
        self.category = category
        self.description = description
        self.status = "Open"  # every new complaint starts as Open
        Complaint.total_complaints += 1  # add one to the shared counter

    def display_info(self):
        """Instance method: print the details of this complaint."""
        print(f"Complaint ID: {self.complaint_id}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Office: {Complaint.office_name}")

    def update_status(self, new_status):
        """Instance method: change the status of this complaint."""
        self.status = new_status
        print(f"Status updated for {self.complaint_id}: {self.status}")

    @classmethod
    def get_office_name(cls):
        """Class method: return the office name shared by all complaints."""
        return cls.office_name

    @classmethod
    def get_total_complaints(cls):
        """Class method: return how many complaints have been created."""
        return cls.total_complaints

    @staticmethod
    def is_valid_category(category):
        """Static method: return True if the category is approved, else False.
        It does not use self or cls, so it works as a simple helper."""
        return category in Complaint.VALID_CATEGORIES


class Citizen:
    """Represents a citizen who can file complaints."""

    def __init__(self, citizen_id, district):
        # Only an ID and a district are stored, so no sensitive personal data is kept
        self.citizen_id = citizen_id
        self.district = district

    def file_complaint(self, complaint_id, category, description):
        """Instance method: create a Complaint object for this citizen."""
        complaint = Complaint(complaint_id, category, description)
        print(f"{self.citizen_id} from {self.district} filed {complaint_id}.")
        return complaint  # give the new complaint back to the caller


def add_complaint(complaint_list, complaint):
    """Add a complaint to the list and show the new total."""
    complaint_list.append(complaint)
    print(f"Added {complaint.complaint_id}. Total in list: {len(complaint_list)}")


def display_all(complaint_list):
    """Loop through the list and display every complaint."""
    # If the list is empty, say so and stop
    if len(complaint_list) == 0:
        print("No complaints registered yet.")
        return
    # enumerate numbers the complaints starting from 1
    for number, complaint in enumerate(complaint_list, 1):
        print(f"\n---- Complaint {number} ----")
        complaint.display_info()


# ---------- Main program ----------

# Create two Citizen objects
citizen1 = Citizen("CIT-001", "Western Area")
citizen2 = Citizen("CIT-002", "Bo")

# The list (data structure) that stores all Complaint objects
complaints = []

# Citizens file complaints and each one is added to the list
print("---- Filing complaints ----")
add_complaint(complaints, citizen1.file_complaint("CMP-001", "Water", "No running water for three days."))
add_complaint(complaints, citizen1.file_complaint("CMP-002", "Roads", "Large pothole on the main road."))
add_complaint(complaints, citizen2.file_complaint("CMP-003", "Electricity", "Street lights not working."))

# Show every complaint in the list
print("\n---- All complaints ----")
display_all(complaints)

# Update the status of the first complaint
print("\n---- Updating a complaint ----")
complaints[0].update_status("Resolved")

# Call the class methods (no object needed)
print("\n---- Class method results ----")
print(Complaint.get_office_name())
print(f"Total complaints: {Complaint.get_total_complaints()}")

# Call the static method: True for a valid category, False for an invalid one
print("\n---- Static method check ----")
print(Complaint.is_valid_category("Water"))     # True
print(Complaint.is_valid_category("Football"))  # False