all: install generate plot

install:
	@echo Installing the requirements
	pip3 install -r req.txt

generate: 
	g++ GenerateData.cpp -o gen.out
	chmod +x gen.out 
	./gen.out
	@echo Data generated!
	@echo 

plot: 
	@echo Plotting The 3.14E Chart
	@echo 
	python3 plot.py

clean: 
	rm -rf gen.out sample_data.txt 