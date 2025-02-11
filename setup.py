import atexit
from setuptools import setup
from setuptools.command.install import install


def _post_install():
    import nltk

    nltk.download("wordnet")


class InstallNLTK(install):
    """Post-installation for installation mode."""

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(_post_install)


setup(
    name="lmms_api",
    version="1.0.0",
    description="A simple Python API wrapper for word-sense disambiguation.",
    url="git@github.com:andrewjong/LMMS.git",
    author="Andrew Jong",
    author_email="andrew.m.jong@gmail.com",
    license="unlicensed",
    packages=["lmms_api"],
    install_requires=[
        "tensorflow>=1.10.0,<2.0.0",
        "bert-serving-server==1.9.1",
        "bert-serving-client==1.9.1",
        "nltk==3.4.5",
        "spacy==2.1.3",
        "gdown==3.8.3",
        "psutil",
        "wget",
        "fastText @ git+https://github.com/facebookresearch/fastText.git@v0.2.0#egg=fastText-0.2.0",
        "en_core_web_sm @ git+https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz#egg=en_core_web_sm"
    ],
    zip_safe=False,
    python_requires=">=3.6",
    cmdclass={"install": InstallNLTK},
)
