require "AssessmentBase.rb"


module Pixels
	include AssessmentBase


	def assessmentInitialize(course)
		super("pixels",course)
		@problems = []
	end

end

