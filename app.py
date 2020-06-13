from database import add_entry, get_entries, create_table

menu = """Please Select one of the following options :
1) Add new entries for today.
2) View Entries
3) exit

Your Selection: """

welcome = "Welcome to the programming diary!"
create_table()
# entries = [
#     {"content": "Today I started learning programming", "date": "01/01/2020"},
#     {"content": "I created a SQLite Database" , "date": "02-01-2020"},
#     {"content": "I finished writing my programming diary application", "date": "03-01-2020"},
#     {"content": "Today I am going to continue learning programming", "date": "04/01/2020"},
# ]

def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


print(welcome)

user_input = input(menu)
while user_input != "3":
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        entries = get_entries()
        view_entries(entries)
    else:
        print("Invalid Input. Please try again")

    user_input = input(menu)
