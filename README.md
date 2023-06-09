# EASY CHEF
• Designed and developed a recipe-sharing social media web app in a team of 3 developers. 

• Used React to develop the front end and Django to develop the back end (with SQLite database). 

• Tested endpoints using Postman. 


## Accounts
• User sign-up, log-in, log-out, and edit profile functionality (first name, last name, email, avatar, phone number).

## Recipes
• Logged-in users can create recipes. A recipe has a name, a set of diets, cuisine, ingredients, serving size, and a list of steps. 

• They can add one or more photos/videos, prep time and cooking time to specific steps or to the overall recipe. 

• A recipe can be created based on another recipe (all fields are prefilled with the information of that base recipe)

• Logged-in users can edit or delete a recipe that they created.

• Logged-in users can create a combined shopping list of different recipes (with different serving sizes).

• Users can view all the details of a specific recipe on that recipe's page (including total likes, average rating, and comments). 

• Logged-in users can also add or remove the recipe from their shopping cart.


## Search
• Search through recipes by their name, ingredients, or creator.

• Filter recipes based on cuisine, diet, or cooking time.

• Search results sorted based on a combination of overall rating and the number of users who marked them as their favourite.

• Users can view lists of popular recipes (sorted by highest overall rating or most favourited).


## Social Media
• Logged-in users can rate recipes on a scale of 1 to 5. They can also update their vote later on.

• Logged-in users can also favourite/unfavourite recipes.

• Logged-in users can post comments on recipes (can include one or more pictures/videos).

• Logged-in users can view recipes they created, the recipes they favourited, and the recipes they interacted with (created, liked, rated, or commented on).


# RUNNING THE APPLICATION

**1.)** Clone the repository and navigate to it: `git clone https://github.com/agamjot-saini/EasyChef.git`

**2.)** These must be installed on the machine before running the **startup** and **run** scripts: 

**python3.10**, **pip** and **virtualenv** (accessible via `python3.10 -m`), and **Node.js 18**.

**3.)** The **_startup_** script runs all preparations such as creating the virtual env, pip installing all packages, migrations, npm install, etc. 

Run this command: `source startup.sh`

**4.)** The **_run_** script runs both backend and frontend servers. 

Run this command: `source run.sh`

## If the above steps don't work, follow these steps to run the app manually:

![EasyChefRunningInstructions](https://user-images.githubusercontent.com/65428409/235272796-eb8d5e0c-0ff9-4d54-b56b-ba73bfba811d.png)

