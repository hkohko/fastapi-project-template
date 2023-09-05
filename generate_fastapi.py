import logging
from sys import prefix, base_prefix
from pathlib import PurePath, Path

logger = logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


_MAIN_DIR = PurePath(__file__).parents[0]
_APP_DIR = _MAIN_DIR.joinpath("app")
_INTERNAL_DIR = _APP_DIR.joinpath("internal")
_MODEL_DIR = _APP_DIR.joinpath("model")
_ROUTER_DIR = _APP_DIR.joinpath("router")
_DB_DIR = _APP_DIR.joinpath("db")

_DIR_LIST = (_APP_DIR, _INTERNAL_DIR, _MODEL_DIR, _ROUTER_DIR, _DB_DIR)

_TOUCH = ("main.py", "__init__.py")


def create_folder_structure():
    for DIR in _DIR_LIST:
        if not Path(DIR).exists():
            Path.mkdir(DIR)
            logging.info(f"created {DIR}")
        else:
            logging.info(f"Folder {DIR.name} already exists!")


def create_init_files():
    for DIR in _DIR_LIST:
        for mkfile in _TOUCH:
            checkfile = Path(DIR).joinpath(mkfile)
            if not checkfile.exists() and Path(DIR) == _APP_DIR:
                mkfile_app = Path(DIR).joinpath(mkfile)
                mkfile_app.touch(exist_ok=True)
                logging.info(f"created {mkfile_app}")
            elif not checkfile.exists():
                if checkfile == Path(DIR).joinpath(_TOUCH[1]):
                    mkfile_inits = Path(DIR).joinpath(_TOUCH[1])
                    mkfile_inits.touch(exist_ok=True)
                    logging.info(f"created {mkfile_inits.name}")
            else:
                logging.info(f"File {mkfile} already exists!")


def is_venv():
    return prefix != base_prefix


def main():
    create_folder_structure()
    create_init_files()


if __name__ == "__main__":
    main()
