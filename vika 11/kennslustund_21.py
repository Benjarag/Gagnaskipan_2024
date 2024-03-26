
from sortedcontainers import SortedDict


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactList:
    def __init__(self):
        '''
        ● Use a dict for the main map, which is keyed on a numeric id and has instances of
          Contact as data.
        ● Use a SortedDict (from sortedcontainers) for a map that will be keyed on name and has
          the unique id as data.
            ○ name_map = SortedDict()
        ● Use a dict for a map that will be keyed on phone and has the unique id as data.
        ● Use a dict for a map that will be keyed on email and has the unique id as data.

        '''
        self.contact_map = {}
        self.name_map = SortedDict() 
        self.phone_map = {}
        self.email_map = {}
        
    def add_contact(self, name, phone, email):
        '''
        ● Here you could also take a Contact class as a parameter if it works better for you.
        ● Generate a unique id (use a counter, starting in 1 and always incrementing by 1 after a
          new contact is inserted).
        ● Insert the id as a key and a new Contact as the data into the main map.
            ○ contact_map[unique_id] = Contact(name, phone, email)
        ● Insert the name as a key and the unique id as data into the name map
            ○ name_map[name] = unique_id
        ● Insert the name as a key and the unique id as data into the name map
            ○ phone_map[phone] = unique_id
        ● Insert the name as a key and the unique id as data into the name map
            ○ email_map[email] = unique_id
        ● These key maps can be called indexes on the data.

        '''
        unique_id = len(self.contact_map) + 1
        self.contact_map[unique_id] = Contact(name, phone, email)
        self.name_map[name] = unique_id
        self.phone_map[phone] = unique_id
        self.email_map[email] = unique_id

    def get_by_name(self, name):
        '''
            ● This operation returns the contact instance with this name
            ● First get the unique_id from the name map.
                ○ id = name_map[name]
            ● Then get the contact itself from the main map.
                ○ return contact_map[id]
            ● What happens if more than one contact has the exact same name?
                ○ Can the SortedDict store small containers of all ids with that name?
        '''
        try:
            id = self.name_map[name]
            return self.contact_map[id]
        except KeyError:
            return "ID not found"


    def get_by_phone(self, phone):
        '''
        gets id from phone map instead
        '''
        try:
            id = self.phone_map[phone]
            return self.contact_map[id]
        except KeyError:
            return "ID not found"

    def get_by_email(self, email):
        '''
        gets id from email map instead
        '''
        try:
            id = self.email_map[email]
            return self.contact_map[id]
        except KeyError:
            return "ID not found"

    def get_by_id(self, id):
        '''
        - returns directly from the main map
        You also have to think about how the unique_id is allowed to flow through the program. Is it
        also in the Contact class but just not shown on the screen. This particular unique_id is really
        not of any importance to the end user, but it needs to be linked to the data, so that when
        something is selected from a list, the unique id is accessible to call operations, such as
        remove(id)
        '''
        try:
            return self.contact_map[id]
        except KeyError:
            return "ID not found"

    def remove(self, id):
        '''
        ● Here you need to make sure the information about this contact is removed from all data
          structures.
        ● Get the Contact instance for this id
            ○ contact = main_map[id]
        ● Remove by different keys from different maps
            ○ del name_map[contact.name]
            ○ del phone_map[contact.phone]
            ○ del email_map[contact.email]
            ○ del main_map[id]
        ● May need more code if allowing multiple items with same name, phone or email
        '''
        try:
            contact = self.contact_map[id]
            del self.name_map[contact.name]
            del self.phone_map[contact.phone]
            del self.email_map[contact.email]
            del self.contact_map[id]
        except KeyError:
            return "ID not found"

    def get_contacts_ordered_by_name(self):
        '''
        ● Here you have to pull each contact out of the main map, but in the order in which the
          name_map is stored.
                ■ ordered_contact_list = []
                  for name in name_map:
                  
                  ordered_contact_list.append(main_map[name_map[name]])
        
        ● Again, the code might be a bit more if you allow multiple contacts with same name.
        ● Also, try using irange() to get a partial list.
            ○ name_list = name_map.irange(“ga”, “hzzz”)
              ordered_contact_list = []
              for name in name_list:
                ordered_contact_list.append(main_map[name_map[name]])

        '''
        ordered_contact_list = []
        for name in self.name_map:
            ordered_contact_list.append(self.contact_map[self.name_map[name]])
        return ordered_contact_list

# tests
if __name__ == "__main__":
    cl = ContactList()
    print("Adding contacts\n")
    cl.add_contact("Gandalf", "555-1212", "gandalf@example.com")
    cl.add_contact("Frodo", "555-1313", "frodo@example.com")
    cl.add_contact("Sam", "555-1414", "sam@example.com")
    cl.add_contact("Aragorn", "555-1515", "aragorn@example.com")
    cl.add_contact("Legolas", "555-1616", "legolas@example.com")
    cl.add_contact("Gimli", "555-1717", "gimli@example.com")
    cl.add_contact("Boromir", "555-1818", "boromir@example.com")
    cl.add_contact("Gollum", "555-1919", "gollum@example.com")

    print("\nGetting by name\n")
    print(cl.get_by_name("Gandalf").phone)
    print(cl.get_by_name("Frodo").phone)
    print(cl.get_by_name("Sam").phone)
    print(cl.get_by_name("Aragorn").phone)
    print(cl.get_by_name("Legolas").phone)
    print(cl.get_by_name("Gimli").phone)
    print(cl.get_by_name("Boromir").phone)
    print(cl.get_by_name("Gollum").phone)
    
    print("\nGetting by phone\n")
    print(cl.get_by_phone("555-1212").name)
    print(cl.get_by_phone("555-1313").name)
    print(cl.get_by_phone("555-1414").name)
    print(cl.get_by_phone("555-1515").name)
    print(cl.get_by_phone("555-1616").name)
    print(cl.get_by_phone("555-1717").name)
    print(cl.get_by_phone("555-1818").name)
    print(cl.get_by_phone("555-1919").name)
    
    print("\nGetting by id\n")
    print(cl.get_by_id(1).name)
    print(cl.get_by_id(2).name)
    print(cl.get_by_id(3).name)
    print(cl.get_by_id(4).name)
    print(cl.get_by_id(5).name)
    print(cl.get_by_id(6).name)
    print(cl.get_by_id(7).name)
    print(cl.get_by_id(8).name)
    
    print("\nRemoving\n")
    cl.remove(1)
    # cl.remove(2)
    # cl.remove(3)
    # cl.remove(4)
    # cl.remove(5)
    # cl.remove(6)
    # cl.remove(7)
    # cl.remove(8)
    
    print("\nGetting by name\n")
    # print(cl.get_by_name("Gandalf").name)
    print(cl.get_by_name("Frodo").name)
    print(cl.get_by_name("Sam").name)
    print(cl.get_by_name("Aragorn").name)
    print(cl.get_by_name("Legolas").name)
    print(cl.get_by_name("Gimli").name)
    print(cl.get_by_name("Boromir").name)
    print(cl.get_by_name("Gollum").name)
    
    print("\nGetting by phone\n")
    # print(cl.get_by_phone("555-1212").email)
    print(cl.get_by_phone("555-1313").email)
    print(cl.get_by_phone("555-1414").email)
    print(cl.get_by_phone("555-1515").email)
    print(cl.get_by_phone("555-1616").email)
    print(cl.get_by_phone("555-1717").email)
    print(cl.get_by_phone("555-1818").email)
    print(cl.get_by_phone("555-1919").email)
    
    print("\nGetting by id\n")
    # print(cl.get_by_id(1).name)
    print(cl.get_by_id(2).name)
    print(cl.get_by_id(3).name)
    print(cl.get_by_id(4).name)
    print(cl.get_by_id(5).name)
    print(cl.get_by_id(6).name)
    print(cl.get_by_id(7).name)
    print(cl.get_by_id(8).name)
    
    print("\nGetting ordered by name\n")
    for contact in cl.get_contacts_ordered_by_name():
        print(contact.name)
    