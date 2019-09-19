TARGET:=../../handout-
### What not to interpret as files
.PHONY: help handout


### Print help message
help:
	@echo "make [help]         -- print these instructions"
	@echo "make handout arg=NN -- create handout-NN.tgz"

handout:
	@mv handout tmp
	@cp -a tmp handout
	@cp -a ../images/handout/* handout
	@tar cfz $(TARGET)$(arg).tgz handout
	@rm -rf handout
	@mv tmp handout
