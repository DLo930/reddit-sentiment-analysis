require "AssessmentBase.rb"


module Speller
	include AssessmentBase


	def assessmentInitialize(course)
		super("speller",course)
		@problems = []
	end

end
