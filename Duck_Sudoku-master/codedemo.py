# Step 1
# Create a class named Organization, whose constructor takes a members
# parameter of type list. The members parameter is a list of organizations.
# Create another class Club inherating Organization, whose
# constructor takes a parameter name and a mems parameter of type list as well. This time,
# mems is a list of strings.
class Organization:
    def __init__(self, li: list["Organization"]):
        self.members = li

    def memlist(self):
        members = []
        for org in self.members:
            members += org.memlist()
        result = set(members)
        return result


class Club:
    def __init__(self, club_name: str, name: list[str]):
        self.club_name = club_name
        self.name = name

    def memlist(self):
        members = set()
        for member in self.name:
            members.add(member)
        return members




def main():
    basketball = Club("Basketball", ["Bob", "Alice"])
    volleyball = Club("Volleyball", ["Carl", "Bob", "Steven"])
    cooking = Club("Cooking", ["Mary", "Ashley"])
    painting = Club("Painting", ["Ashley", "Thomas"])
    music = Club("Music", ["Claire", "Jane"])
    sports = Organization([basketball, volleyball])
    arts = Organization([music, painting])
    orgs = Organization([sports, arts, cooking])
    all_mems = orgs.memlist()
    print(",".join([i for i in all_mems]))

if __name__ == "__main__":
    main()
#
# orgs is an organization, whose members are arts(Organization),
# sports(Organization), and cooking(Department).
#
# Step 2
# Implemente a method memlist in both classes. The method should return
# a collection of distinct names in the organization and possibly suborganizations.
#
#
# # example, continuing the main method above.

#
# Above code should print something like
# Jane,Ashley,Mary,Alice,Claire,Thomas,Bob,Steven,Carl