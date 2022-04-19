comandos:
	@echo ""
	@echo "	COMANDOS"
	@echo ""
	@echo "	install"
	@echo "	ejecutar"
	@echo ""

iniciar:
	@pipenv install

ejecutar:
	@pipenv run flask run
