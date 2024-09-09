# example-project

[![Release](https://img.shields.io/github/v/release/tfantunes/example-project)](https://img.shields.io/github/v/release/tfantunes/example-project)
[![Build status](https://img.shields.io/github/actions/workflow/status/tfantunes/example-project/main.yml?branch=main)](https://github.com/tfantunes/example-project/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/tfantunes/example-project/branch/main/graph/badge.svg)](https://codecov.io/gh/tfantunes/example-project)
[![Commit activity](https://img.shields.io/github/commit-activity/m/tfantunes/example-project)](https://img.shields.io/github/commit-activity/m/tfantunes/example-project)
[![License](https://img.shields.io/github/license/tfantunes/example-project)](https://img.shields.io/github/license/tfantunes/example-project)

This is a template repository for Python projects that use uv for their dependency management.

- **Github repository**: <https://github.com/tfantunes/example-project/>
- **Documentation** <https://tfantunes.github.io/example-project/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

##### Set git credentials manager if needed

Download the latest git-credentials-manager package

```bash
sudo dpkg -i <path-to-package>
git-credential-manager configure

export GCM_CREDENTIAL_STORE=cache
```

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:tfantunes/example-project.git
git push -u origin main
```

### 2. Setting Up The Development Environment

Install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Running the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Committing the changes

Lastly, commit the changes made by the two steps above to the repository. And repeat as you grow the project!

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

### 5. Setting up MkDocs and Github Page

For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).

### 6. Enabling Code coverage reports

To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
