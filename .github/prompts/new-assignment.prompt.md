---
mode: agent
description: Create a new programming homework assignment
---

# Create New Programming Assignment

Your goal is to generate a new homework assignment for the Mergington High School students.

## Step 1: Gather Assignment Information

If not already provided by the user, ask what the assignment will be about.

## Step 2: Create Assignment Structure

1. Create a new directory in the `assignments` folder with a unique name based on the assignment topic
1. Create a new file in the directory named `README.md` with the structure from the [assignment-template.md](../../templates/assignment-template.md) file
1. Fill out the assignment details in the README file
1. (Optional) Add starter code or attachments if the assignment needs them - add these files to the same assignment folder

## Step 3: Update Website Configuration

Update the assignments list in [config.json](../../config.json) website configuration file to include the new assignment. For the dueDate field, use the current date plus 7 days unless specified otherwise.
⌨️ Activity: Test the Assignment Prompt
Open Copilot Chat in VS Code and ensure you're in Agent mode.

Run your prompt by typing /new-assignment in the chat input. There are 2 options:

Type just /new-assignment without a description. Copilot will ask what the assignment should be about.

Include the topic directly: /new-assignment Building REST APIs with FastAPI framework

💡 Assignment Topic Ideas
Verify the new assignment appears in the assignments list on the website preview.

Assignment not showing? 🔍
Review the generated assignment content to ensure it matches your established conventions.

Commit and push your changes:

The new prompt file: .github/prompts/new-assignment.prompt.md
The generated assignment directory and files.
Updated config.json configuration.
Wait for Mona to prepare the next step! (See <attachments> above for file contents. You may not need to search or read the file again.)
