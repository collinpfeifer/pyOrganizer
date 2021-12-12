# pyOrganizer

An automated organization tool developed for Python 3 with [watchdog](https://pythonhosted.org/watchdog/)

## Requirements
This repository has included a requirements.txt file for all the required dependencies. A virtual environment is also recomended for all python projects, but it is optional.

Virtual environment installation using [pip](https://pypi.org/project/pip/)

```bash
pip install virtualenv
```

Dependency librairies installation using [pip](https://pypi.org/project/pip/)

```bash
pip install watchdog
```

## Usage

When you run the program, you will be prompted for a to-be-modified folder. From there, a new folder will be created in the parent directory of the given folder. From here all files in the given directory will be moved and renamed. I chose to move but not rename directories and the files inside due to issues with naming and downloads that could possibly be within the given directory and wouldn't want to be changed. This program can be run in any directory, as long as the parent directory given when prompted is correct.

## Contributions

Pull requests are welcome, major changes should be taken up with an issue to first discuss what you would like to change

## License

[MIT](https://choosealicense.com/licenses/mit/)
