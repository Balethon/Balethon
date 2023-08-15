from setuptools import setup

with open("README.md", encoding="utf-8") as readme_md:
    readme = readme_md.read()

with open("requirements.txt", encoding="utf-8") as requirements_txt:
    requirements = [i.strip() for i in requirements_txt]

setup(
    name="Balethon",
    version="0.0.1",
    description="A python library for creating bots in Bale",
    long_description=readme,
    author="Sajjad",
    author_email="sajjadalipour2006@gmail.com",
    url="https://github.com/SajjadAlipour2006/Balethon",
    license="",
    keywords=["bale", "messanger", "bot", "api", "client"],
    install_requires=requirements,
    python_requires=">=3.7",
    project_urls={
        "Homepage": "https://github.com/SajjadAlipour2006/Balethon",
        "Tracker": "https://github.com/SajjadAlipour2006/Balethon/issues",
        "Community": "ble.ir/join/MTlhN2Q2Mz"
    }
)
