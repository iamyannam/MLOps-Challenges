
root@controlplane ~/code via 🐍 v3.12.3 ✖ pwd
/root/code

root@controlplane ~/code via 🐍 v3.12.3 ✖ ls
README.md  jupyter_lab_config.py  ml-env

root@controlplane ~/code via 🐍 v3.12.3 ➜  pwd
/root/code

root@controlplane ~/code via 🐍 v3.12.3 ➜  cd ..

root@controlplane ~ ➜  ls
code

root@controlplane ~ ➜  mkdir notebooks

root@controlplane ~ ➜  ls
code  notebooks

root@controlplane ~ ➜  ls -ltr
total 8
drwxr-xr-x 3 root root 4096 May 14 06:46 code
drwxr-xr-x 2 root root 4096 May 14 06:52 notebooks

root@controlplane ~ ➜  cd code

root@controlplane ~/code via 🐍 v3.12.3 ➜  ls
README.md  jupyter_lab_config.py  ml-env

root@controlplane ~/code via 🐍 v3.12.3 ➜  vi jupyter_lab_config.py 

root@controlplane ~/code via 🐍 v3.12.3 ➜  source ml-env/bin/activate

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ✦ ✖ jupyter lab --config=/root/code/jupyter_lab_config.py --allow-root --no-browser &
[1] 4935

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ✦ ➜  [W 2026-05-14 06:58:52.686 ServerApp] ServerApp.token config is deprecated in 2.0. Use IdentityProvider.token.
[W 2026-05-14 06:58:52.686 ServerApp] notebook_dir is deprecated, use root_dir
[W 2026-05-14 06:58:52.704 ServerApp] notebook | error adding extension (enabled: True): The module 'notebook' could not be found (No module named 'notebook'). Are you sure the extension is installed?
    Traceback (most recent call last):
      File "/root/code/ml-env/lib/python3.12/site-packages/jupyter_server/extension/manager.py", line 365, in add_extension
        extpkg = ExtensionPackage(name=extension_name, enabled=enabled)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/root/code/ml-env/lib/python3.12/site-packages/jupyter_server/extension/manager.py", line 219, in __init__
        self._load_metadata()
      File "/root/code/ml-env/lib/python3.12/site-packages/jupyter_server/extension/manager.py", line 234, in _load_metadata
        raise ExtensionModuleNotFound(msg) from None
    jupyter_server.extension.utils.ExtensionModuleNotFound: The module 'notebook' could not be found (No module named 'notebook'). Are you sure the extension is installed?
[I 2026-05-14 06:58:52.705 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2026-05-14 06:58:52.708 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2026-05-14 06:58:52.711 ServerApp] jupyterlab | extension was successfully linked.
[I 2026-05-14 06:58:52.712 ServerApp] Writing Jupyter server cookie secret to /root/.local/share/jupyter/runtime/jupyter_cookie_secret
[I 2026-05-14 06:58:52.926 ServerApp] notebook_shim | extension was successfully linked.
[W 2026-05-14 06:58:52.935 ServerApp] All authentication is disabled.  Anyone who can connect to this server will be able to run code.
[I 2026-05-14 06:58:52.935 ServerApp] notebook_shim | extension was successfully loaded.
[I 2026-05-14 06:58:52.937 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2026-05-14 06:58:52.937 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2026-05-14 06:58:52.939 LabApp] JupyterLab extension loaded from /root/code/ml-env/lib/python3.12/site-packages/jupyterlab
[I 2026-05-14 06:58:52.939 LabApp] JupyterLab application directory is /root/code/ml-env/share/jupyter/lab
[I 2026-05-14 06:58:52.939 LabApp] Extension Manager is 'pypi'.
[I 2026-05-14 06:58:52.967 ServerApp] jupyterlab | extension was successfully loaded.
[I 2026-05-14 06:58:52.968 ServerApp] Serving notebooks from local directory: /root/notebooks
[I 2026-05-14 06:58:52.968 ServerApp] Jupyter Server 2.18.2 is running at:
[I 2026-05-14 06:58:52.968 ServerApp] http://controlplane:8888/lab
[I 2026-05-14 06:58:52.968 ServerApp]     http://127.0.0.1:8888/lab
[I 2026-05-14 06:58:52.968 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[I 2026-05-14 06:58:53.329 ServerApp] Skipped non-installed server(s): basedpyright, bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyrefly, pyright, python-language-server, python-lsp-server, r-languageserver, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin, vscode-json-languageserver-bin, yaml-language-server
[I 2026-05-14 06:59:05.600 ServerApp] 302 GET / (@10.244.153.170) 0.41ms
[W 2026-05-14 06:59:14.345 LabApp] Could not determine jupyterlab build status without nodejs
[I 2026-05-14 06:59:24.515 ServerApp] New terminal with automatic name: 1
[W 2026-05-14 06:59:25.802 ServerApp] The websocket_ping_timeout (90000) cannot be longer than the websocket_ping_interval (30000).
    Setting websocket_ping_timeout=30000
