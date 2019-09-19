require "AssessmentBase.rb"


module Huffman
	include AssessmentBase


	def assessmentInitialize(course)
		super("huffman",course)
		@problems = []
	end

end
