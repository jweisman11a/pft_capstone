## Working on a new task

#### Pull latest from the main branch
First, you'll need to make sure your local version of the main branch is up-to-date.
*git checkout master*
*git pull origin master*


#### Create new branch
Next, create a new branch for your task.
*git checkout -b Ticket#-TaskName*


#### Commit changes
Now, make the changes you need to the codebase, create unit tests if needed, and when you're ready for a code review, push your code to the repository. You'll first commit your work to your local branch and then push it to the repository.
*git add .*
*git commit -m "Updated some code to do cool stuff"*
*git push origin Ticket#-TaskName*


#### Merge your working branch with the main branch
Running the rebase from the main branch may cause merge conflicts with your local branch. You'll need to resolve the merge conflict. After that, we'll merge the branch into the main branch and push the new branch to the remote repository.
*git checkout master*
*git merge Ticket#-TaskName*
*git push origin master*


#### Delete your local and remote working branch
Once your code is merged into the main branch, we'll wan to delete the working branch to ensure the project remains clean.
*git branch -d Ticket#-TaskName*
*git push origin --delete Ticket#-TaskName*