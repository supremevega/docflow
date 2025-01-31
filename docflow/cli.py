import argparse
from .core.file_watcher import DebouncedHandler, Observer
import logging

def main():
    parser = argparse.ArgumentParser(description='DocFlow - Automated Document Organization')
    parser.add_argument('--daemon', action='store_true', help='Run in daemon mode')
    parser.add_argument('--config', default='config/default_config.yaml', 
                      help='Path to config file')
    args = parser.parse_args()

    logging.basicConfig(
        filename='docflow.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    event_handler = DebouncedHandler()
    observer = Observer()
    observer.schedule(event_handler, path='~/Downloads', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
