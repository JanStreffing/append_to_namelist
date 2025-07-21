import os

def append_to_namelist(config):
    """
    Runs a preprocessing shell script
    """
    pp_method = pp_type = None
    for model in config["general"]["valid_model_names"]:
        if "append_to_namelist" in config[model]:
            for name in config[model]["append_to_namelist"]:
                if "method" in config[model]["append_to_namelist"][name]:
                    pp_method = config[model]["append_to_namelist"][name]["method"]
                if "type" in config[model]["append_to_namelist"][name]:
                    pp_type = config[model]["append_to_namelist"][name]["type"]
                if pp_type == "shell" and pp_method:
                    #try:
                    os.system(pp_method)
                    #except:
                    #    print("Shell execution of command: '" + pp_method + "' failed, please check...")
    return config
                
