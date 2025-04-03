import frappe

def execute():
    # Get all vehicle records
	vehicles = frappe.db.get_all("Vehicle", pluck="name")

	# Loop through each vehicle record
	for vehicle in vehicles:
		# Update the title field with the vehicle name
		vehicle = frappe.get_doc("Vehicle", vehicle)
		vehicle.set_title()
		vehicle.save()


	# Commit the changes to the database
	frappe.db.commit()
