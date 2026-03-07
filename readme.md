To create a a venv

```
python3 -m venv <sai_env> # run one time to create venv, conda venv
source <sai_env>/bin/activate # you will run each and every time to activate
deactivate # to deactivate venv
```

2. individual package installation
pip install pandas

3. to install packages from requirements.txt
pip install -r requirements.txt

4. To create requirements.txt after installing each and every packages manually using step 2
pip freeze > requirements.txt ( overwrite)
pip freeze >> requirements.txt ( append)

to create unit test file for a code named <calc>.py, unit test file name is test_<calc>.py
after activating the venv, to run the unit test cases. execute pytest from your main working directory