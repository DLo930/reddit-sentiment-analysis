require "AssessmentBase.rb"

module Rec12
  include AssessmentBase

  def assessmentInitialize(course)
    super("rec12",course)
    @problems = []
  end

end
