# String Mutation CLI
#### Jack Nelson

## Install Environment
Execute the below in root directory.
```
python3.9 -m venv env
source env/bin/activate 
```

## Run Tests
To run the test suit execute the below in root folder.
```
pytest
```

## Run Application
To run application, use the below:
```
./main.py ./data/dev/sample.txt
```
Default behavour is to reverse all strings, this can also be achieved by:
```
./main.py ./data/dev/sample.txt -r
```
To reverse word, use the `-w` flag:
```
./main.py ./data/dev/sample.txt -w
```

## Troubleshooting
If you run into permission issues, run the below on main.py:
```
chmod 777 main.py
```