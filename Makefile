.SILENT:
.PHONY: all clean current doc doc-srv serve tox


all:
	echo ""
	echo "  clean        Removes all temporary files"
	echo "  current      Runs the tox-environment for the current development"
	echo "  doc          Builds the documentation using 'Sphinx'"
	echo "  doc-srv      Serves the documentation on port 8082 (and automatically builds it)"
	echo "  serve        Runs the Django development server on port 8080"
	echo "  tox          Runs complete tox test"
	echo ""


# deletes all temporary files created by Django
clean:
	find . -iname "*.pyc" -delete
	find . -iname "__pycache__" -delete

current:
	tox -q -e util

doc:
	tox -q -e doc

doc-srv: doc
	tox -q -e doc-srv

serve:
	tox -q -e run

tox:
	tox -q
