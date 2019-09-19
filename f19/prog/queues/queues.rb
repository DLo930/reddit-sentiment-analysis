require "AssessmentBase.rb"


module Queues
	include AssessmentBase


	def assessmentInitialize(course)
		super("queues",course)
		@problems = []
	end

end

