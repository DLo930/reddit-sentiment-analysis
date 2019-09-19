require "AssessmentBase.rb"


module Peg
	include AssessmentBase


	def assessmentInitialize(course)
		super("peg",course)
		@problems = []
	end

end

