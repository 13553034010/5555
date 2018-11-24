import yaml,os,sys

def read_yaml():
    with open(os.getcwd()+os.sep+"Data"+os.sep+"login_data.yaml","r",encoding="utf-8")as f:
        return yaml.load(f)

