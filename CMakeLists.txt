cmake_minimum_required(VERSION 3.10)

#project name
project(Kylo)

#install flask and run main.py
execute_process (
  COMMAND bash -c "pip3 install flask"
  COMMAND bash -c "python3 main.py"
)
