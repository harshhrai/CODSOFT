import tkinter as tk
from tkinter import messagebox

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        
        self.contacts = []
        
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()
        
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()
        
        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(root)
        self.address_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()
        
        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.pack()
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        
        self.clear_entries()
    
    def view_contacts(self):
        contacts_list = "\n".join([f"Name: {c['name']} | Phone: {c['phone']}" for c in self.contacts])
        messagebox.showinfo("Contacts", contacts_list)
        
    def search_contact(self):
        search_term = self.search_entry.get().lower()
        results = []
        for contact in self.contacts:
            if search_term in contact["name"].lower() or search_term in contact["phone"]:
                results.append(f"Name: {contact['name']} | Phone: {contact['phone']}")

        if results:
            result_str = "\n".join(results)
            messagebox.showinfo("Search Results", result_str)
        else:
            messagebox.showinfo("Search Results", "No contacts found.")
    
    def update_contact(self):
        # Implementation for updating a contact
        pass
    
    def delete_contact(self):
        # Implementation for deleting a contact
        pass
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
