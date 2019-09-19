require "AssessmentBase.rb"


module Strbuf
	include AssessmentBase


	def assessmentInitialize(course)
		super("strbuf",course)
		@problems = []
	end

end

