require "AssessmentBase.rb"


module Images
	include AssessmentBase


	def assessmentInitialize(course)
		super("images",course)
		@problems = []
	end

end

