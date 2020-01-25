import logging
import colorlog

def format_references(references, n=5):
    return references['references'][:n]

def create_logger(name=__name__, verbose=False):
    if verbose:
        colorlog.root.setLevel(level=logging.DEBUG)
    else:
        colorlog.root.setLevel(level=logging.WARNING)

    logger = colorlog.root

    # prevent multiple streams
    if not logger.handlers:
        handler = colorlog.StreamHandler()
        fmt_str = '[%(asctime)s] %(log_color)s%(levelname)s @ line %(lineno)d: %(message)s'
        colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white',
        }

        handler.setFormatter(
            colorlog.ColoredFormatter(fmt_str,log_colors=colors))


        logger.addHandler(handler)
    
      
    return logger
