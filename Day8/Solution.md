--- Corrected .prec-commit-config file as below
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.13
    hooks:
      - id: ruff

  - repo: https://github.com/psf/black-pre-commit-mirror
    rev: 26.5.1
    hooks:
      - id: black

<img width="1851" height="924" alt="image" src="https://github.com/user-attachments/assets/a064bdae-be20-4b6e-8e55-59722f179db3" />

root@controlplane ~/code ✖ cd fraud-detection/

root@controlplane fraud-detection on  main [!] via 🐍 v3.12.3 ➜  pre-commit install
pre-commit installed at .git/hooks/pre-commit

root@controlplane fraud-detection on  main [!] via 🐍 v3.12.3 ➜  pe-commit autoupdate
bash: pe-commit: command not found

root@controlplane fraud-detection on  main [!] via 🐍 v3.12.3 ✖ pre-commit autoupdate
An error has occurred: InvalidConfigError: 
==> File .pre-commit-config.yaml
==> At Config()
==> At key: repos
==> At Repository(repo='https://github.com/psf/black-pre-commit-mirror')
=====> Missing required key: rev
Check the log at /root/.cache/pre-commit/pre-commit.log

root@controlplane fraud-detection on  main [!] via 🐍 v3.12.3 ✖ pre-commit autoupdate
[https://github.com/pre-commit/pre-commit-hooks] Cannot update because the update target is missing these hooks: check_yaml
[https://github.com/astral-sh/ruff-pre-commit] Cannot update because the update target is missing these hooks: ruff-lint
[https://github.com/psf/black-pre-commit-mirror] updating v0.1.0 -> 26.5.1

root@controlplane fraud-detection on  main [!] via 🐍 v3.12.3 ✖ pre-commit autoupdate
[https://github.com/pre-commit/pre-commit-hooks] updating v2.3.0 -> v6.0.0
[https://github.com/astral-sh/ruff-pre-commit] updating v0.1.0 -> v0.15.13
[https://github.com/psf/black-pre-commit-mirror] already up to date!

root@controlplane fraud-detection on  main [!] via 🐍 v3.12.3 ➜  pre-commit autoupdate
[https://github.com/pre-commit/pre-commit-hooks] already up to date!
[https://github.com/astral-sh/ruff-pre-commit] already up to date!
[https://github.com/psf/black-pre-commit-mirror] already up to date!

root@controlplane fraud-detection on  main [!] via 🐍 v3.12.3 ➜  pre-commit run --all-files
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Initializing environment for https://github.com/astral-sh/ruff-pre-commit.
[INFO] Initializing environment for https://github.com/psf/black-pre-commit-mirror.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/astral-sh/ruff-pre-commit.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/psf/black-pre-commit-mirror.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
trim trailing whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing process.py

fix end of files.........................................................Passed
check yaml...............................................................Passed
ruff (legacy alias)......................................................Passed
black....................................................................Passed

root@controlplane fraud-detection on  main [!] via 🐍 v3.12.3 ✖ 
