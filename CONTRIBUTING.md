### Contributing to Formica

Thanks for contributing to formica! Make sure to Fork this repository into your account before making any commits. Then use the following commands to set up the project.

```jsx
git clone https://github.com/<your-github-username>/formica
cd formica
git remote add upstream https://github.com/felixfaisal/formica.git
git pull upstream main
npm install
```

Firstly, if you are afraid or unsure about anything, just ask or submit the issue or a pull request. You won't be yelled at for putting in your best effort. The worst that can happen is that you'll be politely asked to change something.

For a detailed guidance, read further.

All development happens on the develop branch. The main branch contains the known stable version of AOW. To make your contributions, create a new branch from develop.

```
git checkout staging
git checkout -b <"Add relevant name for branch">
```

### Committing your changes and creating a PR

Now you can make your changes, and commit them. We don't have any specific convention as of now, but try to have a clear and summarized message for your commits.

```jsx
git add .
git status
git commit -m "My fixes"

```

Sync your forked repository with the changes in this(upstream) repository

```jsx
git fetch upstream
git rebase upstream/staging
```

Push the changes to your fork.

```jsx
git push origin <"Branch-Name">
```

```jsx
Got to github and create Pull Request
```

This is a good time, to open a pull request in this repository with the changes you have made. Make sure you open a pull request to merge to develop branch and not the main branch directly.

### How can I contribute?

**Reporting bugs:**

- Make sure you test against the latest version. There is a possibility that this bug has already been fixed.

**Report an issue here:**

- Use a descriptive title for the issue.
- Try to describe the steps to reproduce the problem that you are facing.
- Provide Examples and screenshots to demonstrate the steps if possible.

**Common Contribution Guidelines:**

- Make sure there is an issue reported, related to the work that you are doing.
- To prevent any duplication, comment under the issue.
- Push your commits and refer to the issue using fix `#<issue-no>` or close `#<issue-no>` in the commit message.
- Please don't make untested PRs.

**Commit Messages:**

- Write a short (50 chars or less) summary of changes.
- Optional body for a more detailed description of the change. Refer to [this](https://github.com/erlang/otp/wiki/writing-good-commit-messages) for a detailed overview.

**Credits:** Some parts of this are taken from: [PostgREST CONTRIBUTING.md](https://github.com/PostgREST/postgrest/blob/main/.github/CONTRIBUTING.md)
