require "AssessmentBase.rb"

module Rec10
  include AssessmentBase

  def assessmentInitialize(course)
    super("rec10",course)
    @problems = []
  end

end
