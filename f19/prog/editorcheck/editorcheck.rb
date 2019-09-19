require "AssessmentBase.rb"


module Editorcheck
	include AssessmentBase


	def assessmentInitialize(course)
		super("editorcheck",course)
		@problems = []
	end

end

