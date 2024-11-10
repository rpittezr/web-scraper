import os, sys

PWD = os.getenv("PWD")
DJANGO_PROJECT = os.environ.get("DJANGO_PROJECT") or "config"
DJANGO_ROOT_DIR = os.environ.get("DJANGO_ROOT_DIR") or "src"
if not PWD.endswith(f"/{DJANGO_ROOT_DIR}"):
    # src is the django-root
    PWD = os.path.join(PWD, DJANGO_ROOT_DIR)