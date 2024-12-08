# Lamarziendan

Lamarziendan was a series of pop up art performances in various
locations in ’s-Hertogenbosch. This repository contains the source
code for its website, as well as an archived copy that can be viewed
on https://lamarziendan.created.today/

## Installation

Install Python and run the following commands:

    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

## Usage

Visit https://localhost:8000/admin/lamarziendan/edition/ to add
a new edition.
