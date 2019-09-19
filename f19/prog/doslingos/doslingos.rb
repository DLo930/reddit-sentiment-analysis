require "AssessmentBase.rb"


module Doslingos
	include AssessmentBase


	def assessmentInitialize(course)
		super("doslingos",course)
		@problems = []
	end

end

