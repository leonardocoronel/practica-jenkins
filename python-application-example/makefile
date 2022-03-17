all: clean build unit-test coverage package publish dockerize push

clean:
	@echo Clean STEP
	cd python && rm -rf dist .pytest_cache src/application_example/__pycache__ src/keeepcodingtest_leonardo.egg-info src/tests/.coverage src/tests/__pycache__
    #docker rmi --force leonardo7coronel/python-app-leonardo-devops:v1 2> /dev/null

build:
	@echo build STEP
	cd python && pip install -r requirements.txt

unit-test:
	@echo unit test STEP
	cd python/src/tests && coverage run -m pytest -s -v

coverage:
	@echo coverage STEP
	cd python/src/tests && coverage report -m --fail-under=20

package:
	@echo package STEP
	cd python && python3 -m build

publish:
	@echo publish STEP
	cd python && python3 -m twine upload dist/* --config-file ~/.pypirc --skip-existing --verbose

dockerize:
	@echo docker build STEP
	cd docker && docker build -f Dockerfile -t leonardo7coronel/python-app-leonardo-devops:v1 .

push:
	@echo push to dockerhub STEP
	docker push leonardo7coronel/pythonapp-leonardodevops:v1

integration_test:
	@echo Integration_TEST STEP
	docker run --rm leonardo7coronel/python-app-leonardo-devops:v1 