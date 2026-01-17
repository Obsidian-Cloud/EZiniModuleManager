# libutils.py
import traceback


def parse_traceback() -> None:
    """Parses the traceback stack for console debugging
    
    This function extracts the traceback stack. 
    It filters though each frame in the stack to find
    specific values to return for console debugging.
    """
    tags = ['register_obj(', 'get_obj(', 'import_modlist(']
    # Extract the traceback stack 
    stack_sum = traceback.format_list(traceback.extract_stack())    

    _debug = []
    for line in stack_sum:
        if any(tag in line for tag in tags):
            _debug.append(line)
            continue

    n = 1
    for line in _debug:
       print(f'Stack Trace ({n}): ')
       print(line)
       n += 1
    n = 1