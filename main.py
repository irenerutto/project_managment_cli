import argparse

from utils.storage import load_data, save_data

# Create the main argument parser
parser = argparse.ArgumentParser(
    description="Project Management CLI"
)

# Create subcommands
subparsers = parser.add_subparsers(dest="command")

# Add user command
add_user = subparsers.add_parser(
    "add-user",
    help="Add a new user"
)

add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

# List users command
list_users = subparsers.add_parser(
    "list-users",
    help="Display all users"
)

# Add project command
add_project = subparsers.add_parser(
    "add-project",
    help="Add a project to a user"
)

add_project.add_argument("--user", required=True)
add_project.add_argument("--title", required=True)
add_project.add_argument("--description", required=True)
add_project.add_argument("--due-date", required=True)

# List projects command
list_projects = subparsers.add_parser(
    "list-projects",
    help="Display projects for a user"
)

list_projects.add_argument("--user", required=True)

# Add task command
add_task = subparsers.add_parser(
    "add-task",
    help="Add a task to a project"
)

add_task.add_argument("--user", required=True)
add_task.add_argument("--project", required=True)
add_task.add_argument("--title", required=True)
add_task.add_argument("--assigned-to", required=True)

# Read the command entered by the user
args = parser.parse_args()

# Handle add-user
if args.command == "add-user":

    data = load_data()

    data["users"].append({
        "name": args.name,
        "email": args.email,
        "projects": []
    })

    save_data(data)

    print("User added successfully!")

# Handle list-users
elif args.command == "list-users":

    data = load_data()

    if not data["users"]:
        print("No users found.")
    else:
        for user in data["users"]:
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print("-" * 30)

# Handle add-project
elif args.command == "add-project":

    data = load_data()

    for user in data["users"]:

        if user["name"] == args.user:

            user["projects"].append({
                "title": args.title,
                "description": args.description,
                "due_date": args.due_date,
                "tasks": []
            })

            save_data(data)

            print("Project added successfully!")

            break

    else:
        print("User not found.")

# Handle list-projects
elif args.command == "list-projects":

    data = load_data()

    for user in data["users"]:

        if user["name"] == args.user:

            if not user["projects"]:
                print("No projects found.")

            else:
                for project in user["projects"]:
                    print(f"Title: {project['title']}")
                    print(f"Description: {project['description']}")
                    print(f"Due Date: {project['due_date']}")
                    print("-" * 30)

            break

    else:
        print("User not found.")

# Handle add-task
elif args.command == "add-task":

    data = load_data()

    for user in data["users"]:

        if user["name"] == args.user:

            for project in user["projects"]:

                if project["title"] == args.project:

                    project["tasks"].append({
                        "title": args.title,
                        "status": "Pending",
                        "assigned_to": args.assigned_to
                    })

                    save_data(data)

                    print("Task added successfully!")

                    break

            else:
                print("Project not found.")

            break

    else:
        print("User not found.")

# No command entered
else:
    parser.print_help()